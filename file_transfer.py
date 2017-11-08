#!/usr/bin/env python

from __future__ import print_function
import paramiko
#import os
import getpass

pswd = getpass.getpass('please enter password: ')
 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.1.48',username='admin',password=pswd)
sftp = ssh.open_sftp()
#sftp.chdir('/var/tmp')
#pri.t(sftp.listdir()t
sftp.get('/var/tmp/krt_gencfg_filter.txt','/home/hammad/Juniper_PYEZ/krt_gencfg_filter.txt')
sftp.close()
ssh.close()


