#Sistema de inventario

import os
import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    ARCHIVO_INVENTARIO = "inventario.txt"

    def __init__(self):
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo de inventario."""
        if not os.path.exists(self.ARCHIVO_INVENTARIO):
            with open(self.ARCHIVO_INVENTARIO, 'w') as file:
                json.dump([], file)  # Crear un archivo vacío si no existe
        try:
            with open(self.ARCHIVO_INVENTARIO, 'r') as file:
                self.productos = [Producto(**p) for p in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            print("Error al cargar el inventario. Puede que el archivo esté corrupto.")
        except PermissionError:
            print("No tienes permisos para leer el archivo de inventario.")

    def guardar_inventario(self):
        """Guarda los productos en el archivo de inventario."""
        try:
            with open(self.ARCHIVO_INVENTARIO, 'w') as file:
                json.dump([p.__dict__ for p in self.productos], file, indent=4)
        except PermissionError:
            print("No tienes permisos para escribir en el archivo de inventario.")

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        """Agrega un nuevo producto al inventario y guarda los cambios."""
        self.productos.append(Producto(id_producto, nombre, cantidad, precio))
        self.guardar_inventario()
        print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto por su ID y guarda los cambios."""
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        self.guardar_inventario()
        print("Producto eliminado correctamente.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)

if __name__ == "__main__":
    inventario = Inventario()
    while True:
        print("\n1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar inventario")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(id_producto, nombre, cantidad, precio)
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            inventario.mostrar_inventario()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
