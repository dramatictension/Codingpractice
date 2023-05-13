import random
import os

LivesRemaining = 0
Difficulty = 0
PlayerNumber = 0

#define functions to determine starting lives, a function to decrease global lives by 1 if the guess is wrong, and victory.
def ChooseDifficulty():
    while True:
        chosenDifficulty = input("Choose your difficulty. Type 'easy' or 'hard' ").lower()
        if chosenDifficulty == "easy":
            print("You've chosen easy difficulty!")
            break
        
        elif chosenDifficulty == "hard":
            print("You've chosen hard difficulty!")
            break
        else:
            print("Please answer with 'easy' or 'hard'.")
    
    if chosenDifficulty == "easy":
        return 10

    else:
        return 5
def TooHigh():
    print("Too high.\nGuess again.")
    global LivesRemaining
    LivesRemaining =- 1
def TooLow():
    print("Too low.\nGuess again.")
    global LivesRemaining
    LivesRemaining =- 1
def PrintLivesRemaining(Lives):
    print(f"You have {Lives} lives remaining.")
def Victory(PlayerNumber, VictoryLivesRemaining):
    print(f"Yes! I was thinking of {PlayerNumber}! You got it!")
    print(f"Congratulations! You've won with {VictoryLivesRemaining} lives remaining.")

def Defeat(FinalCPUNumber):
    print("Sorry, you're out of lives.")
    print(f"The number I was thinking of was {FinalCPUNumber}!")

#roll number to guess, set lives to 5 for hard mode, 10 for easy mode
#Print welcome, list Easy or Hard, ask for input to determine mode

while True:
    print("Welcome to the number guessing game!")
    LivesRemaining = int(ChooseDifficulty())
    print("I'm thinking of a number between 1 and 100.")
    CPUnumber = random.randint(1, 100)
    #Testing code
    #print(CPUnumber)
    PrintLivesRemaining(Lives=LivesRemaining)

    #Check if guessed number == rolled number, if yes, win, if no, check if guessed number is higher or lower, print which, lose a life
    while LivesRemaining > 0:
        
        PlayerNumber = int(input("Make a guess: "))
        if PlayerNumber > CPUnumber:
            LivesRemaining = TooHigh()
            PrintLivesRemaining(Lives=LivesRemaining)
            
        elif PlayerNumber < CPUnumber:
            LivesRemaining = TooLow()
            PrintLivesRemaining(Lives=LivesRemaining)
        elif PlayerNumber == CPUnumber:
            Victory(PlayerNumber=CPUnumber, VictoryLivesRemaining=LivesRemaining)
            break
    if LivesRemaining == 0:
        Defeat(FinalCPUNumber=CPUnumber)
    playagain = input("Wanna play again? 'yes' or 'no' ").lower()
    if playagain == "no":
        print("Thanks for playing!")
        break
    else:
        os.system('cls')
