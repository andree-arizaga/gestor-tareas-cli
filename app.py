# Gestor de Tareas CLI
# Autor: Andree Arizaga

tareas = []


def agregar_tarea():
    titulo = input("Título de la tarea: ").strip()
    if not titulo:
        print("Error: el título de la tarea no puede estar vacío.")
        return
    tareas.append({"titulo": titulo, "completada": False})
    print("Tarea agregada.")


def listar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return
    for numero, tarea in enumerate(tareas, start=1):
        estado = "[X]" if tarea["completada"] else "[ ]"
        print(f"{numero}. {estado} {tarea['titulo']}")


def pedir_numero_tarea():
    try:
        numero = int(input("Número de la tarea: "))
    except ValueError:
        print("Debes escribir un número.")
        return None
    if numero < 1 or numero > len(tareas):
        print("Esa tarea no existe.")
        return None
    return numero - 1


def completar_tarea():
    indice = pedir_numero_tarea()
    if indice is not None:
        tareas[indice]["completada"] = True
        print("Tarea marcada como completada.")


def eliminar_tarea():
    indice = pedir_numero_tarea()
    if indice is not None:
        eliminada = tareas.pop(indice)
        print(f"Tarea eliminada: {eliminada['titulo']}")



def mostrar_menu():
    print("\n===== GESTOR DE TAREAS v1.0 =====")
    print("Escribe el número de una opción y presiona Enter.")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("Saliendo del gestor de tareas...")
            break
        else:
            print("Opción no disponible todavía.")


if __name__ == "__main__":
    main()
