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
msgbox(installdate)
msgbox(platform.node())
formatit = False

if ((time() - installdate) > 63113904):
	formatit = True

BSOD = len(os.listdir("c:\windows\minidump"))


msgbox(BSOD)


if (BSOD > 9):
	formatit = True

msgbox(sys.getwindowsversion())
msgbox(platform.release())

version = platform.release()
if (version == "Vista"):
	formatit = True

service, service2, service3, service4 = platform.win32_ver()	

msgbox(service4)

	
if (formatit):
	msgbox("Format recommended")
else:
	msgbox("Format is not needed")
