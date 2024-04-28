class empleado():

    def __init__(self,conn):
        self.conn = conn

    def getdepartamento(self):
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM departamento ORDER BY id ASC;"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        
    def getdepartamentoxid(self,id):
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM departamento WHERE id = %s ORDER BY id ASC;"
            cursor.execute(sql,[id])
            result = cursor.fetchone()
            return result
        
    def insertarempleado(self,empleado):
        with self.conn.cursor() as cursor:
            sql = ("INSERT INTO empleado("
                "cedula,"
                "nombre,"
                "telefono,"
                "correo, "
                "fecha_nacimiento, "
                "sexo, "
                "edad, "
                "id_departamento, "
                "sueldo)"
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);")
            cursor.execute(sql,empleado)
            self.conn.commit()

    def editarempleado(self,empleado):
        with self.conn.cursor() as cursor:
            sql=("UPDATE public.empleado SET "
                "cedula=%s,"
                "nombre=%s,"
                "telefono=%s,"
                "correo=%s,"
                "fecha_nacimiento=%s,"
                "sexo=%s,"
                "edad=%s,"
                "id_departamento=%s,"
                "sueldo=%s "
                "WHERE id=%s;")
            cursor.execute(sql,empleado)
            self.conn.commit()

    def eliminarempleado(self,id):
        with self.conn.cursor() as cursor:
            #sql = "DELETE FROM empleado WHERE id = %s"
            sql = "UPDATE empleado SET estado = false WHERE id = %s"
            cursor.execute(sql,[id])
            self.conn.commit()

    def getempleado(self):
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM empleado ORDER BY id ASC"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        
    def getempleadoxfiltro(self,cedula,nombre):
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM getempleado(%s,%s) WHERE estado = true"
            cursor.execute(sql,[cedula,nombre])
            result = cursor.fetchall()
            return result
        
    def getempleadoxid(self,id):
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM empleado WHERE id = %s;"
            cursor.execute(sql,[id])
            result = cursor.fetchone()
            return result