# Gestor de Tareas CLI
# Autor: Andree Arizaga

tareas = []


def mostrar_menu():
    print("\n===== GESTOR DE TAREAS =====")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "5":
            print("Saliendo del gestor de tareas...")
            break
        else:
            print("Opción no disponible todavía.")


if __name__ == "__main__":
    main()
