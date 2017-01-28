itemList = []

print("What to shop today ?")
print("Enter SHOW to see current added items in your list")
print("Enter HELP to see the list of commands")
print("Enter DONE to stop adding items")

while(True):
	items = str(raw_input("> "))
	if(items == "DONE"):
		break
	elif(items == "SHOW"):
		for item in itemList:
			print(item)
	elif(items == "HELP"):
		print("Enter SHOW to see current added items in your list")
		print("Enter HELP to see the list of commands")
		print("Enter DONE to stop adding items")
	else:
		itemList.append(items)

print("Here is your list")
for item in itemList:
	print(item)


