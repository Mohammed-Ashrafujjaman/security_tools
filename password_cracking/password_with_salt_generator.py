#!/usr/bin/python3

# this library is deprecated!
import crypt

def salted_with_crypt(passwd, salt):
	c_s_pass = crypt.crypt(passwd,salt)
	print(f"Salted password with crypt library.")
	print(f"password: {c_s_pass}")


def main():
	passwd = input("[*] Enter a password: ")
	salt = input("[*] Enter salt (only 2 characters): ")

	salted_with_crypt(passwd,salt)


if __name__ == '__main__':
	main()