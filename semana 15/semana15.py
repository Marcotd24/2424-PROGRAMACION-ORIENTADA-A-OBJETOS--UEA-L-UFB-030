import tkinter as tk
from tkinter import messagebox

def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Por favor, ingresa una tarea.")

def marcar_completada():
    try:
        index = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(index)
        lista_tareas.delete(index)
        lista_tareas.insert(index, f"✔ {tarea}")
    except IndexError:
        messagebox.showwarning("Selección requerida", "Por favor, selecciona una tarea para marcarla como completada.")

def eliminar_tarea():
    try:
        index = lista_tareas.curselection()[0]
        lista_tareas.delete(index)
    except IndexError:
        messagebox.showwarning("Selección requerida", "Por favor, selecciona una tarea para eliminar.")

def agregar_con_enter(event):
    agregar_tarea()

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x300")

# Campo de entrada y botón para agregar tarea
entrada_tarea = tk.Entry(root, width=40)
entrada_tarea.pack(pady=10)
entrada_tarea.bind("<Return>", agregar_con_enter)

btn_agregar = tk.Button(root, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.pack()

# Lista de tareas
lista_tareas = tk.Listbox(root, width=50, height=10)
lista_tareas.pack(pady=10)

# Botones de acción
btn_completar = tk.Button(root, text="Marcar como Completada", command=marcar_completada)
btn_completar.pack()

btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack()

# Iniciar la aplicación
root.mainloop()
