# Updated version of network_scanner_level_2
# we will scan multiple port at once

#! /usr/bin/python3

import socket 
from termcolor import colored
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2) # set scanning time to 2 sec so that program does not stuck

print("This will take IP and Port number to scan.\nGiven port will consider the last port number.\nIt will scan all port 1 to the given_port number.")
host = input('[*] Enter the host to scan(ip address): ')
port = int(input("[*] Enter the last port( 1 to 65535 ) : "))

def portscanner(port):
	if sock.connect_ex((host,port)):
		print(colored(f"port {port} is closed",'red'))
	else:
		print(colored(f"port {port} is open",'green'))

for x in range(1, port+1):
	portscanner(x)
sock.close()

# problem with this code:
# 1. this code only scan if port is opened or closed
# 2. even filtered port is given as closed 
# 3. for more port result screen will overwhelm with results