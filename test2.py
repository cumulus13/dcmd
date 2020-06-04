#!c:/SDK/Anaconda2/python.exe
from __future__ import print_function

import win32gui, win32con, win32api, win32ui
import os
import time

def load(img = os.path.join(os.path.dirname(__file__), "image.ico")):
	hdl = win32gui.GetForegroundWindow()
	#img = os.path.join(os.path.dirname(__file__), "image.ico")
	img = os.path.join(os.path.dirname(__file__), "logo.png")
	icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
	hicon = win32gui.LoadImage(hdl, img, win32con.IMAGE_BITMAP, 100, 100, icon_flags)
	hdc = win32gui.GetDC(hdl)
	n = 1
	while 1:
		if n <= 10:
			win32gui.DrawIcon(hdc, 100, 100, hicon)
			time.sleep(1)
			n+=1
		else:
			break

#hdl = win32gui.GetForegroundWindow()
#img = os.path.join(os.path.dirname(__file__), "image.ico")
#img = os.path.join(os.path.dirname(__file__), "logo.png")
#img = r"d:\DOWNLOADS\images\243.jpg"
#icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
#hicon = win32gui.LoadImage(hdl, img, win32con.IMAGE_ICON, 100, 100, icon_flags)
#hdc = win32gui.GetDC(hdl)
#win32gui.LoadIcon(0, win32con.IDI_APPLICATION)

#icoX = win32api.GetSystemMetrics(win32con.SM_CXICON)
#icoY = win32api.GetSystemMetrics(win32con.SM_CXICON)

#hdc = win32ui.CreateDCFromHandle(hdl) 
#hbmp = win32ui.CreateBitmap()
#hbmp.CreateCompatibleBitmap(hdc, icoX, icoX)
#hdc = hdc.CreateCompatibleDC()

#hdc.SelectObject(hbmp)
#hdc.DrawIcon((100,100), hicon)

#win32gui.DrawIcon(hdc, 100, 100, hicon)
 
#  className = "PythonDocSearch" 
#  wc = win32gui.WNDCLASS()
#  wc.hInstance = hdl
#  wc.lpszClassName = className
#  wc.style = win32con.CS_VREDRAW | win32con.CS_HREDRAW
#  wc.hbrBackground = win32con.COLOR_WINDOW + 1
#  this_app=win32api.GetModuleHandle(None)
#  #wc.hIcon = win32gui.LoadIcon(this_app, 1)
#  wc.hIcon = win32gui.LoadImage(hdl, img, win32con.IMAGE_ICON, 0, 0, icon_flags)
load()