from Sistema_empleados.Clase_Empleado import Empleado
from Sistema_empleados.Clase_Empresa import Empresa

print('*** Sistema de Empleados ***')

# Crear una instancia de una empresa
empresa1 = Empresa('Mi Empresa')

# Contratar algunos empleados
empresa1.contratar_empleado('Juan', 'Ventas')
empresa1.contratar_empleado('María', 'Marketing')
empresa1.contratar_empleado('Pedro', 'Ventas')
empresa1.contratar_empleado('Ana', 'Recursos Humanos')

# Obtener el numero total de empleados de la empresa creada
print(f'Total de empleados en la empresa: {Empleado.obtener_total_empleados()}')

# Obtener el numero de empleados en el departamento de Ventas
print(f'Empleados en el departamento de Ventas: '
      f'{empresa1.obtener_num_emp_por_dept('Ventas')}')

# Mostrar todos los empleados de la empresa
empresa1.mostrar_todos_los_empleados()