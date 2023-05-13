#Create blind auction program.

#Import os to be able to call the command cls to clear the terminal
import os
#Create empty dictionary for the purpose of collecting bidder names and bid amounts as keys and values
bidderdict = {}

#define a function used to add keys and values to the dictionary
def bid():

    print("Welcome to the blind auction!")
    bidder_name = input("What's your name?\n")
    while True:
        try:
            bid_amount = int(input("What's your bid amount in dollars?\n"))
            break
        except ValueError:
            print("Please enter a number!")
    #Add to the dictionary. [key] = amount bid
    bidderdict[bidder_name] = bid_amount

#Call bid, ask if there are more keys to be added to the dictionary. If not, flip the morebidders flag to False to end the loop.       
while True:
    bid()
    print("Are there still other bidders? Type Y or N")
    add_bid = input("").lower()
    while add_bid != "y" and add_bid != "n":
        print("Please answer with Y or N.\n")
        add_bid = input("").lower()
    if add_bid == "y":
        os.system('cls')
    elif add_bid == "n":
        os.system('cls')
        break

#Set new vars to replace with names and bid amounts
current_highest_bid = 0
current_highest_bidder = ""

#For every bidder in the finished bidder list, check if the bid listed is higher than the current highest bid.
#If yes, replace the current highest bid. if no, ignore.
for bidder in bidderdict:
    currentbid = int(bidderdict[bidder])
    if currentbid > current_highest_bid:
        current_highest_bid = currentbid
        current_highest_bidder = bidder

#Finally, print f with the vars set in the previous for loop to ascertain the winner and the winning bid.
print(f"The winner is {current_highest_bidder} with a bid of ${current_highest_bid}. Congratulations!")
    
