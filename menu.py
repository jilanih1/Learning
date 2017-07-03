#!/usr/bin/env python
# Menu using while loop

var = 'select option # '
foo = 'you have selected option #:'
stat1 = 'Invalid selection. Please try again.'
stat2 = 'Please select an option [1-4]: '

def menu():
	print('-' * 10 + 'choices' + '-' * 10)
	print('1: ' + var + '1')
	print('2: ' + var + '2')
	print('3: ' + var + '3')
	print('4: exit')
	print('-' * 27)

while True:
	menu()
	try:
		choice = input(stat2)
		if choice>0 and choice<4:
			print foo, choice
		elif choice<=0 or choice>4:
			print stat1
		elif choice==4:
			print 'exiting...'
			break
	except (NameError, SyntaxError):
		print stat1
