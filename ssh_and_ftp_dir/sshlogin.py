# Simple fixed ssh connection codes
# Can not process multiple user define command over ssh with this code
# good for specific task but not dynamic or robust 
#!/usr/bin/python3

import pexpect
import argparse

PROMPT = ['# ','>>> ','> ','\$ ']

def send_command(child,command):
	child.sendline(command)
	child.expect(PROMPT)
	print(child.before)


def ssh_connect(user,pswd,ip):
	# print(f"user: {user}\npassword: {pswd}\nhost: {ip}")
	connStr = 'ssh '+'-oHostkeyAlgorithms=+ssh-rsa '+user+'@'+ip 
	child = pexpect.spawn(connStr)
	ret = child.expect([pexpect.TIMEOUT,"Are you sure you want to continue connecting?"])
	if ret == 0:
		print("[-] Error Connecting")
		return -1
	if ret == 1:
		child.sendline("yes")
		ret = child.expect([pexpect.TIMEOUT,"* [p|P]assword:"])
		if ret == 0:
			print("[-] Connction failed!")
			return -1
	child.sendline(pswd)
	child.expect(PROMPT)
	return child

def ssh_connect_direct(user,pswd,ip):
	connStr = 'ssh '+'-oHostkeyAlgorithms=+ssh-rsa '+user+'@'+ip 
	child = pexpect.spawn(connStr)
	ret = child.expect([pexpect.TIMEOUT,"password:"])
	if ret == 0:
		print("[-] Connction failed!")
		return -1
	child.sendline(pswd)
	child.expect(PROMPT)
	return child


def main():
	parser = argparse.ArgumentParser(description="This is simple ssh login code")
	parser.add_argument('-i','--IP-ADDR',dest='tgtIP',metavar="<ip address>",help='target IP address')
	parser.add_argument('-u','--USER',dest='tgtUser',metavar="<user>",help='user to access')
	parser.add_argument('-p','--PASSWORD',dest='tgtPass',metavar="<password>",help='password')

	args = parser.parse_args()

	if args.tgtUser == None or args.tgtIP == None or args.tgtPass == None:
		print(parser.print_help())
		exit(0)

	try:
		child = ssh_connect(args.tgtUser,args.tgtPass,args.tgtIP)
		if child == -1:
			print("Didn't ask confirmation!\nApplying direct aproch....")
			child = ssh_connect_direct(args.tgtUser,args.tgtPass,args.tgtIP)
			# while True:
				# command = input("you: ")
			send_command(child,"ps")
			send_command(child,"cat /etc/passwd")
				# if command == 'exit':
					# break
		else:
			print("[+] connection established [+]")
			# while True:
			send_command(child,"ps")
			send_command(child,"cat /etc/passwd")
				# if command == 'exit':
					# break
	except:
		print("[-] connection error!")


if __name__ == '__main__':
	main()