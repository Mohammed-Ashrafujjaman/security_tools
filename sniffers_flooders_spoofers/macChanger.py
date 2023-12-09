#!/usr/bin/python3

import subprocess

def changeMacAddr(interface,mac):
	try:
		subprocess.call(['ifconfig',interface,'down'])
		subprocess.call(['ifconfig',interface,'hw','ether',mac])
		subprocess.call(['ifconfig',interface,'up'])
		return True
	except:
		return False


def main():
	# new_mac = "CH:AR:LI:EG:HO:ST"
	interface = input("[*] interface you want to change mac address: ")
	new_mac = input("[*] input new mac address: ")

	if interface == None:
		print("no interface is given.")
		exit() 
	if new_mac == None:
		print("no mac address is given.")
		exit()

	# befor_mac = subprocess.check_output(['ifconfig',interface])
	rslt = changeMacAddr(interface,new_mac)
	# after_mac = subprocess.check_output(['ifconfig',interface])
	if rslt:
		print("[+] Mac Address changed successfully.")
	else:
		print("[-] Mac Address could not change.")



if __name__ == '__main__':
	main()

# Limitation:
# 1. Some mac address may not be assigned.[example: 77:66:55:44:33:22]
# but it still show mac change though mac actually did not change.
# 2. There are much simpler way such as [ macchanger -r wlan0] -> will assign random mac to wlan0