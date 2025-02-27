import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def to_dict(self):
        return {"ID": self.id_producto, "Nombre": self.nombre, "Cantidad": self.cantidad, "Precio": self.precio}


class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.productos = {}
        self.archivo = archivo
        self.cargar_desde_archivo()

    def añadir_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: ID de producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            print("Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            print("Producto actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p.to_dict() for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        return encontrados if encontrados else "Producto no encontrado."

    def mostrar_todos(self):
        return [p.to_dict() for p in self.productos.values()]

    def guardar_en_archivo(self):
        with open(self.archivo, "w") as f:
            json.dump([p.to_dict() for p in self.productos.values()], f, indent=4)

    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r") as f:
                data = json.load(f)
                self.productos = {p["ID"]: Producto(p["ID"], p["Nombre"], p["Cantidad"], p["Precio"]) for p in data}
        except (FileNotFoundError, json.JSONDecodeError):
            self.productos = {}


# Interfaz de Usuario
def menu():
    inventario = Inventario()
    while True:
        print(
            "\n1. Añadir Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Mostrar Inventario\n6. Guardar y Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.añadir_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deje vacío para no cambiar): ")
            precio = input("Nuevo precio (deje vacío para no cambiar): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None,
                                           float(precio) if precio else None)
        elif opcion == "4":
            nombre = input("Ingrese nombre del producto a buscar: ")
            print(inventario.buscar_producto(nombre))
        elif opcion == "5":
            print(inventario.mostrar_todos())
        elif opcion == "6":
            inventario.guardar_en_archivo()
            print("Inventario guardado. Saliendo...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
