# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 09:57:14 2021

@author: IT LAB
"""
#Python program for 'Guess the Number Game'
import random
number = random.randint(1, 20)) #generating a number within the range 1 to 20

player_name = input("Hello, What's your name?")#getting the user name
number_of_guesses = 0
print('okay! '+ player_name+ ' I am Guessing a number between 1 and 20:')

while number_of_guesses<6: #number of guesses = 6
    guess = int(input())#getting the guessed number from the user
    number_of_guesses += 1
    #executes when the user guessed the correct number
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
    
#executes when the user crosses the guess limit of 6
else:
    print('You did not guess the number, The number was ' + str(number))
