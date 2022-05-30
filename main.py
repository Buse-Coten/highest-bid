from replit import clear

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest:
      highest = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of {highest}$")
    


while not bidding_finished:
  name = input("What's your name?")
  price = int(input("What's your bid? $"))
  bids[name] = price
  should_continue = input("Are there any bidders? Type 'yes' or 'no'\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()

