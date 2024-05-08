from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

# -------- Constantes -------------------
WHITE = "#FFFFFF"


# ----------------    Password Generator   ----------------------
def generate_password():
    #password = ""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    pssword_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_letters + password_numbers
    
    shuffle(password_list)

    password = "".join(password_list)

    #print(f"Your password is: {password}")
    pass_entry.delete(0, 'end')
    pass_entry.insert(0, password)

#--------- Funciones  -------------------

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get() 
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ups!", message="Asegurate de llenar todos los datos!")
    else:
        # Agregamos el manejo de errores para cuando el archivo .jsnon no existe aun, en ese caso solamente 
        # se crea un archivo nuevo con la información
        try:        # ------------- codigo que se intenta ejecutar
            with open("data.json", "w") as data_file:
                #reading old data
                data = json.load (data_file)
        except FileNotFoundError:       # ------------- codigo que se ejecuta is hay un error
            with open("data.json", w) as data_file:
                json.dump(data, data_file, indent=4)
        else:           # ------------- Codigo que se ejecuta si no hay error en el intento
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", w) as data_file:
                #saving updated data
                json.dump(data, data_file, indent=4)
        finally:            # -------------    Codigo que se ejecuta haya error o no 
            website_entry.delete(0, END)
            pass_entry.delete(0, END)


# --------    GUI    --------------------
window = Tk()
window.title("My Password")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
pass_label = Label(text="Password")
pass_label.grid(row=3, column=0)

# Inputs
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
#da el enfoque al input website_entry
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
#pone un valor inicial al campo email
email_entry.insert(0,"mail@gmail.com")
pass_entry = Entry(width=25)
pass_entry.grid(row=3, column=1)

#botones
genera_pass_button = Button(text="Generar", command=generate_password)
genera_pass_button.grid(row=3,column=2)

# command=save dispara la funcion llamada save cuando de da click en el boton
agregar_button = Button(text="Agregar", width=32, command=save )
agregar_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
