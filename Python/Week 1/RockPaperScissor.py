#Play rock paper scissor
import random

print("Welcome to Rock, Paper, Scissors! test your strength against the AI.")
roll = input("Rock, Paper or Scissors?\n").lower()

if roll == ("rock"):
    playerroll = 0
elif roll == ("paper"):
    playerroll = 1
elif roll == ("scissors") or roll == ("scissor"):
    playerroll = 2

airoll = random.randint(0,2)

if playerroll == 0 and airoll == 0:
    print("You chose.. Rock! The AI chose.. Rock! It's a tie!")
elif playerroll == 0 and airoll == 1:
    print("You chose.. Rock! The AI chose.. Paper! You lose!")
elif playerroll == 0 and airoll == 2:
    print("You chose.. Rock! The AI chose.. Scissors! You win!")
elif playerroll == 1 and airoll == 0:
    print("You chose.. Paper! The AI chose.. Rock! You win!")
elif playerroll == 1 and airoll == 1:
    print("You chose.. Paper! The AI chose.. Paper! It's a tie!")
elif playerroll == 1 and airoll == 2:
    print("You chose.. Paper! The AI chose.. Scissors! You lose!")
elif playerroll == 2 and airoll == 0:
    print("You chose.. Scissors! The AI chose.. Rock! You lose!")
elif playerroll == 2 and airoll == 1:
    print("You chose.. Scissors! The AI chose.. Paper! You win!")
elif playerroll == 2 and airoll == 2:
    print("You chose.. Scissors! The AI chose.. Scissors! It's a tie!")
else:
    print("Wrong input. Be sure to input either Rock, Paper or Scissors!")