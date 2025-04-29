import re
import os
from Contacto import Contacto

class GestionContactos:
    def __init__(self, archivo):
        self.contactos = []
        self.archivo = archivo
        self.cargar_contactos()

    def cargar_contactos(self):
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r', encoding='utf-8') as f:
                    for linea in f:
                        nombre, telefono, email = linea.strip().split(',')
                        self.contactos.append(Contacto(nombre, telefono, email))
        except Exception as e:
            print(f"Error al cargar contactos: {e}")

    def guardar_contactos(self):
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                for contacto in self.contactos:
                    f.write(f"{contacto.nombre},{contacto.telefono},{contacto.email}\n")
        except Exception as e:
            print(f"Error al guardar contactos: {e}")

    def agregar_contacto(self, nombre, telefono, email):
        # Verificar si los campos no están vacíos
        if not nombre or not telefono or not email:
            print("Los campos no pueden estar vacíos.")
            return

        # Validar email
        patron_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(patron_email, email):
            print("Formato de correo electrónico inválido.")
            return

        # Validar nombre (solo letras)
        if not nombre.isalpha():
            print("El nombre solo puede contener letras.")
            return

        # Validar teléfono (solo números)
        if not telefono.isdigit():
            print("El teléfono solo puede contener números.")
            return

        self.contactos.append(Contacto(nombre, telefono, email))
        self.guardar_contactos()
        print("Contacto agregado correctamente.")

    def mostrar_contactos(self):
        print('\n*** Listado de contactos ***')
        if not self.contactos:
            print("No hay contactos para mostrar.")
            return
        for contacto in self.contactos:
            print(contacto)

    def buscar_contacto(self, nombre):
        # Buscar el contacto por nombre
        encontrados = [contacto for contacto in self.contactos if contacto.nombre.lower() == nombre.lower()]
        if encontrados:
            for contacto in encontrados:
                print(contacto)
        else:
            print("Contacto no encontrado.")

    def eliminar_contacto(self, nombre):
        encontrado = False
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto)
                self.guardar_contactos()
                print("Contacto eliminado correctamente.")
                encontrado = True
                break
        if not encontrado:
            print("Contacto no encontrado.")

