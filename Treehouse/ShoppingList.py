itemList = []

def show_help():
	print("What to shop today ?")
	print("Enter SHOW to see current added items in your list")
	print("Enter HELP to see the list of commands")
	print("Enter DONE to stop adding items")

def show_list():
	print("Here is your list:")
	for item in itemList:
		print(item)

def items_added(items):
	itemList.append(items)
	print("Added {}. List now has {} items".format(items,len(itemList)))

show_help()

while True:
	items = str(raw_input("> "))
	if items == "DONE":
		break
	elif items == "SHOW":
		show_list()
		continue
	elif items == "HELP":
		show_help()
		continue
	else:
		items_added(items)

show_list()


