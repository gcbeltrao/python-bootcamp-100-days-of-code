from replit import clear
from art import logo

print(logo)

auction_running = True
Auction={}

def find_winner():
  for person in Auction:
    highest_bid = 0
    winner = ""
    if Auction[person] > highest_bid:
      highest_bid = Auction[person]
      winner = person
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while auction_running:
  name = input("What is your name?\n")
  bid = int(input("What is your bid? \n$"))
  
  Auction[name] = bid
    
  go_on = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if go_on == "no":
    auction_running = False
    find_winner()
  else:
    clear()
