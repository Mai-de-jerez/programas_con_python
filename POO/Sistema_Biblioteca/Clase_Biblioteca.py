class Biblioteca:

    def __init__(self, nombre: str):
        self._nombre = nombre
        self._inventario = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def inventario(self):
        return self._inventario


    def agregar_libro(self, libro):
        self._inventario.append(libro)


    def buscar_libro_por_autor(self, autor: str):
        for libro in self._inventario:
            if libro.autor.lower() == autor.lower():
                self.mostrar_libro(libro)

    def mostrar_libro(self, libro):
        print(f'Libro -> Título: {libro.titulo}, Autor: {libro.autor},'
              f'Género: {libro.genero}')


    def buscar_libro_por_genero(self, genero: str):
        for libro in self._inventario:
            if libro.genero.lower() == genero.lower():
                self.mostrar_libro(libro)


    def mostrar_todos_los_libros(self):
        print(f'\nEstos son todos los libros que hay en la biblioteca {self.nombre}:\n')
        for libro in self.inventario:
            self.mostrar_libro(libro)











