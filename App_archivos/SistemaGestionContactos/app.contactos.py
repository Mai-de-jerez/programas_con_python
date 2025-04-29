from GestionContactos import GestionContactos

def menu():
    gestion = GestionContactos('contactos.txt')
    while True:
        print("\n--- Menú de Gestión de Contactos ---")
        print("1. Agregar contacto")
        print("2. Mostrar todos los contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Correo electrónico: ")
            gestion.agregar_contacto(nombre, telefono, email)

        elif opcion == '2':
            gestion.mostrar_contactos()

        elif opcion == '3':
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            gestion.buscar_contacto(nombre)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            gestion.eliminar_contacto(nombre)

        elif opcion == '5':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, inténtelo de nuevo.")

if __name__ == "__main__":
    menu()
