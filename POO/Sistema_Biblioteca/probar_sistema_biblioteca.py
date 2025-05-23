# Creamos un objeto de tipo biblioteca
from Sistema_Biblioteca.Clase_Biblioteca import Biblioteca
from Sistema_Biblioteca.Clase_Libro import Libro

bibliotecaMai = Biblioteca('Biblioteca Mai')

# Agregar algunos libros
libro1 = Libro('El Alquimista', 'Paulo Cohelo', 'Ficción')
libro2 = Libro('1984', 'George Orwell', 'Ficción')
libro3 = Libro('El código Da Vinci', 'Dan Brown', 'Misterio')
libro4 = Libro('Rayuela', 'Julio Cortázar', 'Novela')
libro5 = Libro('Verónica decide morir', 'Paulo Cohelo', 'Ficción')
# Agregar los libros a la biblioteca
bibliotecaMai.agregar_libro(libro1)
bibliotecaMai.agregar_libro(libro2)
bibliotecaMai.agregar_libro(libro3)
bibliotecaMai.agregar_libro(libro4)
bibliotecaMai.agregar_libro(libro5)

# Nombre de la biblioteca
print(f'*** Bienvenidos a la {bibliotecaMai.nombre} ***')

# Buscar libros por autor
print(f'\nLibros de Paulo Cohelo: ')
bibliotecaMai.buscar_libro_por_autor('Paulo Cohelo')

# Buscar libros por género
print(f'\nLibros de Ficción: ')
bibliotecaMai.buscar_libro_por_genero('Ficción')

# Mostrar todos los libros de la biblioteca
bibliotecaMai.mostrar_todos_los_libros()