bids ={}
auction_members = True

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of Rs {highest_bid}")

while auction_members:
  name = input("Enter the name of the bidder: ")
  price = int(input("Enter the bidding amount: RS. "))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no' : ").lower()
  if should_continue == "no":
    auction_members = False
    find_highest_bidder(bids)
  # elif should_continue == "yes":
    # clear()