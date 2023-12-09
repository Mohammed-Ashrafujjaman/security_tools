#!/usr/bin/python3

import hashlib
from urllib.request import urlopen

def crack_sha1(password_list,hash_value):
	for password in password_list.split('\n'):
		# print(f'{password}')
		hash_pass = hashlib.sha1(bytes(password,'utf-8')).hexdigest()
		if hash_value == hash_pass:
			print(f"[+] password matched! -> {password}")
			return True

	return False



def main():
	password_list = str(urlopen('https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/probable_wpa.txt').read(),'utf-8')
	print("1.Input raw password\n2.Input hash value")
	x = int(input("Choose: "))
	if x == 1:
		raw_pass = input("[+] input password: ")
		hash_v = hashlib.sha1(bytes(raw_pass,'utf-8')).hexdigest()
		print(f"{hash_v}")
		check = crack_sha1(password_list,hash_v)
		if check:
			print("Congo!")
		else:
			print("[-] Password not in the wordlists")
	else:
		raw_hash = input("[+] input hash: ")
		check = crack_sha1(password_list,raw_hash)
		if check:
			print("Congo!")
		else:
			print("[-] Password not in the wordlists")


	

if __name__ == '__main__':
	main()