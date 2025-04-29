from InventarioProductos_db.conexion import Conexion
from InventarioProductos_db.Producto import Producto

class GestionInventario:
    INSERTAR = 'INSERT INTO productos (Nombre, Cantidad, Precio, Categoria) VALUES(%s, %s, %s, %s)'
    MOSTRAR = 'SELECT * FROM productos'
    BUSCAR = 'SELECT * FROM productos WHERE Nombre=%s'
    ACTUALIZAR = 'UPDATE productos SET Cantidad=%s, Precio=%s, Categoria=%s WHERE Nombre=%s'
    ELIMINAR = 'DELETE FROM productos WHERE Nombre=%s'

    @classmethod
    def insertar(cls, producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.nombre, producto.cantidad, producto.precio, producto.categoria)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al insertar un producto: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


    @classmethod
    def mostrar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.MOSTRAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla productos
            productos = []
            for registro in registros:
                producto = Producto(registro[0], registro[1],
                                  registro[2], registro[3])
                productos.append(producto)
            return productos
        except Exception as e:
            print(f'Ocurrió un error al mostrar productos: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def buscar(cls, producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.nombre,)
            cursor.execute(cls.BUSCAR, valores)
            registro = cursor.fetchone()
            if registro:
                producto_encontrado = Producto(registro[0], registro[1], registro[2], registro[3])
                return producto_encontrado
            else:
                return None
        except Exception as e:
            print(f'Ocurrió un error al buscar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


    @classmethod
    def actualizar(cls, producto, campo, nuevo_valor):
        conexion = None
        try:
            if campo not in ['Cantidad', 'Precio', 'Categoria']:
                print('Campo no válido para actualización.')
                return 0

            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            consulta = f"UPDATE productos SET {campo} = %s WHERE Nombre = %s"
            valores = (nuevo_valor, producto.nombre)
            cursor.execute(consulta, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al actualizar el producto: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)



    @classmethod
    def eliminar(cls, producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.nombre,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al eliminar un producto: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


if __name__ == '__main__':
    # Actualizar un producto




    producto_actualizar = Producto(nombre='Champú')  # Solo el nombre del producto es necesario
    campo = 'Cantidad'  # Campo que vamos a actualizar (puede ser 'cantidad', 'precio' o 'categoria')
    nuevo_valor = 7  # Nuevo valor del campo
    productos_actualizados = GestionInventario.actualizar(producto_actualizar, campo, nuevo_valor)
    print(f'Productos actualizados: {productos_actualizados}')

    # Insertar productos
    # producto1= Producto(nombre='Miel', cantidad=3, precio=3.99, categoria='Alimentación')
    # productos_insertados = GestionInventario.insertar(producto1)
    # print(f'Productos insertados: {productos_insertados}')

    # Eliminar un producto
    # producto_eliminar = Producto(nombre='Miel')
    # productos_eliminados = GestionInventario.eliminar(producto_eliminar)
    # print(f'Productos eliminados: {productos_eliminados}')

    # Mostrar los productos
    # productos = GestionInventario.mostrar()
    # for producto in productos:
    #   print(producto)

    # Buscar un producto
    # producto_buscar = Producto(nombre='Champú')
    # producto_buscado = GestionInventario.buscar(producto_buscar)
    # print(f'Producto buscado: \n{producto_buscado}')


