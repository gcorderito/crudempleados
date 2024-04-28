import psycopg2

def conexion():
    try:
        conn = psycopg2.connect(user='postgres',
                                password='postgres',
                                host='127.0.0.1',
                                port='5432',
                                database='empleado')
        
        return conn
    except:
        print("No se pudo conectar al servidor")