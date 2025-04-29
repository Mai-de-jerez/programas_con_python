class Empleado:
    # Atributo de clase
    contador_empleados = 0

    def __init__(self, nombre, departamento):
        # Incrementamos el valor del atributo de clase
        Empleado.contador_empleados += 1
        self.id = Empleado.contador_empleados
        self.nombre = nombre
        self.departamento = departamento



    @classmethod
    def obtener_total_empleados(cls):  # class
        return cls.contador_empleados

