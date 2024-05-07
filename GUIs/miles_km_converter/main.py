from tkinter import *

def mill_a_kms():
    mill = float(millas.get())
    kms_total = mill * 1.609
    kms_label.config(text=f"{kms_total}")


window = Tk()
window.title("Convertidor de Millas a Kms")
window.config(padx=20, pady=20)

millas = Entry(width=7, text=0)
millas.grid(column=1, row=0)

mill_Label = Label(text="Millas")
mill_Label.grid(column=2, row=0)

es_igual = Label(text="es igual a ")
es_igual.grid(column=0, row=1)

kms_label = Label(text="0")
kms_label.grid(column=1, row=1)

kms = Label(text="Km")
kms.grid(column=2, row=1)

btn_calcular = Button(text="Calcular", command=mill_a_kms)
btn_calcular.grid(column=1, row=2)

while True:
    window.mainloop()
