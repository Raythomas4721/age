driving = input('Have you driven a car ?')
if driving != 'Yes' and driving != 'No':
	print("Only can enter Yes or No")
	raise SystemExit

age = input('How old are you ?')
age = int(age)
if driving == 'Yes':
	if age >= 18:
		print('You are good')
	else:
		print('You should not do that')
elif driving == 'No':
	if age >= 18:
		print('It is time to get your driver license')
	else:
		print('You will be able to get your driver license in a few years' ) 