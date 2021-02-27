#!/usr/bin/env python3
import random
number = random.randint(1,10)

print ("Welcome to the game - Guess the number!!")
player_name = input("Hello, please enter your name : ")
number_of_guesses  = 0
print ("Okay " + player_name + " You will have to guess the number between 1 and 10 :")

while number_of_guesses < 5:
	guess = int(input("Please guess the number : "))
	number_of_guesses += 1
	if guess < number :
		print ("Your guessed number is very low")

	if guess > number : 
		print ("Your guessed number is very high")
	if guess == number :
		break

if guess == number : 
	print ("You guessed the number in " + str(number_of_guesses) + " tries!!!")
else:
	print ("Sorry, you did not guess the correct number and your tries are "+str(number_of_guesses) + "The correct number is "+str(number))

