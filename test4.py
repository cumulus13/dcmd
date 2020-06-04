#!c:/SDK/Anaconda2/python.exe
import win32api, win32gui, win32con
from ctypes import windll, byref, wintypes
from ctypes.wintypes import SMALL_RECT
from pause import pause

STDOUT = -11
hdl = windll.kernel32.GetStdHandle(STDOUT)
fd = win32gui.GetForegroundWindow()
style = win32con.GWL_STYLE | win32con.WS_MAXIMIZEBOX
lPtr = win32gui.GetWindowLong(fd, win32con.WS_BORDER)

#win32gui.SetWindowLong(fd, win32con.GWL_STYLE, win32gui.GetWindowLong(fd, style))
win32gui.SetWindowLong(fd, win32con.GWL_STYLE, lPtr)
