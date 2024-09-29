
import os
import subprocess

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print(f"El archivo {ruta_script_absoluta} no se encontró. Verifica que la ruta sea correcta.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.run(['python', ruta_script], check=True)  # Cambié Popen por run
        else:  # Unix-based systems
            subprocess.run(['python3', ruta_script], check=True)  # Cambié Popen por run
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    unidades = {
        '1': 'Unidad 1 - Introduccion',
        '2': 'Unidad 2 - Clases y objetos',
        '3': 'Unidad 3 - Herencia y polimorfismo',  # Corregido error tipográfico
        '4': 'Mis tareas personales'  # Nueva opción personalizada
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú principal
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            ruta_unidad = os.path.join(ruta_base, unidades[eleccion_unidad])
            if os.path.exists(ruta_unidad):
                mostrar_sub_menu(ruta_unidad)
            else:
                print(f"La ruta {ruta_unidad} no existe.")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_sub_menu(ruta_unidad):
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\nSubmenú - Selecciona una subcarpeta")
        # Imprime las subcarpetas
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_scripts(ruta_sub_carpeta):
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\nScripts - Selecciona un script para ver y ejecutar")
        # Imprime los scripts
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion_script = input("Elige un script, '0' para regresar o '9' para ir al menú principal: ")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return  # Regresar al menú principal
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print("Opción no válida. Regresando al menú de scripts.")
                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

tareas = []  # Lista para almacenar las tareas

def gestionar_tareas():
    while True:
        print("\nGestión de Tareas")
        print("1 - Ver tareas")
        print("2 - Agregar tarea")
        print("3 - Eliminar tarea")
        print("0 - Regresar al menú principal")

        opcion = input("Elige una opción: ")
        if opcion == '1':
            if not tareas:
                print("No tienes tareas pendientes.")
            else:
                print("\nTus tareas:")
                for i, tarea in enumerate(tareas, start=1):
                    print(f"{i}. {tarea}")
        elif opcion == '2':
            nueva_tarea = input("Escribe la nueva tarea: ")
            if nueva_tarea.strip() == "":
                print("La tarea no puede estar vacía. Intenta nuevamente.")
            else:
                tareas.append(nueva_tarea)
                print("Tarea agregada.")
        elif opcion == '3':
            if not tareas:
                print("No tienes tareas para eliminar.")
            else:
                print("\nTus tareas:")
                for i, tarea in enumerate(tareas, start=1):
                    print(f"{i}. {tarea}")
                try:
                    indice = int(input("Elige el número de la tarea a eliminar: ")) - 1
                    if 0 <= indice < len(tareas):
                        tareas.pop(indice)
                        print("Tarea eliminada.")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Entrada no válida.")
        elif opcion == '0':
            break
        else:
            print("Opción no válida.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
