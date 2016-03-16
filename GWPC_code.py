import GWPC

def chooseFitnessExp(numberOfExps):
	choice = 0
	while choice < 1 or choice > numberOfExps: 
		if choice != '1' and choice != '2' and choice != '3' and choice != '4'  and choice != '5' and choice != '6' and choice != '7':
			choice = 0
	if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6' or choice == '7':
		choice = int(choice)
	print()
	return choice

