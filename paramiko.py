#!/usr/bin/env python

import paramiko, sys, getpass

hostname = raw_input('Please select host: ')
username = raw_input('Please enter username: ')
password = getpass.getpass('Please enter password: ')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, port=22, username=username, password=password)

stdin,stdout,stderr = ssh.exec_command('uptime')
type(stdin)
upout = stdout.read()
print upout
