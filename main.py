# main.py
from tkinter import *

root = Tk()
root.geometry("1200x900")
root.title("Mapa Gabinetów")

# Create frames
ramka_lista = Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly = Frame(root)
ramka_mapa = Frame(root)

# Grid layout
ramka_lista.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly.grid(row=1, column=0, columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)

root.mainloop()