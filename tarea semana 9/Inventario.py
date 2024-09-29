# archivo: inventario.py
from producto import Producto

class Inventario:
    def __init__(self):
        """Inicializa el inventario con una lista vacía de productos."""
        self.productos = []

    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al inventario.
        Verifica que el ID del producto sea único.
        """
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: ID ya existente.")
        else:
            self.productos.append(producto)
            print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario por su ID."""
        self.productos = [p for p in self.productos if p.get_id() != id_producto]
        print("Producto eliminado correctamente.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza la cantidad o precio de un producto dado su ID.
        """
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print("Producto actualizado correctamente.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca productos por nombre (puede haber coincidencias parciales)."""
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_productos(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos:
                print(producto)
