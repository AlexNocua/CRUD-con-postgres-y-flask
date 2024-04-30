from psycopg2 import connect

HOST = 'localhost'
PORT = 5432 #tu puerto
BD = 'DB_personas'
USUARIO = 'postgres'
PASSWORD = '' #tu contraseña




def EstablecerConexion():

    try:
        conexion = connect(host=HOST, port=PORT, dbname=BD, user=USUARIO, password=PASSWORD)
    except ConnectionError:
        print('Error de conexion')

    return conexion
