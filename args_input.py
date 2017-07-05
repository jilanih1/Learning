#!/usr/bin/env python

#Example: how to input a string if an option is not selected initially.

import argparse

parser = argparse.ArgumentParser(usage='args_input.py -s <string>')
parser.add_argument('-s', '--string', help='type a string to be printed.')
args = parser.parse_args()

if not args.string:
	var = raw_input('no string entered, please enter string to be printed: ')
else:
	var = args.string

print var
