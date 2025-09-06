# Importa las librerias
import tkinter as tk
from PIL import Image, ImageTk

# Crea la clase GIFJeep
class GIFJeep(tk.Label):
    # Crea el constructor para la clase GIFJeep
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
        self.delay = int(10000 / ima.info['duration'])
        self.idx = 0
        
        # Crea un constructor para los fps del gif
        super().__init__(master, image=self.frames[0])
        self.after(self.delay, self.play)
    
    # Define la funcion play para ejecutar el gif
    def play(self):
        self.idx = (self.idx + 1) % len(self.frames)  # Corregido
        self.config(image=self.frames[self.idx])
        self.after(self.delay, self.play)
