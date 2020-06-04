import ctypes
# Constants from the Windows API
STD_OUTPUT_HANDLE = -11

FOREGROUND_RED    = 0x0047 # text color contains red.

def get_csbi_attributes(handle):
	# Based on IPython's winconsole.py, written by Alexander Belchenko  
	import struct 
	csbi = ctypes.create_string_buffer(22)
	res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
	assert res
	
	(bufx, bufy, curx, cury, wattr,left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
	return wattr
	
handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
reset = get_csbi_attributes(handle)

ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_RED)

print "Cherry on top" 

ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset) 