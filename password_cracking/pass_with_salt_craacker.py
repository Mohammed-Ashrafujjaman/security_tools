#!/usr/bin/python3

# will finish this latter as crypt library depricated!
import crypt 

def crackSaltedPass(cryptPass):
	salt = cryptPass[:2]
	wordlist = open('wordlist.txt','r') # treating as default wordlist in the same directory
	for word in wordlist.readlines():
		word = word.strip('\n')
		cryptWord = crypt.crypt(word,salt)
		if cryptPass == cryptWord:
			print(f"password found: {word}")
			print(f"salt: {salt}")
			exit()

def main():
	# wordlist = input("input wordlist with path: ")
	userlist = input("input userlist: ")

	file = open(userlist,'r')

	for line in file.readlines():
		if ':' in line:
			line = line.strip('\n')
			cryptPass = line.split(':')[1]
			rslt = crackSaltedPass(cryptPass)
	print("password not in the wordlist")


if __name__ == '__main__':
	main()