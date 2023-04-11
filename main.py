from turtle import Turtle, Screen
from state import State
import pandas

# Initial setup
turtle = Turtle()
screen = Screen()
screen.title("U.S. States Game")

# Setup background
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=726, height=492)
turtle.shape(image)

# Read CSV file
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

# Save the correct answer
guessed_states = []
while len(guessed_states) <= 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct',
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # Save states that the user did not guess
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

    # Add the of the state to the screem
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        add_state = State(answer_state, int(state_data.x), int(state_data.y))

