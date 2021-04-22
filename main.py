from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("Guess the US States")
screen.setup(725, 491)
screen.bgpic("blank_states_img.gif")

turtle = Turtle()
turtle.hideturtle()
turtle.penup()
turtle.color("black")

data = pandas.read_csv("50_states.csv")
guesses_list = []
guessed = 0

while len(guesses_list) < 50:
    user_input = screen.textinput(f"{guessed}/50 States Correct", "Please enter a name of the state:").title()

    if user_input in data["state"].to_list():
        coordinates = data[data.state == user_input]
        turtle.goto(int(coordinates["x"]), int(coordinates["y"]))
        turtle.write(f"{user_input}", move=False, align="left", font=("Arial", 8, "normal"))
        guessed += 1
        guesses_list.append(user_input)
    elif user_input.lower() == 'exit':
        # I am using list comprehensions, save up a lot of lines
        state_names = [state for state in data["state"].to_list() if state not in guesses_list]
        state_x = [int(data[data.state == state].x) for state in data["state"].to_list() if state not in guesses_list]
        state_y = [int(data[data.state == state].y) for state in data["state"].to_list() if state not in guesses_list]
        # for state in data["state"].to_list():
        #     if state not in guesses_list:
        #         state_names.append(state)
        #         state_x.append(int(data[data.state == state].x))
        #         state_y.append(int(data[data.state == state].y))
        remaining = {"State": state_names, "X-Coordinates": state_x, "Y-Coordinate": state_y}
        custom_data_frame = pandas.DataFrame(remaining)
        custom_data_frame.to_csv("Remaining States.csv")
        screen.bye()
        break
