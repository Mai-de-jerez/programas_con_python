from zona_fit_db.cliente import Cliente
from zona_fit_db.cliente_dao import ClienteDAO

print('*** Clientes Zona Fit (GYM) ***')
opcion= None
while opcion != 5:
    print('''Menú:
    1. Listar clientes
    2. Agregar clientes
    3. Modificar clientes
    4. Eliminar cliente
    5. Salir''')
    opcion = int(input('Escribe tu opcion (1-5): '))
    if opcion == 1:
        clientes = ClienteDAO.seleccionar()
        print('\n*** Listado de Clientes ***')
        for cliente in clientes:
            print(cliente)
    elif opcion == 2:
        nombre_var = input('Escribe el nombre: ')
        apellido_var = input('Escribe el apellido: ')
        membresia_var = input('Escribe la membresia: ')
        cliente = Cliente(nombre=nombre_var, apellido=apellido_var,
                          membresia=membresia_var)
        clientes_insertados = ClienteDAO.insertar(cliente)
        print(f'Clientes insertados: {clientes_insertados}')
    elif opcion == 3:
        id_cliente_var = int(input('Escribe el id del cliente a modificar: '))
        nombre_var = input('Escribe el nombre: ')
        apellido_var = input('Escribe el apellido: ')
        membresia_var = input('Escribe la membresia: ')
        cliente = Cliente(id_cliente_var, nombre_var, apellido_var, membresia_var)
        clientes_actualizados = ClienteDAO.actualizar(cliente)
        print(f'Clientes actualizados: {clientes_actualizados}')
    elif opcion == 4:
        id_cliente_var = int(input('Escribe el id del cliente a eliminar: '))
        cliente = Cliente(id=id_cliente_var)
        clientes_eliminados = ClienteDAO.eliminar(cliente)
        print(f'Clientes eliminados: {clientes_eliminados}')
else:
    print('Salimos de la app.')


