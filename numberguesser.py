import random

while True:
	print("Welcome to number guesser.")
	print("Press 1 to play and 2 to quit")
	choice = raw_input("What would you like to do?") #input to see if quit
	if choice == "2":
		break
	elif choice == "1":
		minimum = int(input("What's the mimimum value?"))
		maximum = int(input("What's the maximum value?"))
		r = random.randint(minimum, maximum) #generates a random number
		while True: #start guessing the number
			userChoice = int(input("Guess a number:"))
			if userChoice == r:
				print("Yay! You guessed it!")
				break
			elif userChoice < r:
				print("Too low")
			elif userChoice > r:
				print("Too high")
			else:
				print("Not an option")
	else: 
		print("not an option, silly.")       	