# This is a little bit updated version of 1st program
# we will take ip and port from user

#! /usr/bin/python3

import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2) # set scanning time to 2 sec so that program does not stuck

host = input('[*] Enter the host to scan(ip address): ')
port = int(input('[*] Enter the host port to scan: '))

def portscanner(port):
	if sock.connect_ex((host,port)):
		print(f"port {port} is closed")
	else:
		print(f"port {port} is open")

portscanner(port)
sock.close()

# problem with this code is:
# 1. filtered port shows closed
# 2. only scan one port at a time (unable to scan multiple port)
# 3. still very basic 
