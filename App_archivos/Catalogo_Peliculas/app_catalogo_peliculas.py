from Catalogo_Peliculas.clase_servicio_peliculas import ServicioPeliculas
from Catalogo_Peliculas.clase_pelicula import Pelicula

class AppCatalogoPeliculas:
    def __init__(self):
        self.servicio_peliculas = ServicioPeliculas()

    def mostrar_menu(self):
        print('*** App Catálogo Películas ***')
        while True: # El bucle sigue hasta que salir se convierte en True
            try:
                print(f'''Opciones:
                1. Agregar Película
                2. Listar Películas
                3. Eliminar Catálogo
                4. Salir''')
                opcion = int(input("Elige una opción (1-4): "))
                if opcion == 1:
                    nombre_pelicula = input("Introduce el nombre de la película: ")
                    pelicula = Pelicula(nombre_pelicula)
                    self.servicio_peliculas.agregar_pelicula(pelicula)
                elif opcion == 2:
                    self.servicio_peliculas.listar_peliculas()
                elif opcion == 3:
                    self.servicio_peliculas.eliminar_archivo_peliculas()
                elif opcion == 4:
                    print("¡Hasta luego!")
                    break
                else:
                    print("Error: Opción no válida, por favor elige entre 1 y 4.")
            except ValueError:
                print("Error: Por favor ingresa un número válido para la opción.")
            except Exception as e:
                print(f"Error inesperado en el menú: {e}")

if __name__ == "__main__":
    app = AppCatalogoPeliculas()  # Creamos la instancia de la clase
    app.mostrar_menu()  # Llamamos al metodo para mostrar el menú


