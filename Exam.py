def products(amount,dict):
	
	# return array of items user can buy that stores inside this and return
	items = []

	for i,j in dict.items():
	
		if amount>j:
			items.append(i)
	
	return items

def supplier(inventory):
	
	reset = int(input('Want to reset count ? Press 1 or Press 9 to Go back'))
	
	if reset == 1:
		inventory['Coke'] = 10
		inventory['Pepsi'] = 10
		inventory['Soda'] = 10
	return

def purchaser(amount,dict,inventory):
	# calls funtion which returns items array
	items = products(amount,dict)

	# if function call return []
	# no items can user buy
	if len(items)==0:
		print('You dont have enough money to buy anything')

	else:
		print('Select From follow given Options')

		# print all the given Options
		for j,i in enumerate(items):
			print(j+1,':',i)

		selection = int(input('Select Items you want to buy or Press 9 for Revoke'))

		if selection == 9:
			items = []
			return
		
		print(f'You have selected {items[selection-1]} and price for that is {dict[items[selection-1]]}')
		print(f'You get change about {amount-dict[items[selection-1]]}')
		
		# reduce item from inventory
		inventory[items[selection-1]] -= 1

		print(f'current inventory count for {items[selection-1]} is {inventory[items[selection-1]]}')


if __name__ == '__main__':
	# Dictnory for the Items as well as inverntory count

	dict = {'Coke':25,'Pepsi':35,'Soda':45}
	inventory = {'Coke':10,'Pepsi':10,'Soda':10}

	# Infinte loop
	while True:
		
		# Ask for user Input to select from purchaser or Supplier
		selectOption = int(input('1.Purchaser or 2.Supplier'))
		
		# Work accordingly based on the User Input
		if selectOption == 2:
			print('You are the supplier')
			supplier(inventory)
		else:
			amount = int(input("Enter amount"))
			purchaser(amount,dict,inventory)
