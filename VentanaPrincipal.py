import tkinter as tk
from ScreenSelector import ScreenSelector

class VentanaPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        
        boton = tk.Button(self.root, text="Presióname", command=self.instancia_selector)
        boton.pack()

        self.root.mainloop()

    def LabelTranslated(self,text):
        label = tk.Label(self.root, text=text)
        label.pack()
        print (type(text))
    
    def instancia_selector(self):
        selectro = ScreenSelector(self)