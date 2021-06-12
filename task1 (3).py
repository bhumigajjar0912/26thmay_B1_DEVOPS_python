import datetime
import psutil as p
import platform
import os
from getmac import get_mac_address
import subprocess

description = '''
Press 1 to Check current time and Date :- 
Press 2 to Check RAM Size of Your current OS  :- 
Press 3 to KNow Name of YOur current OS :- 
Press 4 to Check What is MAc Address of YOur lapTOP/PC/VM/CLoudVM :- 
Press 5 to create one directory IN your Desktop :- 
Press 6 to Restart Your current OS :- 
Press 7 to Print list of all available Wifi in your laptop Range :-
Press 8 to RUn another code in Your current folder  :-  
'''

def size(byte):
  #this the function to convert bytes into more suitable reading format.

  #Suffixes for the size
  for x in ["B","KB","MB","GB","TB"]:
    if byte<1024:
      return f"{byte:.2f}{x}"
    byte=byte/1024
    
def memory():
  #Getting the Memory/Ram Data.
  mem = p.virtual_memory()
  print("Total Memory:    ",size(mem.total))
  print("Available Memory:", size(mem.available))
  print("Used Memory:     ", size(mem.used))
  print("Percentage:      ",mem.percent,"% \n")


user_input = eval(input('Enter number between 1 to 8:'))
if user_input==1:
    now = datetime.datetime.now()
    print ("Current date and time : {}".format(now.strftime("%Y-%m-%d %H:%M:%S")))
elif user_input==2:
    memory()
elif user_input==3:
    print(platform.system())
elif user_input==4:
    mac = get_mac_address()
    print(mac.upper())
elif user_input==5:
    path = os.path.join("C:/Users/acer/Desktop/", "NewFolder")
    os.mkdir(path)
    print("Directory '% s' created" % "NewFolder")
elif user_input==6:
    os.system("shutdown /r /t 1")
elif user_input==7:
    devices = subprocess.check_output(['netsh','wlan','show','network'])
    devices = devices.decode('ascii')
    devices= devices.replace("\r","")
    print(devices)
elif user_input==8:
    os.system('task1.py')


