import turtle
import pandas
FONT = ("Arial", 10, "normal")

screen = turtle.Screen()
screen.title("Guess the States!")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
turtle.penup()
guess_amount = 0
guessed_states = []
states_data = pandas.read_csv("50_states.csv")
state_names = states_data.state.to_list()

game_ongoing = True

while game_ongoing == True:

    answer_state = screen.textinput(title=f"{guess_amount}/50 States guessed.", prompt="Name a State!").title()

    if answer_state in state_names:
        current_state  = states_data[states_data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(current_state.x) , int(current_state.y))
        t.write(answer_state)
        guess_amount += 1
        guessed_states.append(answer_state)
        if guess_amount == 50:
            game_ongoing = False

    # Obsolete code for a more difficult solution
    # for index, state in states_data.iterrows():
    #     if answer == state["state"]:
    #         x = state["x"]
    #         y = state["y"]
    #         turtle.goto(x, y)
    #         turtle.write(answer_state, font=FONT)
    #         guess_amount += 1




turtle.mainloop()

