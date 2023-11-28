#! /usr/bin/python3

import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.31.144'
port = 2003

def portscanner(port):
	if sock.connect_ex((host,port)):
		print(f"port {port} is closed")
	else:
		print(f"port {port} is open")

portscanner(port)

# problem with this code is: 
# 1. port should be given other wise no use
# 2. filtered port or firewall may make this program stack in "line 11"
# 3. every thing is static so user cannot use there own ip and port while running 