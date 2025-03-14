import tkinter as tk
from tkinter import messagebox


class AplicacionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación GUI Básica")

        # Etiqueta
        self.label = tk.Label(root, text="Ingrese un dato:")
        self.label.pack()

        # Campo de texto
        self.entry = tk.Entry(root)
        self.entry.pack()

        # Botón Agregar
        self.add_button = tk.Button(root, text="Agregar", command=self.agregar_dato)
        self.add_button.pack()

        # Lista para mostrar los datos
        self.listbox = tk.Listbox(root)
        self.listbox.pack()

        # Botón Limpiar
        self.clear_button = tk.Button(root, text="Limpiar", command=self.limpiar_datos)
        self.clear_button.pack()

    def agregar_dato(self):
        dato = self.entry.get()
        if dato:
            self.listbox.insert(tk.END, dato)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "El campo no puede estar vacío")

    def limpiar_datos(self):
        self.listbox.delete(0, tk.END)


# Crear ventana principal
root = tk.Tk()
app = AplicacionGUI(root)
root.mainloop()
