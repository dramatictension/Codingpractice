import random

def get_card_value(card):
    if card == "Ace":
        # Return a list containing both possible values of the Ace
        isace = input("You drew an ace! Is this a 1 or 11?")
        while isace != "1" and isace != "11":
            isace = input("Please type 1 or 11.")
        if isace == "1":
            return 1
        elif isace == "11":
            return 11
        
    elif card in ["Jack", "Queen", "King"]:
        # Return 10 for all face cards
        return 10
    else:
        # For numeric cards, return the corresponding integer value
        return cards_dict[card]

#Library of cards. King, Queen, Jack = 10, ace is either 1 or 11
cards_dict = {
    "2":2 , "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10, "Ace": [1, 11]
}
#Pull cards of player and dealer
while True:
    player_card1 = random.choice(list(cards_dict.keys()))
    if player_card1 == "Ace":
        print("You drew an ace! Is this a 1 or a 11?")
        card1_isace = input("")
        if card1_isace == "1":
            player_card1 = 1
        elif card1_isace == "11":
            player_card1 = 11
    player_card2 = random.choice(list(cards_dict.keys()))
    if player_card2 == "Ace":
        print("You drew an ace! Is this a 1 or a 11?")
        card2_isace = input("")
        if card2_isace == "1":
            player_card2 = 1
        elif card2_isace == "11":
            player_card2 = 11
    player_card3 = 0
    dealer_card1 = random.choice(list(cards_dict.keys()))
    if dealer_card1 == "Ace":
        dealer_card1 = 11
    dealer_card2 = random.choice(list(cards_dict.keys()))
    if dealer_card2 == "Ace":
        if dealer_card1 <11:
            dealer_card2 = 11
        else:
            dealer_card2 = 1
    dealer_card3 = 0


    #Print both of the cards the player pulled, as well as one of the dealer's
    print(f"Cards have been drawn!\nYour cards: {player_card1} and {player_card2}")
    print(f"Dealer's cards: {dealer_card1} and ?")
    player_sum =  get_card_value(player_card1) + get_card_value(player_card2)
    dealer_sum = get_card_value(dealer_card1) + get_card_value(dealer_card2)
    print(f"Your current score is {player_sum}")
    #If player score is >21, fail
    if player_sum >21:
        print("You went over 21. You lose.")
        playagain = input("Wanna play again? Y or N\n").lower()
        if playagain == "n":
            print("Thanks for playing!")
            break
    if dealer_sum == 21:
        print("The dealer has Blackjack. You lose.")
    pullcard3 = input("Want to pull a third card? Y or N\n").lower()
    if pullcard3 == "y":
        player_card3 = random.choice(list(cards_dict.keys()))
        print(f"You pulled a {player_card3}")
        player_sum += get_card_value(player_card3)
        if player_sum > 21:
            print("You went over 21. You lose.")
            playagain = input("Wanna play again? Y or N\n").lower()
            if playagain == "n":
                print("Thanks for playing!")
                break
        print(f"Your score is {player_sum}")
    print(f"The dealer's second card is revealed: \nThe dealer has {dealer_card1}, {dealer_card2}")
    if player_sum == 21 and dealer_sum <21:
        print("Blackjack! You win!")
        playagain = input("Wanna play again? Y or N \n").lower()
        if playagain == "n":
            print("Thanks for playing!")
            break
    if dealer_sum<player_sum:
        print("The dealer pulls a third card..")
        dealer_card3 = random.choice(list(cards_dict.keys()))
        print(f"Dealer pulls {dealer_card3}!")
        dealer_sum += get_card_value(dealer_card3)
    if dealer_sum>21:
        ("Bust! Dealer went over 21. You win!")
        playagain = input("Wanna play again? Y or N \n").lower()
        if playagain == "n":
            print("Thanks for playing!")
            break
    if player_sum == dealer_sum:
        print("Tied score. You lose.")
        playagain = input("Wanna play again? Y or N \n").lower()
        if playagain == "n":
            print("Thanks for playing!")
            break
    print(f"Your final score is {player_sum}")
    print(f"The dealer's final score is {dealer_sum}")
    if player_sum > dealer_sum:
        print("You win!")
        playagain = input("Wanna play again? Y or N \n").lower()
        if playagain == "n":
            print("Thanks for playing!")
            break
    else:
        print("You lose.")
        playagain = input("Wanna play again? Y or N \n").lower()
        if playagain == "n":
            print("Thanks for playing!")
            break
    


#Ask player Y or N to pull another card

#If player card value is over 21, lose. If dealer and player have the same hand, player draws. If dealer <17, dealer draws.
#If both dealer and player have less than 21, add values of player and dealer, highest number wins.