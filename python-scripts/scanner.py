#!/bin/python3

import sys
import socket
from datetime import datetime

# Functions definition
def print_banner(target):
	print("-" * 50)
	print("Scanning target "+target)
	print("Time started: "+str(datetime.now()))
	print("-" * 50)

# Define our target
target = ""

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # Translate hostname to ipv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip|hostname>")
	sys.exit()

# Add a pretty banner
print_banner(target)

try:

	for port in range(1,100):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.1)
		result = s.connect_ex((target,port)) # returns an error indicator 0 - open, 1 - closed
#		print("Checking port {}...".format(port))		
		if result == 0:
			print("The port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
