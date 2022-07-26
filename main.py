from tkinter import *
from turtle import width
import tkintermapview;

Root = Tk()
Root.title("Sistema de gestion de mineria")
Root.geometry("800x600")

my_label = LabelFrame(Root)
my_label.pack(pady=20, padx=20)

map_widget = tkintermapview.TkinterMapView(
    my_label, 
    width=700, 
    height=500, 
    corner_radius=0
)
map_widget.set_position(8.355074, -62.630637)
map_widget.pack()

""" 
Se muestra un mapa de la zona a operar
se indica las coordenadas
las unidades automaticas trabajaran dentro de las areas reamarcadas
"""
Root.mainloop()