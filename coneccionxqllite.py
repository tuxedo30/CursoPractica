import sqlite3

def Crear_BaseDatos():
    try:
        bd = sqlite3.connect('bd_usuarios.db')
        cursor = bd.cursor()

        creacion = '''CREATE TABLE IF NOT EXISTS bd_usuarios.usuarios(
            ID INT PRIMARY KEY NOT NULL,
            NOMBRE_USUARIO VARCHAR(50) NOT NULL,
            PASSWORD VARCHAR (50) NOT NULL,
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100)
            )'''   
        cursor.execute(creacion)  
        cursor.close()

    except sqlite3.OperationalError as Error:
        e = Error


