import turtle
import pandas as pd

image = "blank_states_img.gif"
states_file = "50_states.csv"
states_guessed = []

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

state = turtle.Turtle() # setting up turtle for text
state.hideturtle()
state.penup()

data = pd.read_csv(states_file) # reads csv
states_list = data.state.to_list() # adds the states to a list

answer_state = screen.textinput("Guess the State", prompt="What is a State's name?").title()

while len(states_guessed) < 50:
    screen.update()

    if answer_state in states_list:
        answer = data[data.state == answer_state]
        state.goto(answer.x.item(), answer.y.item())
        state.write(answer_state) # write correct guess on map
        states_guessed.append(answer)  # record correct guesses in a list

    answer_state = screen.textinput(title=f"{len(states_guessed)}/50 States Correct", prompt="What is a State's name?").title() # keep track of score

screen.exitonclick()
