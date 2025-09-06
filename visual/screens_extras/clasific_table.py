# Importa la libreria de tkinter
import tkinter as tk
from tkinter import ttk

# Define la funcion de la pantalla de clasificacion
def screen_clasification(clasification_data):
    # Se define como una pantalla flotante
    clasification_window = tk.Toplevel()
    clasification_window.title("Clasificacion")
    clasification_window.geometry("400x300")
    clasification_window.config(bg="Black")
    title = tk.Label(clasification_window, text="Clasificacion", font="Helvetica 18 bold", bg="Black", fg="White")
    title.pack(pady=10)
    
    # Crea las columnas de la tabla
    tree = ttk.Treeview(clasification_window, columns=("Jugador", "Ganadas"), show="headings", height=5)
    tree.heading("Jugador", text="Jugador")
    tree.heading("Ganadas", text="Puntos")
    
    # Obtiene los valores que les den los jugadores
    for player, wined in clasification_data.items():
        tree.insert("", "end", values=(player, wined))
    
    tree.pack(pady=20)

    # Muestra la pantalla
    clasification_window.mainloop()