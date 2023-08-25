import os, sys
from banners import device
from variables import numbers
os.system("clear")
print(device.sys_os)
print(device.janob_darknet)
device = input(">>> ")
if device == numbers.num1:
	os.system("cd userbot && python main.py")
elif device == numbers.num2:
	print("Hali tayyor emas !")
elif device == numbers.num3:
	os.system("python nicknameclock.py")
elif device == numbers.num4:
	print("Hali tayyor emas !")
elif device == numbers.num5:
	os.system("cd clock && python clock.py")
elif device == numbers.num6:
	print("Hali tayyor emas !")
elif device == numbers.num7:
	print("Hali tayyor emas !")
elif device == numbers.num0:
	os.system("exit")
	os.system("python main.py")

	