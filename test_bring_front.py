#!c:\SDK\Anaconda2\python.exe
#  import win32gui

#  def windowEnumerationHandler(hwnd, top_windows):
    #  top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

#  if __name__ == "__main__":
	#  results = []
	#  top_windows = []
	#  win32gui.EnumWindows(windowEnumerationHandler, top_windows)
	#  for i in top_windows:
		#  print "i 0 =", i
		#  if "ping" in i[1].lower():
			#  print i
			#  win32gui.ShowWindow(i[0],5)
			#  win32gui.SetForegroundWindow(i[0])
			#  break
			
			
import sys
import traceback
try:
	print sys.argv[1]
except:
	traceback.format_exc()