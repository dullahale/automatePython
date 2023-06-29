from art import logo as logo
import clear as clear
# The major lesson of this exercise is to improve looping through a dictionary.
print(logo)

new_bidder = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("Please enter your name: ")
    bid_price = int(input("Please enter the price you'd like to bid: $"))

    new_bidder[name] = bid_price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(new_bidder)

    elif should_continue == 'yes':
        clear
