import random

number = random.randint(1,10)
guessed_number = 0
count = []

def game():
	while len(count) < 5:	
		try:
			guessed_number = int(raw_input("Guess a number :"))
		except ValueError:
			print("Enter a integer")
		else:
			if(guessed_number == number):
				print("HIT. Your number was {}".format(number))
				break
			elif(guessed_number > number):
				print("Your number {} is too high".format(guessed_number))
			elif(guessed_number < number):
				print("Your number {} is too low".format(guessed_number))
			else:
				print("MISS")
		count.append(guessed_number)

	else:
		print("You didnt get it !!")
	play_again = raw_input("Do you want to play again ? Y/n")
	if play_again.lower() != "n":
		game()
	else:
		print("Bye. See you again !!")

game()
	