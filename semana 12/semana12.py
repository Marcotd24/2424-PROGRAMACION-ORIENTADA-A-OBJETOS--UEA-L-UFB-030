class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.user_id}, Libros prestados: {[libro.info[0] for libro in self.libros_prestados]}"


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario {ISBN: Libro}
        self.usuarios = set()  # Conjunto de IDs de usuarios únicos
        self.registro_usuarios = {}  # Diccionario {ID: Usuario}

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro
        print(f"Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            eliminado = self.libros_disponibles.pop(isbn)
            print(f"Libro eliminado: {eliminado}")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.usuarios:
            self.usuarios.add(usuario.user_id)
            self.registro_usuarios[usuario.user_id] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print("El ID de usuario ya existe.")

    def dar_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            self.usuarios.remove(user_id)
            eliminado = self.registro_usuarios.pop(user_id)
            print(f"Usuario eliminado: {eliminado.nombre}")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, user_id, isbn):
        if user_id in self.registro_usuarios and isbn in self.libros_disponibles:
            usuario = self.registro_usuarios[user_id]
            libro = self.libros_disponibles.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.info[0]}' prestado a {usuario.nombre}")
        else:
            print("Usuario no registrado o libro no disponible.")

    def devolver_libro(self, user_id, isbn):
        if user_id in self.registro_usuarios:
            usuario = self.registro_usuarios[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Libro '{libro.info[0]}' devuelto por {usuario.nombre}")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no registrado.")

    def buscar_libro(self, filtro, tipo="titulo"):
        resultados = []
        for libro in self.libros_disponibles.values():
            if tipo == "titulo" and filtro.lower() in libro.info[0].lower():
                resultados.append(libro)
            elif tipo == "autor" and filtro.lower() in libro.info[1].lower():
                resultados.append(libro)
            elif tipo == "categoria" and filtro.lower() in libro.categoria.lower():
                resultados.append(libro)

        if resultados:
            print("Resultados de búsqueda:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros con ese criterio.")

    def listar_libros_prestados(self, user_id):
        if user_id in self.registro_usuarios:
            usuario = self.registro_usuarios[user_id]
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(libro)
        else:
            print("Usuario no registrado.")


# Ejemplo de uso
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Agregar libros
    libro1 = Libro("1984", "George Orwell", "Ficción", "12345")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "67890")
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    # Registrar usuario
    usuario1 = Usuario("Juan Pérez", "U001")
    biblioteca.registrar_usuario(usuario1)

    # Prestar libro
    biblioteca.prestar_libro("U001", "12345")

    # Listar libros prestados
    biblioteca.listar_libros_prestados("U001")

    # Devolver libro
    biblioteca.devolver_libro("U001", "12345")

    # Buscar libros por título
    biblioteca.buscar_libro("1984", "titulo")

    # Eliminar libro
    biblioteca.quitar_libro("67890")
