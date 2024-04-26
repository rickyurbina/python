import turtle
import pandas

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


screen = turtle.Screen()
screen.title("States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# --------------------------------------------------------------------------------------
#codigo para dar click en la pantalla y saber las coordenadas de ese punto
# def get_mouse_click(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click)
# #sirve para mantener abierta la pantalla
# turtle.mainloop()
# --------------------------------------------------------------------------------------
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 adivinados",
                                    prompt="Escribe el nombre aqui").title()
    if answer_state == "Exit":
        
        #   aqui podemos agregar el tema de List Comprehension para reducir el codigo siguiente
        missing_states = [state for state in all_states if state not in guessed_states]

        # ------------------   codigo reucido con la linea anterior
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)


        # grabaos en un archivo los estados que no adivino el usuario para saber cuales estudiar
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        #podemos tomar la respuesta que escribió el usuario
        #t.write(answer_state)
        # o podemos limpiar el indice del archivo y mostrarlo
        t.write(state_data.state.item())
# screen.exitonclick()
#turtle.mainloop()
print(guessed_states)