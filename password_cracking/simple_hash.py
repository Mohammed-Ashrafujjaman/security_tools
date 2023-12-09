#!/usr/bin/python3

import hashlib

def main():
	ot = input("type anything to produce hash value: ")

	hashtype1 = hashlib.md5()
	hashtype1.update(ot.encode())
	print(hashtype1.hexdigest())

	hashtype2 = hashlib.sha1()
	hashtype2.update(ot.encode())
	print(hashtype2.hexdigest())

	hashtype3 = hashlib.sha224()
	hashtype3.update(ot.encode())
	print(hashtype3.hexdigest())

	hashtype4 = hashlib.sha256()
	hashtype4.update(ot.encode())
	print(hashtype4.hexdigest())

	hashtype5 = hashlib.sha512()
	hashtype5.update(ot.encode())
	print(hashtype5.hexdigest())

	# hashtype6 = hashlib.md6()
	# hashtype6.update(ot.encode())
	# print(hashtype6.hexdigest())

if __name__ == '__main__':
	main()