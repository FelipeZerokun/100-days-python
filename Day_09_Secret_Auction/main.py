# 100 days of coding - Python
# Day 9: Secret Auction
# By Felipe Rojas
# Learning how to define and use functions with fixed arguments.


import art
import os
clear = lambda: os.system('cls')

#HINT: You can call clear() to clear the output in the console.
    
print(art.logo)
print("Secret Auction program, by Felipe Rojas")


bidders = []
auction_end = False

def new_entry(name, bid):
  new_bidder = {}
  new_bidder["name"] = name
  new_bidder["bid"] = bid
  bidders.append(new_bidder)

while not auction_end:
  bidder_name = input("Enter your name: ")
  bid_quantity = int(input("Enter your bid: $"))
  new_entry(bidder_name, bid_quantity)
  continue_auction = input("Is there another person? (Yes or No): ").lower()
  
  if continue_auction == "no":
    auction_end = True

  elif continue_auction == "yes":
    clear()

top_bid = 0
top_bidder = ""
for person in bidders:
  if person["bid"] > top_bid:
    top_bidder = person["name"]
    top_bid = person["bid"]


print(f"{top_bidder} wins the bid with ${top_bid}")