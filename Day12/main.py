from art import logo
import random

print(logo)

GAME_ON = True
attempts_10 = 10
attempts_5 = 5

print("Welcome to the Guessing Game!")
print("I am thinking of a number between 1 and 100.")

number = random.randint(1, 100)

print(f"Pssst, the correct answer is: {number}")

def set_dificulty():
    dificulty = input("Choose a dificulty. Type 'easy' or 'hard': ")
    if dificulty == "easy":
        print("You have 10 attempts remaining to guess the number.")
        return attempts_10
    else:
        print("You have 5 attempts remaining to guess the number.")
        return attempts_5

def make_guess():
    global GAME_ON
    attempts = set_dificulty() 
    while GAME_ON:
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            GAME_ON = False
        else:
            guess = int(input("Make a guess: "))
            if guess == number:
                print(f"You got it! The answer was {number}")
                GAME_ON = False
            elif guess < number:
                print("Too low.")
                attempts -= 1
                if attempts >= 1:
                    print(f"You have {attempts} attempts remaining to guess the number.")
            elif guess > number:
                print("Too high.")
                attempts -= 1
                if attempts >= 1:
                    print(f"You have {attempts} attempts remaining to guess the number.")

make_guess()
