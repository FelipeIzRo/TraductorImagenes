import tkinter as tk

root = tk.Tk()
root.title("Ejemplo con Label")

# Crear y añadir un Label con texto
label = tk.Label(root, text="Hola, este es un Label en Tkinter")
label.pack(pady=20)

root.mainloop()