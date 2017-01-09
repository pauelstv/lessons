import os
import platform
import sys

def getsysteminfo():
    print(os.getcwd())
    print(platform.processor())
    print(sys.platform)
    print(sys.getwindowsversion())
    print(os.getpid())
    print(os.getlogin())

getsysteminfo()


callback = "azaza"
answ = "kekeke"
print (('%s huypesda %s') % (callback, answ) )
print("Press any key to exit...")
kek=input()


