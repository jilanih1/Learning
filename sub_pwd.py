#!/usr/bin/env python

from __future__ import print_function
import subprocess

proc = subprocess.Popen('pwd', stdout=subprocess.PIPE)
pwd = proc.stdout.read()
print(type(pwd))
print(pwd)
