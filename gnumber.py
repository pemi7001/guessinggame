#"""
#Python Web Development Techdegree
#Project 1 - Number Guessing Game
#--------------------------------

#For this first project we will be using Workspaces. 

#NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

#"""

import random


def start_game():
    #"""Psuedo-code Hints
    
    #When the program starts, we want to:
    #------------------------------------
    #1. Display an intro/welcome message to the player.
      print("you guessed", trys,"times!")


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to the number guessing game!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")       
    #2. Store a random number as the answer/solution.
ans = random.randint(1,10)   
    #3. Continuously prompt the player for a guess.
guess = int(input("please guess a number between 1 and 10.    "))
trys = 1    
while ans != guess:


    
    #a. If the guess greater than the solution, display to the player "It's lower".
    if guess > ans:
        print("It's lower")
        guess = int(input("please guess a number between 1 and 10.    "))
        trys += 1 
    #b. If the guess is less than the solution, display to the player "It's higher".
    elif guess < ans:
        print("Its higher")
        guess = int(input("please guess a number between 1 and 10.    "))
        trys += 1 
    
    #4. Once the guess is correct, stop looping, inform the user they "Got it"
    elif guess == ans:
        print ("Got it!")
        

         #and show how many attempts it took them to get the correct number.
    #5. Let the player know the game is ending, or something that indicates the game is over.
        print("you guessed", trys, "times!")
        print("Game Over!")
        break
    #( You can add more features/enhancements if you'd like to. )
    #"""
    ## write your code inside this function.


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()

    
