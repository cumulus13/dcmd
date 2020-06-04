#!c:/SDK/Anaconda2/python.exe
import sys
import os

def supports_color():
	plat = sys.platform
	supported_platform = plat != 'Pocket PC' and (plat != 'win32' or 'ANSICON' in os.environ)
	# isatty is not always implemented, #6223.  
	is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
	return supported_platform and is_a_tty

supports_color()
	
#print supports_color()

#from make_colors import make_colors

#print make_colors("TEST", 'lw', 'lr')