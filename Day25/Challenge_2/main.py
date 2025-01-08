import turtle
import pandas as pd

IMAGE = "Brazil_Map.gif"
guessed_states = []

screen = turtle.Screen()

screen.title("Brazil States Game")
screen.addshape(IMAGE)

turtle.shape(IMAGE)

#  Função para pegar as coordenadas da imagem e colocar os nomes dos estados na posição correta.
# def coord(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(coord)
# turtle.mainloop()


data = pd.read_csv("27_states.csv")
states_name = data["state"].tolist()

while len(guessed_states) < 27:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/27 States Correct",
                                    prompt="What is the state name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in states_name:
            if state not in guessed_states:
                missing_states.append(state)
        df_missing_states = pd.DataFrame(missing_states)
        df_missing_states.to_csv("missing_states.csv")
        break
    elif answer_state in guessed_states:
        pass
    elif answer_state in states_name:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(answer_state)

        guessed_states.append(answer_state)


screen.exitonclick()
