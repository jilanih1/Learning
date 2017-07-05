#!/usr/bin/env python

import paramiko, getpass, subprocess

hostname = raw_input('Please enter hostname: ')
username = raw_input('Please enter username: ')
password = getpass.getpass(username + '@' + hostname + ' password: ')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

pinghost = subprocess.Popen(['ping', '-c', '1', hostname],stdout=subprocess.PIPE)
stdout, stderr = pinghost.communicate()
if pinghost.returncode == 0:
	print 'Host is pingable, continuing...'
	try:
		command = raw_input('please enter a Linux command: ')
		ssh.connect(hostname, port=22, username=username, password=password)
		stdin,stdout,stderr = ssh.exec_command(command)
		type(stdin)
		print command
		print stdout.read()

	except paramiko.AuthenticationException:
		print 'Authentication Failed: Please check username and password.'
	except paramiko.ssh_exception.NoValidConnectionsError:
		print 'Connection Refused: Unable to connect to port 22 on ' + hostname
else:
	print 'Host is not pingable, please check network connectivity.'
