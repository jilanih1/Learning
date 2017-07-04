#!/usr/bin/env python
# Menu using while loop

from __future__ import print_function

foo = 'you have selected option #:'
stat = 'Invalid selection. Please try again.'

def menu():
	print(' ' * 12 + '_' * 7) 
	print('_' * 11 + '/' + 'CHOICES' + '\\' + '_' * 11)
	for x in range(1,4):
		print('%d: Select option #: %d' % (x,x))
	print('4: exit')
	print('_' * 31)

while True:
	menu()
	try:
		choice = input('Please select an option [1-4]: ')
		if choice>0 and choice<4:
			print(foo, choice)
		elif choice<=0 or choice>4:
			print(stat)
		elif choice==4:
			print('exiting...')
			break
	except (NameError, SyntaxError):
		print(stat)
