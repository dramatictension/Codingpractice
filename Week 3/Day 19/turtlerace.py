import turtle
import random

screen = turtle.Screen()
screen.setup(width=500, height=400)

sheldon = turtle.Turtle()
shelly = turtle.Turtle()
shatner = turtle.Turtle()
shelbert = turtle.Turtle()
sharles = turtle.Turtle()


def maketurtles():
    sheldon.shape("turtle")
    shelly.shape("turtle")
    shatner.shape("turtle")
    shelbert.shape("turtle")
    sharles.shape("turtle")
    sheldon.color("red")
    shelly.color("blue")
    shatner.color("green")
    shelbert.color("yellow")
    sharles.color("purple")
    sheldon.penup()
    shelly.penup()
    shatner.penup()
    shelbert.penup()
    sharles.penup()


def moveturtles():
    sheldonrandom = random.randint(0, 10)
    shellyrandom = random.randint(0, 10)
    shatnerrandom = random.randint(0, 10)
    shelbertrandom = random.randint(0, 10)
    sharlesrandom = random.randint(0, 10)
    sheldon.forward(sheldonrandom)
    shelly.forward(shellyrandom)
    shatner.forward(shatnerrandom)
    shelbert.forward(shelbertrandom)
    sharles.forward(sharlesrandom)


def determinewinner():
    winner = ""
    if sheldon.xcor() >= 250:
        winner = "red"
    elif shelly.xcor() >= 250:
        winner = "blue"
    elif shatner.xcor() >= 250:
        winner = "green"
    elif shelbert.xcor() >= 250:
        winner = "yellow"
    elif sharles.xcor() >= 250:
        winner = "purple"
    return winner


def race():
    while True:
        moveturtles()
        winner = determinewinner()
        if winner:
            break


maketurtles()

user_bet = screen.textinput(
    "Turtle race!", "Bet on a Turtle! Red, Blue, Green, Yellow or Purple"
).lower()

sheldon.goto(-230, 100)
shelly.goto(-230, 50)
shatner.goto(-230, 0)
shelbert.goto(-230, -50)
sharles.goto(-230, -100)

race()
winner = determinewinner()
screen.bye()
print(f"The winner is: {winner}!")
if user_bet == winner:
    print("You won!")
else:
    print("Too bad!")
