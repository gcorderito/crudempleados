import sys
import os
import socket
import urllib.request
import platform
from datetime import datetime

myDir = os.getcwd()
sys.path.append(myDir)

from Database.conexion import conexion
from Model.empleado import empleado

class empleadocontroller():

    def __init__(self):
        self.empleado = empleado(conexion())

    def obtenerdepartamento(self):
        datos = self.empleado.getdepartamento()
        if len(datos) != 0:
            departamentos = []
            for x in range(len(datos)):
                departamento = {}
                departamento['id'] = datos[x][0]
                departamento['nombre'] = datos[x][1]
                departamentos.append(departamento)
        else:
            departamentos = None

        return departamentos
    
    def obtenerdepartamentoxid(self,id):
        datos = self.empleado.getdepartamentoxid(id)
        if datos != None:
            departamento = {}
            departamento['id'] = datos[0]
            departamento['nombre'] = datos[1]
        else:
            departamento = None

        return departamento
    
    def insertarempleado(self,empleado):
        datos = (empleado['cedula'],
                 empleado['nombre'],
                 empleado['telefono'],
                 empleado['correo'],
                 empleado['fechanacimiento'],
                 empleado['sexo'],
                 empleado['edad'],
                 empleado['indexdepartamento'],
                 empleado['sueldo'])
        self.empleado.insertarempleado(datos)

    def editarempleado(self,empleado):
        datos = (empleado['cedula'],
                 empleado['nombre'],
                 empleado['telefono'],
                 empleado['correo'],
                 empleado['fechanacimiento'],
                 empleado['sexo'],
                 empleado['edad'],
                 empleado['indexdepartamento'],
                 empleado['sueldo'],
                 empleado['id'])
        self.empleado.editarempleado(datos)

    def eliminarempleado(self,id):
        self.empleado.eliminarempleado(id)

    def obtenerempleadoxid(self,id):
        empleado = self.empleado.getempleadoxid(id)

        if empleado != None:
            datos = {}
            datos['id'] = empleado[0]
            datos['cedula'] = empleado[1]
            datos['nombre'] = empleado[2]
            datos['telefono'] = empleado[3]
            datos['correo'] = empleado[4]
            datos['fecha_nacimiento'] = empleado[5]
            datos['inicial_sexo'] = empleado[6]
            datos['edad'] = empleado[7]
            datos['id_departamento'] = empleado[8]
            datos['sueldo'] = empleado[9]
            datos['estado'] = empleado[10]
        else:
            datos = None

        return datos


    def obtenerempleados(self):
        empleados = self.empleado.getempleado()

        if empleados != None:
            datos = []
            for x in range(len(empleados)):
                empleado = {}
                empleado['id'] = empleados[x][0]
                empleado['cedula'] = empleados[x][1]
                empleado['nombre'] = empleados[x][2]
                empleado['telefono'] = empleados[x][3]
                empleado['correo'] = empleados[x][4]
                empleado['fecha_nacimiento'] = empleados[x][5]
                empleado['inicial_sexo'] = empleados[x][6]
                empleado['edad'] = empleados[x][7]
                empleado['id_departamento'] = empleados[x][8]
                empleado['sueldo'] = empleados[x][9]
                empleado['estado'] = empleados[x][10]
                
                departamento = self.obtenerdepartamentoxid(empleado['id_departamento'])
                if departamento != None:
                    empleado['departamento'] = departamento['nombre']
                else:
                    empleado['departamento'] = ""

                if empleado['inicial_sexo'] == "M":
                    empleado['sexo'] = "Masculino"
                elif empleado['inicial_sexo'] == "F":
                    empleado['sexo'] = "Femenino"
                else:
                    empleado['sexo'] = ""

                datos.append(empleado)
        else:
            datos = None

        return datos
    
    def obtenerempleadosxfiltro(self,cedula,nombre):
        empleados = self.empleado.getempleadoxfiltro(cedula,nombre)
        if empleados != None:
            datos = []
            for x in range(len(empleados)):
                empleado = {}
                empleado['id'] = empleados[x][0]
                empleado['cedula'] = empleados[x][1]
                empleado['nombre'] = empleados[x][2]
                empleado['telefono'] = empleados[x][3]
                empleado['correo'] = empleados[x][4]
                empleado['fecha_nacimiento'] = empleados[x][5]
                empleado['inicial_sexo'] = empleados[x][6]
                empleado['edad'] = empleados[x][7]
                empleado['departamento'] = empleados[x][8]
                empleado['sueldo'] = empleados[x][9]
                empleado['estado'] = empleados[x][10]

                if empleado['inicial_sexo'] == "M":
                    empleado['sexo'] = "Masculino"
                elif empleado['inicial_sexo'] == "F":
                    empleado['sexo'] = "Femenino"
                else:
                    empleado['sexo'] = ""

                datos.append(empleado)
        else:
            datos = None

        return datos

