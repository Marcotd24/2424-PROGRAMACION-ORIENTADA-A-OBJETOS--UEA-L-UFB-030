import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha and hora and descripcion:
        tree.insert("", "end", values=(fecha, hora, descripcion))
        entry_fecha.delete(0, tk.END)
        entry_hora.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Todos los campos deben estar llenos")


def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        confirmacion = messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar el evento?")
        if confirmacion:
            tree.delete(seleccionado)
    else:
        messagebox.showwarning("Error", "Selecciona un evento para eliminar")


# Configuración de la ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("500x400")

# Frame para la lista de eventos
tree_frame = tk.Frame(root)
tree_frame.pack(pady=10)

# TreeView para mostrar los eventos
tree = ttk.Treeview(tree_frame, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# Frame para los campos de entrada
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Campos de entrada
label_fecha = tk.Label(input_frame, text="Fecha (YYYY-MM-DD):")
label_fecha.grid(row=0, column=0)
entry_fecha = tk.Entry(input_frame)
entry_fecha.grid(row=0, column=1)

label_hora = tk.Label(input_frame, text="Hora (HH:MM):")
label_hora.grid(row=1, column=0)
entry_hora = tk.Entry(input_frame)
entry_hora.grid(row=1, column=1)

label_descripcion = tk.Label(input_frame, text="Descripción:")
label_descripcion.grid(row=2, column=0)
entry_descripcion = tk.Entry(input_frame)
entry_descripcion.grid(row=2, column=1)

# Frame para los botones
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

btn_agregar = tk.Button(button_frame, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=5)

btn_eliminar = tk.Button(button_frame, text="Eliminar Evento", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=5)

btn_salir = tk.Button(button_frame, text="Salir", command=root.quit)
btn_salir.grid(row=0, column=2, padx=5)

root.mainloop()

