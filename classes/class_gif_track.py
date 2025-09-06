# Importa las librerias
import tkinter as tk
from PIL import Image, ImageTk

# Define la clase GIFTrack
class GIFTrack(tk.Label):
    # Crea el constructor de la clase GIFTrack
    def __init__(self, master, filename):
        ima = Image.open(filename)
        self.frames = []
        # Usa try para evitar posibles errores
        try:
            while True:
                self.frames.append(ImageTk.PhotoImage(ima.copy()))
                ima.seek(len(self.frames))
        except EOFError:
            pass
        
        # Define la duracion del gif
        self.delay = int(49000 / ima.info['duration'])
        self.idx = 0
        
        # Crea un constructor para los fps del gif
        super().__init__(master, image=self.frames[0])
        self.after(self.delay, self.play)
    
    # Define la funcion play para ejecutar el gif
    def play(self):
        self.idx = (self.idx + 1) % len(self.frames)
        self.config(image=self.frames[self.idx])
        self.after(self.delay, self.play)