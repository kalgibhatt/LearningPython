import random

words = ['blue','red','orange','pink','black','white','purple','yellow','grey']

while True:
	game = input("Do you want to continue ? Y/n")
	if game.lower() == "n":
		break

	#pick a random word
	guessed_word = random.choice(words)
	bad_guess = []
	good_guess = []

	while len(bad_guess) > 7 and len(good_guess) != len(guessed_word):
		#draw spaces, guessed letter and spaces
		for letter in guessed_word:
			if letter in good_guess:
				print(letter, end='')
			else:
				print('_', end='')
		print('')
		print("Strikes : {} / 7".format(len(bad_guess)))
		print('')

	#take guess
	guess = raw_input("Guess a letter").lower()

	if(len(guess) != 1):
		print("You can only guess single letter")
		continue
	elif guess in good_guess or guess in bad_guess:
		print("You have already guessed this letter")
		continue
	elif not guess.isalpha():
		print("You can only guess letters")
		continue
	
	if guess in guessed_word:
		good_guess.append(guess)
		if(len(good_guess) == len(list(guessed_word))):
			print("You win. The word was {}".format(guessed_word))
			break
	else:
		bad_guess.append(guess)
else:
	print("You did not make it. The secret word was: {}".format(guessed_word))

