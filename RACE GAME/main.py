import random
import turtle as t

race_on = True

screen_mode = t.Screen()

screen_mode.setup(width=800, height=500)
user_bet = screen_mode.textinput(title="Make your bet", prompt='What turtle will win the race?'
                                                          'Enter color:\n')

y_cordinates = [-100, -60, -20, 20, 50]
colors = ['lime', 'red', 'purple', 'blue', 'maroon']

all_turle = []
for turtle_index in range(0, 5):
    tim = t.Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-390, y=y_cordinates[turtle_index])
    all_turle.append(tim)

while race_on:

    for turtle in all_turle:
        if turtle.xcor() > 390:
            race_on = False
            winning_turtle = turtle.pencolor()

            if winning_turtle == user_bet:
                print(f"You have won, {winning_turtle} is the winner of the race")

            else:
                print(f"You have lost, {winning_turtle} is the winner of the race")

        random_forward = random.randint(0, 10)
        turtle.forward(random_forward)

screen_mode.exitonclick()
