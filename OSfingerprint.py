#!/usr/bin/python
import os, sys, logging

# turn off scapy warnings
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

# import Scapy libs
from scapy.all import IP, TCP, sr1

# return name for OS based on TCP window size and TTL
def OSbyWindowSize(window_size, ttl):
	return {
		"4128" : lambda ttl:
			"iOS 12.4 (Cisco Router)",
		"5720" : lambda ttl:
			"Google Linux",
		"5840" : lambda ttl:
			"Linux 2.4",
		"8192" : lambda ttl:
			"Windows 7",
		"16384": lambda ttl:
			"Windows 2003" if int(ttl) > 64 else "OpenBSD",
		"65535": lambda ttl:
			"Windows XP" if int(ttl) > 64 else "FreeBSD",
	}.get(window_size, lambda ttl: "Unknown OS")(ttl)

# make sure root privilege
if not os.geteuid() == 0:
	sys.exit("Must have root privileges")

# check for command line args
if len(sys.argv) < 2:
	sys.exit("Usage: %s [hostname|IP]" % sys.argv[0])

# get IP address or hostname
target_ip = sys.argv[1]

# most commonly open ports
common_ports = [ 80, 22, 21, 135, 139, 143, 1723, 3389,\
				 25, 23, 53, 443, 110, 445, 8080, 4567 ]

# try each common port until one responds
for port in common_ports:
	# assemble IP packet with target IP
	ip = IP()
	ip.dst = target_ip

	# assemble TCP with dst port and SYN flag set
	tcp = TCP()
	tcp.dport = port
	tcp.flags = "S"

	print "Trying port %d..." % port

	# send the packet and wait 2 seconds for an answer
	rcv_pkt = sr1(ip/tcp, timeout = 2, verbose = 0)

	# if answered no need to try more ports
	if rcv_pkt:
		break

# check to see if host responded, quit if otherwise
if not rcv_pkt:
	sys.exit("No response from host.")

# extract the TCP window size from the received packet
window_size = rcv_pkt.sprintf("%TCP.window%")

# extract the IP TTL from the received packet
ttl = rcv_pkt.sprintf("%IP.ttl%")

# get OS name
os_name = OSbyWindowSize(window_size, ttl)

# display the result
print "OS is probably", os_name
