import os

itemList = []

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")

def show_help():
	clear_screen()
	print("What to shop today ?")
	print("Enter SHOW to see current added items in your list")
	print("Enter HELP to see the list of commands")
	print("Enter DONE to stop adding items")
	print("Enter REMOVE to remive item from the list")

def show_list():
	clear_screen()
	index = 1
	print("Here is your list:")
	for items in itemList:
		print("{}.{}".format(index,items))
		index += 1
	print("-"*10)

def items_added(items):
	show_list()
	if len(itemList):
		position = raw_input("Where you want to add the item ? {}\nPress ENTER to add at the end of the list".format(items))
	else:
		position = 0
	try:
		position = abs(int(position))
	except ValueError:
		position = None

	if position is not None:
		itemList.insert(position-1,items)
	else:
		itemList.append(new_item)
	show_list()

def remove_from_list():
	show_list()
	what_to_remove = raw_input("What you want to remove from list ?")
	try:
		itemList.remove(what_to_remove)
	except ValueError:
		pass
	show_list()

show_help()

while True:
	new_item = str(raw_input("> "))
	if new_item.upper() == "DONE" or new_item.upper() == 'QUIT':
		break
	elif new_item.upper() == "SHOW":
		show_list()
		continue
	elif new_item.upper() == "HELP":
		show_help()
		continue
	elif new_item.upper() == "REMOVE":
		remove_from_list()
		continue
	elif new_item == "":
		print("Enter some item")
		continue
	else:
		items_added(new_item)

show_list()


