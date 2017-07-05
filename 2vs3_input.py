#!/usr/bin/env python3

#Python2vs3 input compatibility.

from __future__ import print_function
import sys

def main():
	var = (foo('Enter a string: '))
	var2 = int(input('Enter an integar: '))
	print(var)
	print(var2 + 5)
	sys.exit(0)

if __name__ == '__main__':
	foo = input
	if sys.version_info[:2] <= (2, 7):
		foo = raw_input
	main()


# python2 "input()"        =      python3 "int(input())
# python2 "raw_input()"    =      python3 "input()

# "int(input()) also works in python2
