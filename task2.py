"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
import random








def title():
    print("input a number between 1 and 500\nyou have 10 trys\nif the number is close then guess higher or lower\nif its correct then you win\nno two playthroughs will be the same...")
def game():
    Num = random.randint(1,500)


    for i in range(1,11):
        guess= int(input("Enter a number: "))


        if guess > Num:
            print("too high")

        if guess < Num:
            print("too low")

        if guess == Num:
            print("Correct! thanks for playing!")
            break
    else:
        print(f"{Num} was the Correct number! thanks for playing!")





Ask = input("Have you played before? Y or N?: ")
for i in Ask:


    if Ask == "Y":
        game()
        
    if Ask == "N":
        title()
