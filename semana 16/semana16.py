import tkinter as tk
from tkinter import messagebox


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("400x400")

        # Lista de tareas
        self.tasks = []

        # Elementos de la interfaz
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=20)

        self.add_button = tk.Button(self.root, text="Añadir Tarea", width=20, command=self.add_task)
        self.add_button.pack(pady=10)

        self.task_listbox = tk.Listbox(self.root, height=10, width=40, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=20)

        self.complete_button = tk.Button(self.root, text="Marcar como Completada", width=20, command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", width=20, command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Asignar atajos de teclado
        self.root.bind("<Return>", self.add_task_from_keyboard)
        self.root.bind("<C>", self.complete_task_from_keyboard)
        self.root.bind("<Delete>", self.delete_task_from_keyboard)
        self.root.bind("<Escape>", self.close_app)

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea.")

    def add_task_from_keyboard(self, event):
        self.add_task()

    def complete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_task_index]
            self.tasks[selected_task_index] = f"{task} (Completada)"
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def complete_task_from_keyboard(self, event):
        self.complete_task()

    def delete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

    def delete_task_from_keyboard(self, event):
        self.delete_task()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def close_app(self, event):
        self.root.quit()


# Crear la ventana principal
root = tk.Tk()
app = TaskManagerApp(root)

# Ejecutar la aplicación
root.mainloop()
