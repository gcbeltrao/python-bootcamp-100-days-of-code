from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_cards = []
player_cards = []

def sum_dealer():
    sum_dealer_cards = 0
    for card in dealer_cards:
        sum_dealer_cards += card
    return sum_dealer_cards

def sum_player():
    sum_player_cards = 0
    for card in player_cards:
        sum_player_cards += card
    return sum_player_cards

def draw_card(a):
    for _ in range(a):
        dealer_cards.append(random.choice(cards))
        player_cards.append(random.choice(cards))

def draw_card_player():
    player_cards.append(random.choice(cards))
    print(f"Your cards: {player_cards}, current score: {sum_player()}")
    print(f"Computer first card: {dealer_cards[0]}")

def draw_card_dealer():
    dealer_cards.append(random.choice(cards))

def start_game():
    print(logo)
    dealer_cards.clear()
    player_cards.clear()
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        draw_card(2)
        print(f"Your cards: {player_cards}, current score: {sum_player()}")
        print(f"Computer first card: {dealer_cards[0]}")
        continue_game(True)
    else:
        continue_game(False)

def continue_game(game_on):
    while game_on:
        want_draw = input("Type 'y' to get another card, type 'n' to pass: ")
        if want_draw == "y":
            draw_card_player()
            if sum_player() > 21:
                print(f"Your final hand: {player_cards}, final score: {sum_player()} ")
                print(f"Computer final hand: {dealer_cards}, final score: {sum_dealer()} ")
                print("You went over. You lose :(")
                game_on = False
        elif want_draw == "n":
            if sum_player() > sum_dealer():
                print(f"Your final hand: {player_cards}, final score: {sum_player()} ")
                print(f"Computer final hand: {dealer_cards}, final score: {sum_dealer()} ")
                print("You win :)")
                game_on = False
            elif sum_dealer() > sum_player():
                print(f"Your final hand: {player_cards}, final score: {sum_player()} ")
                print(f"Computer final hand: {dealer_cards}, final score: {sum_dealer()} ")
                print("You lose :(")
                game_on = False
    start_game()

start_game()