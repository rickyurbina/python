import tkinter

# Crear ventana usando tkinter
window = tkinter.Tk()
window.title("Primera Ventana")
window.minsize(width=600, height=400)

my_label = tkinter.Label(font=("Arial", 24, "bold"))
my_label.pack()  # Agrega la etiqueta en la ventana y la coloca en el centro

while True:
    window.mainloop()

