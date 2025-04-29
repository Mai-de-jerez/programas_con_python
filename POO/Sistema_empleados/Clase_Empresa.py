from Sistema_empleados.Clase_Empleado import Empleado


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def contratar_empleado(self, nombre, departamento):
        empleado = Empleado(nombre, departamento)
        self.empleados.append(empleado)

    def obtener_num_emp_por_dept(self, departamento):
        contador_emp_por_dept = 0
        for empleado in self.empleados:
            if empleado.departamento == departamento:
                contador_emp_por_dept += 1
        return contador_emp_por_dept

    def mostrar_todos_los_empleados(self):
        print(f'\nTotal de empleados para la empresa: {self.nombre}\n')
        for empleado in self.empleados:
            print(f'''Empleado {empleado.id}
            Nombre: {empleado.nombre}
            Departamento: {empleado.departamento}''')