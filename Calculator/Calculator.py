import re


def perform_math():
	global run
	global previous

	if previous == '':
		equation = input('Enter equation: ')
	else:
		equation = input(str(previous))

	if equation == 'quit':
		print('Closing Calculator')
		run = False
		return

	equation = re.sub('[a-zA-Z,:" "]', '', str(previous)+equation)
	previous = eval(equation)


print('Running Calculator')
print("Type 'quit' to exit the app\n")

previous = ''

run = True
while run:
	perform_math()

