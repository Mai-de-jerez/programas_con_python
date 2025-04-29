from InventarioProductos_db.Producto import Producto
from InventarioProductos_db.GestionInventario import GestionInventario

print('*** Inventario Productos ***')
opcion = None
while opcion != 6:
    print('''\nMenú:
    1. Mostrar productos
    2. Agregar productos
    3. Actualizar productos
    4. Buscar un producto
    5. Eliminar un producto
    6. Salir''')

    try:
        opcion = int(input('Escribe tu opcion (1-6): '))
        if opcion not in [1, 2, 3, 4, 5, 6]:
            print("Opción no válida, por favor elige una opción entre 1 y 6.")
            continue
    except ValueError:
        print("Opción no válida, por favor ingresa un número.")
        continue

    if opcion == 1:
        productos = GestionInventario.mostrar()
        print('\n*** Listado de Productos ***')
        for producto in productos:
            print(producto)

    elif opcion == 2:
        nombre_var = input('Escribe el nombre: ')
        while True:
            producto_existente = GestionInventario.buscar(Producto(nombre=nombre_var))
            if producto_existente is not None:
                print("Error: El producto con este nombre ya existe. Por favor, ingresa un nombre diferente.")
                nombre_var = input('Escribe el nombre: ')
            else:
                break
        while True:
            try:
                cantidad_var = int(input('Escribe la cantidad: '))
                break
            except ValueError:
                print("Error: La cantidad debe ser un número entero.")
        while True:
            try:
                precio_var = float(input('Escribe el precio: '))
                break
            except ValueError:
                print("Error: El precio debe ser un número válido (por ejemplo, 3.99).")

        categoria_var = input('Escribe la categoría: ')
        producto = Producto(nombre=nombre_var, cantidad=cantidad_var,
                            precio=precio_var, categoria=categoria_var)
        productos_insertados = GestionInventario.insertar(producto)
        print(f'Productos insertados: {productos_insertados}')

    elif opcion == 3:
        nombre_var = input('Escribe el nombre del producto a actualizar: ')
        producto = Producto(nombre=nombre_var)
        producto_buscado = GestionInventario.buscar(producto)

        if producto_buscado is None:
            print('Error: Producto no encontrado en la base de datos.')
        else:
            print(f'Producto encontrado: {producto_buscado}')
            campo = input('Escribe el campo a actualizar (Cantidad, Precio, Categoria): ')
            if campo not in ['Cantidad', 'Precio', 'Categoria']:
                print('Campo no válido para actualización.')
            else:
                nuevo_valor = input(f'Escribe el nuevo valor para {campo}: ')

                try:
                    if campo == 'Cantidad':
                        while True:
                            try:
                                nuevo_valor = int(nuevo_valor)
                                if nuevo_valor < 0:
                                    print("Error: La cantidad no puede ser negativa.")
                                else:
                                    break
                            except ValueError:
                                print("Error: La cantidad debe ser un número entero.")
                                nuevo_valor = input(f'Escribe el nuevo valor para {campo}: ')
                    elif campo == 'Precio':
                        while True:
                            try:
                                nuevo_valor = float(nuevo_valor)
                                if nuevo_valor <= 0:
                                    print("Error: El precio debe ser mayor que 0.")
                                else:
                                    break
                            except ValueError:
                                print("Error: El precio debe ser un número válido.")
                                nuevo_valor = input(f'Escribe el nuevo valor para {campo}: ')
                    elif campo == 'Categoria':
                        break
                except ValueError:
                    print(f"Error: El valor para {campo} debe ser un número válido.")
                    continue

                productos_actualizados = GestionInventario.actualizar(producto_buscado, campo, nuevo_valor)
                if productos_actualizados > 0:
                    print(f'Producto(s) actualizado(s): {productos_actualizados} fila(s) modificada(s).')
                else:
                    print('Error al actualizar el producto.')


    elif opcion == 4:
        nombre_var = input('Escribe el nombre del producto a buscar: ')
        producto = Producto(nombre=nombre_var)
        producto_buscado = GestionInventario.buscar(producto)
        print(f'Producto buscado: \n{producto_buscado}')

    elif opcion == 5:
        nombre_var = input('Escribe el nombre del producto a eliminar: ')
        producto = Producto(nombre=nombre_var)
        productos_eliminados = GestionInventario.eliminar(producto)
        print(f'Productos eliminados: {productos_eliminados}')

else:
    print('Salimos de la app.')
