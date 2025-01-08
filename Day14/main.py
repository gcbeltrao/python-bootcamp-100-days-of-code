import art
from game_data import data
import random

def get_random_person():
    return random.choice(data)


def data_person(person):
    name = person["name"]
    description = person["description"]
    country = person["country"]
    return f"{name}, a {description}, from {country}"


def followers(person):
    return person["follower_count"]


def game():
    score = 0
    print(art.logo)
    celebrity1 = get_random_person()
    celebrity2 = get_random_person()
    game_on = True
    while game_on:
        celebrity1 = celebrity2
        celebrity2 = get_random_person()

        while celebrity1 == celebrity2:
            celebrity2 = get_random_person()

        print(f"Compare A: {data_person(celebrity1)}")
        print(art.vs)
        print(f"Compare B: {data_person(celebrity2)}")
        guess = input("Who has more followers? Type 'A' or 'B':    ").upper()
        if guess == "A" or guess == "B":
            if guess == "A":
                person1 = celebrity1
                person2 = celebrity2
            elif guess == "B":
                person1 = celebrity2
                person2 = celebrity1

            if followers(person1) > followers(person2):
                score += 1
                print(art.logo)
                print(f"You're right! Current score: {score}")
            else:
                print(f"Sorry, that is wrong. Final score: {score}")
                game_on = False
        else:
            game_on = False
            print("Try again.")

game()
