# Actualizar registros de Python a MySQL
import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost', # 127.0.0.1
    user = 'root',
    password = 'nemrac1985',
    database = 'personas_db'
)

# ejecutar la sentencia update
cursor = personas_db.cursor()
sentencia_sql = 'UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s'
valores = ('Victoria', 'Flores', 45, 6)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print('Se ha modificado la información...')
cursor.close()
personas_db.close()
