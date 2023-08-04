import turtle
import pandas

states_data = pandas.read_csv("50_states.csv")
state_names = states_data.state.tolist()

guessed_states = []
total_states_count = len(state_names)

screen = turtle.Screen()
screen.title("U.S. States Game")

img = "blank_states_img.gif"
screen.addshape(img)

background = turtle.Turtle()
background.shape(img)

while len(guessed_states) < 50:

    answer_state = screen.textinput(f"{len(guessed_states)}/{total_states_count} States Correct",
                                    "What's another state's name?").title()
    if answer_state == "Exit":
        missed_states = [state for state in state_names if state not in guessed_states]
        pandas.DataFrame(missed_states).to_csv("missed_states.csv")
        break

    if answer_state in state_names and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_cords = states_data[states_data["state"] == answer_state]
        state_name = turtle.Turtle()
        state_name.penup()
        state_name.hideturtle()
        state_name.goto(state_cords.x.item(), state_cords.y.item())
        state_name.write(answer_state)


