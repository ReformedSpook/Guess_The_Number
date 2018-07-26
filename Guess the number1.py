#Guess the number game.
 
import random

print("Welcome To Guess The Number!")

name = input("Enter your name: ")
while True:
  
    if name.isalpha():
        break
    else:
        print("invalid input")
        name = input("Please enter a valid name: ")

restart = 'y'
while restart == 'y':
    guesses = 6
    guesses_taken = 0
    number = random.randint(1, 20)
   
    print("Well " + name.title() + " Im thinking of a number between 1 and 20")
   
    while guesses > 0:

        guess = input("Take a guess: ")

        while True:
  
            if guess.isdigit():
                break
            else:
                print("invalid input")
                guess = input("Please enter a valid number: ")

        guess = int(guess)             
        guesses -= 1    
        guesses_taken += 1
        if guess > 20 or guess < 1 :
            print("Please a choose a number between 1 and 20")
        elif guess > number:
            print("Your guess was too high, you have", guesses, "remaining")    
        elif guess < number:
            print("Your guess was too low , you have", guesses, "remaining")        
        else:
            print("No way", name, "xD! You guessed the right number in", guesses_taken, "guesses !!")
            break
           
    if guess != number:
        print("Feels Bad :( , You didn't guess the number. The number was", number)
   
    while True:

        restart = input("Run again? (y/n): ")
        if restart != 'y' and restart != 'n':
            print('invalid input.')
        else:
            break