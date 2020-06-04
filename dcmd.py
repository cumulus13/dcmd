import win32api, win32gui, win32con
from ctypes import windll, byref, wintypes
from ctypes.wintypes import SMALL_RECT
import ctypes
import winbase
import struct
import sys
if sys.version_info.major == 3:
	raw_input = input
	
	
class COORD(ctypes.Structure):
	_fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
	LF_FACESIZE = 32 
	_fields_ = [
				("cbSize", ctypes.c_ulong),
				("nFont", ctypes.c_ulong),
				("dwFontSize", COORD),
				("FontFamily", ctypes.c_uint),
				("FontWeight", ctypes.c_uint),
				("FaceName", ctypes.c_wchar * LF_FACESIZE)
	]
	

class dcmd(object):
	def __init__(self):
		super(dcmd, self)
		self.STDOUT = -11
		self.hdl = windll.kernel32.GetStdHandle(self.STDOUT)
		self.foreground_handle = win32gui.GetForegroundWindow()
		
	def getScreenSize(self):
		return win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)

	def setPosition(self, left, top, right, bottom):
		
		#rect = wintypes.SMALL_RECT(0, 0, 100, 80) # (left, top, right, bottom) 
		rect = wintypes.SMALL_RECT(left, top, right, bottom) # (left, top, right, bottom) 
		windll.kernel32.SetConsoleWindowInfo(self.hdl, True, byref(rect))
		
	def setBuffer(self, rows=None, columns=None):
		width, height, curx, cury, wattr, left, top, right, bottom, maxx, maxy = self.getBuffer()
		if not rows:
			rows = width
		if not columns:
			columns = height
			
		#bufsize = wintypes._COORD(100, 80) # rows, columns
		bufsize = wintypes._COORD(rows, columns) # rows, columns
		windll.kernel32.SetConsoleScreenBufferSize(self.hdl, bufsize)
		
	def getBuffer(self):
		csbi = ctypes.create_string_buffer(22)
		res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(self.hdl, csbi)
		width, height, curx, cury, wattr, left, top, right, bottom, maxx, maxy = struct.unpack("hhhhHhhhhhh", csbi.raw)
		return width, height, curx, cury, wattr, left, top, right, bottom, maxx, maxy
		#return winbase.GetConsoleScreenBufferInfo()
		
	def setSize(self, width=None, height=None, x = None, y = None, center=False):
		x1 = x
		y1 = y
		#  print("x =", x)
		#  print("y =", y)
		#  print("height =", height)
		x0, y0, width0, height0 = win32gui.GetWindowRect(self.foreground_handle)
		if x and str(x).isdigit():
			x = int(x)
		if y and str(y).isdigit():
			y = int(y)
		if not x:
			if x == 0:
				x = 0
			else:
				x = x0
		if not y:
			if y == 0:
				y = 0
			else:
				y = y0
		if not width:
			width = width0 - x
		if not height:
			height = height0 - y
		
		if x == "right" or x == "r":
			x = win32api.GetSystemMetrics(0) - width
			y = y0
		if x == "left" or x == "l":
			x = 0
			y = y0
		if x == "button" or x == "b" or y == "button" or y == "b":
			y = win32api.GetSystemMetrics(1) - height
			x = x0
		if x == "top" or x == "t" or y == "top" or y == "t":
			y = 30
			x = x0
		if x == 'c' or y == 'c':
			center = True
			x = x0
		
		#win32gui.MoveWindow(self.foreground_handle, win32api.GetSystemMetrics(0)/3, win32api.GetSystemMetrics(1)/9, 500, 170, True)
		#  print("height =", height)
		if center:
			#  print("x =",x)
			#  print("y =",y)
			#  print("width =", width)
			#  print("height =", height)
			win32gui.MoveWindow(self.foreground_handle, int(win32api.GetSystemMetrics(0)/3), int(win32api.GetSystemMetrics(1)/10), width, height, True)
		else:
			#  print("x =",x)
			#  print("y =",y)
			#  print("width =", width)
			#  print("height =", height)
			win32gui.MoveWindow(self.foreground_handle, x, y, width, height, True)
			
	def setAlwaysOnTop(self, width, height, x = 0, y = 0, center=False):
		#win32gui.SetWindowPos(self.foreground_handle, win32con.HWND_TOPMOST,win32api.GetSystemMetrics(0)/3,win32api.GetSystemMetrics(1)/3,500,170,0)
		if center:
			win32gui.SetWindowPos(self.foreground_handle, win32con.HWND_TOPMOST, int(win32api.GetSystemMetrics(0)/3), int(win32api.GetSystemMetrics(1)/10), width, height, 0)
		else:
			win32gui.SetWindowPos(self.foreground_handle, win32con.HWND_TOPMOST, x, y, width, height, 0)
			
	def setNormal(self, width, height):
		win32gui.SetWindowPos(self.foreground_handle, win32con.HWND_NOTOPMOST, int(win32api.GetSystemMetrics(0)/3), int(win32api.GetSystemMetrics(1)/10), width, height, 0)
		
	def changeFont(self, nfont=12, xfont=11, yfont=18, ffont=54, wfont=400, name="Lucida Console"):
		font = CONSOLE_FONT_INFOEX() 
		font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
		font.nFont = nfont
		font.dwFontSize.X = xfont
		font.dwFontSize.Y = yfont
		font.FontFamily = ffont
		font.FontWeight = wfont
		font.FaceName = name
		#  print("yfont =", yfont)
		#  print("name  =", name)
		ctypes.windll.kernel32.SetCurrentConsoleFontEx(self.hdl, ctypes.c_long(False), ctypes.pointer(font))
		
	def getListWindows(self):
		def enumsHandle(hwnd, lParam):
			title = win32gui.GetWindowText(hwnd)
			excpt = ["Form1", "Default IME", "MSCTFIME UI", "frmTray", "frmBar", "frmLine1", "frmLine2", "frmLine3", "frmLine4", "frmLine5", "Rating", "CD Art Display 1.x Class", "CADnotifier", "CiceroUIWndFrame", "VistaSwitcher", "DDE Server Window", "uninteresting", "DWM Notification Window", "EndSessionWindow", "Program Manager", "GetPosWnd", "igfxtrayWindow"]
			if title and not title in excpt and not len(title) == 1:
				print(title)
		
		win32gui.EnumWindows(enumsHandle, None)
		
	def setTop(self, name = None, normal=False):
		hdls = []
		if name:
			def enumsHandle(hwnd, lParam):
				title = win32gui.GetWindowText(hwnd)
				if name.lower() in title.lower() or name.lower() == title.lower():
					hdls.append([hwnd, title])
			win32gui.EnumWindows(enumsHandle, None)
			
			if hdls:
				if len(hdls) > 1:
					n = 1
					for i in hdls:
						print(str(n) + ". " + i[1])
					q = raw_input("Select number to top: ")
					if q and str(q).isdigit() and not int(q) >  len(hdls):
						h = hdls[int(q) - 1][0]
						rect = win32gui.GetWindowRect(h)
						if normal:
							win32gui.SetWindowPos(h, win32con.HWND_NOTOPMOST, rect[0], rect[1], rect[2], rect[3], 0)
						else:
							win32gui.SetWindowPos(h, win32con.HWND_TOPMOST, rect[0], rect[1], rect[2], rect[3], 0)
		else:
			rect = win32gui.GetWindowRect(self.foreground_handle)
			if normal:
				win32gui.SetWindowPos(self.foreground_handle, win32con.HWND_NOTOPMOST, rect[0], rect[1], rect[2], rect[3], 0)
			else:
				win32gui.SetWindowPos(self.foreground_handle, win32con.HWND_TOPMOST, rect[0], rect[1], rect[2], rect[3], 0)
		
	def usage(self):
		import argparse
		import sys
		parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)
		parser.add_argument('-W', '--width', action='store', help='Set Width', type = int)
		parser.add_argument('-H', '--height', action='store', help='Set Height', type = int)
		parser.add_argument('-x', '--xpos', action='store', help='X position')
		parser.add_argument('-y', '--ypos', action='store', help='Y position')
		parser.add_argument('-c', '--center', action='store_true', help='By pass X,Y then centering it')
		parser.add_argument('-gb', '--get-buffer', action='store_true', help='Get current buffer')
		parser.add_argument('-bc', '--buffer-column', action='store', help='Set Buffer colums', type = int)
		parser.add_argument('-br', '--buffer-row', action='store', help='Set Buffer rows', type = int)
		parser.add_argument('-f', '--font', action='store', help='Change font name', default = "Consolas")
		parser.add_argument('-fs', '--font-size', action='store', help='Change font size', type = int, default = 13)#, required='--font')
		parser.add_argument('-fb', '--font-bold', action='store', help='Change font bold', type = int, default = 400)#, required='--font')
		parser.add_argument('-l', '--list-window', action='store_true', help='Show all window active name/title')
		parser.add_argument('-t', '--always-top', action='store_true', help='Set always on top')
		parser.add_argument('-nt', '--not-always-top', action='store_true', help='Set always on top to normal')
		parser.add_argument('-T', '--always-top-this', action='store_true', help='Set always on top for this terminal')
		parser.add_argument('-nT', '--not-always-top-this', action='store_true', help='Set always on top for this terminal to normal')
		
		if len(sys.argv) == 1:
			parser.print_help()
		else:
			args = parser.parse_args()
			if args.width or args.height or args.xpos or args.ypos or args.center:
				self.setSize(args.width, args.height, args.xpos, args.ypos, args.center)
			if args.get_buffer:
				width, height, curx, cury, wattr, left, top, right, bottom, maxx, maxy = self.getBuffer()
				print("WIDTH  =", width)
				print("HEIGHT =", height)
				print("CURX   =", curx)
				print("CURY   =", cury)
				print("WATTR  =", wattr)
				print("LEFT   =", left)
				print("RIGHT  =", right)
				print("TOP    =", top)
				print("BOTTOM =", bottom)
				print("MAX-X  =", maxx)
				print("MAX-y  =", maxy)
			if args.buffer_column or args.buffer_row:
				self.setBuffer(args.buffer_row, args.buffer_column)
			if args.font or args.font_size or args.font_bold:
				self.changeFont(nfont=12, xfont=11, yfont=args.font_size, ffont=54, wfont=args.font_bold, name=args.font)
			if args.list_window:
				self.getListWindows()
			if args.always_top:
				self.setTop(args.always_top)
			if args.not_always_top:
				self.setTop(args.not_always_top, normal=True)
			if args.always_top_this:
				self.setTop()
			if args.not_always_top_this:
				self.setTop(normal=True)
			
		
if __name__ == '__main__':
	c = dcmd()
	c.usage()
		
		