# Number Guessing (User)
import random as rd
comp_number = rd.randint(1,1000)
#print(comp_number)
done = False
turns = 0
while not done:
    user_number = int(input())
    if user_number < comp_number:
        print("Sorry, ur number is too low. Please guess again!")
        turns = turns + 1
        done = False
    elif user_number > comp_number:
        print("sorry, ur number is too high. Please guess again!")
        turns = turns + 1
        done = False
    elif user_number == comp_number:
        print(f"Hey User u have guessed it correctly in {turns} iterations and the secret number is {comp_number}")
        done = True
