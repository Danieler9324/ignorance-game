# Importa librerias
import tkinter as tk
from PIL import Image, ImageTk

# Crea la clase GIFElephant
class GIFElephant(tk.Label):
    #Crea el constructor de la clase GIFElephant
    def __init__(self, master, filename):
        ima = Image.open(filename)
        self.frames = []
        # Usa el metodo try para eliminar posibles errores
        try:
            while True:
                self.frames.append(ImageTk.PhotoImage(ima.copy()))
                ima.seek(len(self.frames))
        except EOFError:
            pass
        
        # Establece la duracion del GIFElephant (en milisegundos)
        self.delay = int(30000 / ima.info['duration'])
        self.idx = 0
        
        # Crea un constructor para el delay 
        super().__init__(master, image=self.frames[0])
        self.after(self.delay, self.play)
    
    # Define la funcion play para ejecutar el gif
    def play(self):
        self.idx = (self.idx + 1) % len(self.frames)
        self.config(image=self.frames[self.idx])
        self.after(self.delay, self.play)
