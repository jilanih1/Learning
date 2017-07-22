#!/usr/bin/env python
#Script testing out Netmiko Library
#Netmiko Link: https://pynet.twb-tech.com/blog/automation/netmiko.html

#Tested in Arista vEOS (Pulls running-config from device)

from __future__ import print_function
from netmiko import ConnectHandler
import sys, getpass
if sys.version_info[:2] <= (2, 7):
	input = raw_input

if __name__ == '__main__':

	host = input('Please enter IP address: ')
	user = input('Please enter username: ')
	pswd = getpass.getpass('Please enter password: ')

	#Dictionary with device information:
	device = {
		'device_type': 'arista_eos',
		'ip': host,
		'username': user,
		'password': pswd,
		'port': 22,
	}

	#ConnectHandler with and without a dictionary:
	net_connect = ConnectHandler(**device)
	#net_connect = ConnectHandler(device_type='arista_eos', ip=host, username=user, password=pswd, port=22)

	#Enters enable mode:
	net_connect.enable()
	#Output from show commands:
	output1 = net_connect.send_command_expect('show running-config')
	output2 = net_connect.send_command_expect('show running-config diffs')[:-1] 

	print('\033[91m' + '*' * 50 + '\n' + 'Running-config from ' + host + ':' + '\n' + '*' * 50 + '\033[0m')
	print(output1)
	print('\033[91m' + '*' * 50 + '\n' + 'Differences from startup-config:' + '\n' + '*' * 50 + '\033[0m')
	print(output2)
	print('\033[91m' + '*' * 50 + '\033[0m')

	#Terminates SSH session:
	net_connect.disconnect()

sys.exit(1)
