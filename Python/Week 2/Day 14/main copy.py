import random
import art
from game_data import data
import os
#Write a functions that do two things:
#Function a: Pull a random entry from game_data, print all its key values.
#Function b: Pull a random entry from game_data, EXCEPT follower count.

def pull_new_celeb(replaced_celeb):
  replaced_celeb = random.choice(data)
  return replaced_celeb

def GameOver():
  global currentRound
  print("Sorry, you were off. Game Over.")
  print(f"You survived {currentRound} rounds.")

account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
  account_b = random.choice(data)

currentRound = 1
while True:
  print(art.logo)
  print(f"Round {currentRound}")
  print("Which one of these has more followers?")
  print(f"A: {account_a['name']}, a {account_a['description']} from {account_a['country']}")
  print("VS")
  print(f"B: {account_b['name']}, a {account_b['description']} from {account_b['country']}")
  playerguess = input("A or B?\n").lower()
  if playerguess == "a":
    if account_a['follower_count'] > account_b['follower_count']:
      print(f"Correct! {account_a['name']} has {account_a['follower_count']} followers,") 
      print(f"while {account_b['name']} has {account_b['follower_count']}.")
      currentRound += 1
      account_b = random.choice(data)
      os.system('cls')
    else:
      print(f"Wrong! {account_a['name']} has {account_a['follower_count']} followers,")
      print(f"while {account_b['name']} has {account_b['follower_count']}.")
      GameOver()
      break
  elif playerguess == "b":
    if account_b['follower_count'] > account_a['follower_count']:
      print(f"Correct! {account_b['name']} has {account_b['follower_count']} followers,")
      print(f"while {account_a['name']} has {account_a['follower_count']}.")
      currentRound += 1
      account_a = account_b
      account_b = random.choice(data)
      os.system('cls')
    else:
      print(f"Wrong! {account_a['name']} has {account_a['follower_count']} followers,")
      print(f"while {account_b['name']} has {account_b['follower_count']}.")
      GameOver()
      break
  