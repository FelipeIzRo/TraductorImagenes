import tkinter as tk

def create_label():
    # Eliminar la etiqueta anterior si existe
    if hasattr(root, 'current_label') and root.current_label:
        root.current_label.pack_forget()

    # Crear una nueva etiqueta
    new_label = tk.Label(root, text="Nueva Etiqueta")
    new_label.pack()
    
    # Guardar la referencia a la nueva etiqueta
    root.current_label = new_label

root = tk.Tk()
root.geometry("300x200")
root.title("Gestión de Etiquetas")

# Inicialmente, no hay etiqueta
root.current_label = None

# Crear un botón para crear una etiqueta
button = tk.Button(root, text="Crear Etiqueta", command=create_label)
button.pack(pady=20)

root.mainloop()