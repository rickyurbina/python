from tkinter import *
from tkinter import messagebox
# -------- Constantes -------------------
WHITE = "#FFFFFF"


#--------- Funciones  -------------------

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get() 

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ups!", message="Asegurate de llenar todos los datos!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Se guardaran estos datos: \nEmail: {email}"
                                                            f"\nPassword: {password}\n es correcto?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
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
genera_pass_button = Button(text="Generar")
genera_pass_button.grid(row=3,column=2)

# command=save dispara la funcion llamada save cuando de da click en el boton
agregar_button = Button(text="Agregar", width=32, command=save )
agregar_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
