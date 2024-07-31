import tkinter as tk
from PIL import Image,ImageTk
from ScreenSelector import ScreenSelector

class VentanaPrincipal:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('600x400')
        self.root.configure(bg='#808185')

        size = (150, 50)
        image = ImageTk.PhotoImage(Image.open('imagesInterface/button.png').resize(size))

        button = tk.Button(self.root,
                          text='EmpezarTraduccion',
                          command=self.instancia_selector,
                          cursor='hand2',
                          bg=self.root.cget('bg'),
                          bd=0,
                          image=image)
        button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=1, pady=1)

        self.label = tk.Label(self.root, text='EmpezarTraduccion')
        self.label.pack()
        

        self.root.mainloop()

        
    def LabelTranslated(self,text):
        self.label.pack_forget()
        self.label = tk.Label(self.root, text=text)
        self.label.pack()
        print (type(text))
    
    def instancia_selector(self):
        selector = ScreenSelector(self)