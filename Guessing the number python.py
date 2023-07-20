'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import random
import math

def guess_number():
    random_number = random.randint(1,1000)
    x = random_number
    player_name=input("enter ur name:")
    confirm_play=input("would u like to start the game?(enter yes or no):")
    attempts=0 
    while confirm_play.lower()== "yes":
        guess = int(input("Guess a number:- "))
        if guess < 1 or guess > 1000:
            print("please guess any number in the range.")
        elif x == guess:
            print("\n\nCongratulations ",player_name,"you won!")
            print("it took you",attempts,"attempts to win this game")
            break
        attempts+=1 
        if x %2==0:
            print("the number is divisble by 2")
        if x %3==0:
            print("the number is divisble by 3")
        if x %4==0:
            print("the number is divisble by 4")
        if x %5==0:
            print("the number is divisble by 5")
        if x %6==0:
            print("the number is divisble by 6")
        if x %7==0:
            print("the number is divisble by 7")
        if x %9==0:
            print("the number is divisble by 9")
        if x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You Guessed too high!")
    
    else:
        print("thanks",player_name,"for your time.")
        
guess_number()
