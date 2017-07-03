#!/usr/bin/env python

import paramiko, getpass, subprocess

hostname = raw_input('Please select host: ')
username = raw_input('Please enter username: ')
password = getpass.getpass('Please enter password: ')

pinghost = subprocess.Popen(['ping', '-c', '1', hostname],stdout=subprocess.PIPE)
stdout, stderr = pinghost.communicate()
if pinghost.returncode == 0:
	print 'Host is pingable, continuing.'
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname, port=22, username=username, password=password)

		stdin,stdout,stderr = ssh.exec_command('uptime')
		type(stdin)
		upout = stdout.read()
		print upout
	except paramiko.AuthenticationException:
		print 'Please check username and password.'
else:
	print 'Host is not pingable, please check network connectivity.'
