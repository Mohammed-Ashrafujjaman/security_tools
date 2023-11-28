#!/usr/bin/python3

from socket import *
import optparse # this is depricated so try "Argparse"
from threading import *
from termcolor import colored
import time

def connScan(tgtHost,tgtPort):
	try:
		sock = socket(AF_INET,SOCK_STREAM)
		sock.settimeout(2)
		sock.connect((tgtHost,tgtPort))
		print(colored(f"[+] {tgtPort} tcp Open",'green'))
		try:
			output = sock.recv(1024).decode('utf-8').strip('\n') # if port is open then it might send some data back
			print(colored(f"[++>] Port {tgtPort}: {output}",'blue'))
		except:
			print(colored(f"[-] No additional info for Port: {tgtPort}",'red'))
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
	thread_lists = []
	# start_time = time.perf_counter()
	for tgtPort in tgtPorts:
		thrd = Thread(target=connScan, args = (tgtHost, int(tgtPort)))
		thrd.start()
		thrd.join() # This line in not conventional as it nullify the reasoning of threads but it keeps the results together.
		# thread_lists.append(thrd)

	# for thread in thread_lists:
	# 	thread.join()
	# for tgtPort in tgtPorts:
	# 	connScan(tgtHost,tgtPort)

	# finished_time = time.perf_counter()
	# print(f"finished in {round(finished_time-start_time, 5)} second(s)")
		

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
