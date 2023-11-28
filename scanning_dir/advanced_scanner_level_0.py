#!/usr/bin/python3

from socket import *
import optparse # will convert it to "argparse" 
from threading import *
from termcolor import colored

def connScan(tgtHost,tgtPort):
	try:
		sock = socket(AF_INET,SOCK_STREAM)
		sock.settimeout(2)
		sock.connect((tgtHost,tgtPort))
		print(colored(f"[+] {tgtPort} tcp Open",'green'))
	except:
		print(colored(f"[-] {tgtPort} tcp Close",'red'))
	finally:
		sock.close()

def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print(colored(f"[-] Unknown host: {tgtHost}",'red'))
	try:
		tgtName = gethostbyaddr(tgtIP)
		print(colored(f"[+] Scan Results for: {tgtName[2]}",'green'))
	except:
		print(f"[+] Scan Results for: {tgtHost}")
	# settimeout(1)
	for tgtPort in tgtPorts:
		thrd = Thread(target=connScan, args = (tgtHost, int(tgtPort)))
		thrd.start()

def main():
	parser = optparse.OptionParser('usage of program: ' +'-H <target host> -p <target port>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports seperated by comma')
	(options,args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	if 	tgtHost == None or tgtPorts[0] == 'None':
		print(parser.usage)
		exit(0)
	portScan(tgtHost,tgtPorts)

if __name__ == "__main__":
	main()

# limitation:
# 1. can only scan port (straight forward)
# 2. unable to distinguish filtered and closed port (shows close for filterd port)
# 3. can scan multiple port but not range of port rather specific port given by user