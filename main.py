import turtle
import pandas

screen = turtle.Screen()
image = "indian-map.gif"
screen.bgpic(image)

data = pandas.read_csv('indian_states.csv')
states_list = data['state'].to_list()
correct_guess_list = []
states_to_learn = []

while len(correct_guess_list) < 36:
    user_guess = turtle.textinput(prompt='Enter indian states name', title=f'{len(correct_guess_list)}/36 States').title()
    if user_guess in correct_guess_list:
        continue

    elif user_guess == "Exit":

        for i in range(len(states_list)):
            if states_list[i] not in correct_guess_list:
                states_to_learn.append(states_list[i])
        break

    elif user_guess in states_list:
        x = int(data[data.state == user_guess].x)
        y = int(data[data.state == user_guess].y)
        correct_guess_list.append(user_guess)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.color('blue')
        t.goto(x, y)
        t.write(arg=f'{user_guess}', font=('Aerial', 8, 'bold'))

remaining_state_dic = {
    'state': states_to_learn
}
remaining_states = pandas.DataFrame(remaining_state_dic)
remaining_states.to_csv('remaining_states.csv')
