# Squawroot
# Checks integrity of Windows using WCU Student Computing standards as parameters
# 2014-03-24
# jwking@wcu.edu

from easygui import *
from subprocess import check_output
from _winreg import *
from time import *
import os, os.path
import platform
import sys

aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
aKey = OpenKey(aReg, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\")
test = QueryValueEx(aKey, "InstallDate")
installdate, trash = test
#msgbox(installdate)
#msgbox(platform.node())
formatit = False
reasons = "Reason/s "


if ((time() - installdate) > 63113904):
	formatit = True
	reasons = reasons + "| Install date "
	

if os.path.exists("c:\windows\minidump"):
	BSOD = len(os.listdir("c:\windows\minidump"))
else:
	BSOD = 0


#msgbox(BSOD)


if (BSOD > 9):
	formatit = True
	reasons = reasons + "| Too many BSODs "

#msgbox(sys.getwindowsversion())
#msgbox(platform.release())

version = platform.release()
if (version == "Vista"):
	formatit = True
	reasons = reasons + "| Because Vista "

service, service2, service3, service4 = platform.win32_ver()	

#msgbox(service4)

	
if (formatit):
	msgbox("Format recommended")
	msgbox(reasons)
else:
	msgbox("Format is not needed")