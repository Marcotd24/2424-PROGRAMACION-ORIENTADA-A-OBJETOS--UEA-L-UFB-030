# archivo: producto.py

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor que inicializa un producto con su ID, nombre, cantidad y precio.
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        """Devuelve el ID del producto."""
        return self.id_producto

    def get_nombre(self):
        """Devuelve el nombre del producto."""
        return self.nombre

    def get_cantidad(self):
        """Devuelve la cantidad del producto."""
        return self.cantidad

    def get_precio(self):
        """Devuelve el precio del producto."""
        return self.precio

    def set_cantidad(self, cantidad):
        """Establece una nueva cantidad para el producto."""
        self.cantidad = cantidad

    def set_precio(self, precio):
        """Establece un nuevo precio para el producto."""
        self.precio = precio

    def __str__(self):
        """Devuelve una representación en cadena del producto."""
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"
