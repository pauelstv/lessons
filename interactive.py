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

#вывод числа с плавающей точкой, 2 знака, float
total = 2.288
print("FLOAT VALUE PRINT:", "%.2f" % total)
#строковые методы
parrot = "KeekKeeeKEEKEe AAZAZAZAa"
print("Lower:", parrot.lower())
print("Upper:", parrot.upper())
print("Lower:", str.lower(parrot))
print("Upper:", str.upper(parrot))
print("Count length:", len(parrot))

callback = "azaza"
answ = "kekeke"
print (('%s huypesda %s') % (callback, answ) )
print("Press any key to exit...")
kek=input()


