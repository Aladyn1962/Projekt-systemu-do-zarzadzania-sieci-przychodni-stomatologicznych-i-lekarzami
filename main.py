# main.py
from tkinter import *
import tkintermapview

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

map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1200, height=600, corner_radius=5)
map_widget.set_position(52.23, 21.0)  # Warsaw coordinates
map_widget.set_zoom(6)
map_widget.grid(row=0, column=0, columnspan=3)


class Gabinet:
    def __init__(self, nazwa, ulica, miejscowosc, nr_budynku):
        self.nazwa = nazwa
        self.ulica = ulica
        self.miejscowosc = miejscowosc
        self.nr_budynku = nr_budynku
        self.pracownicy = []
        self.pacjenci = []


# main.py
gabinet_list = []


def dodaj_gabinet():
    nazwa = entry_nazwa.get()
    ulica = entry_ulica.get()
    miejscowosc = entry_miejscowosc.get()
    nr = entry_nr_budynku.get()

    gabinet = Gabinet(nazwa, ulica, miejscowosc, nr)
    gabinet_list.append(gabinet)
    pokaz_liste_gabinetow()