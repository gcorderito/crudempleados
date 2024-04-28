import re
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from datetime import datetime

class validaciones():

    def fn_validar_numero(self, txtbox):
        numero = txtbox.text()
        validar = re.match('^[0-9]+$', numero, re.I)
        if numero == "":
            txtbox.setStyleSheet("border: 1px solid yellow;")
            return None
        elif not validar:
            txtbox.setStyleSheet("border: 1px solid red;")
            return False
        else:
            txtbox.setStyleSheet("border: 1px solid green;")
            return True
        
    def fn_validar_nombre(self, txtbox):
        nombre = txtbox.text()
        validar = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', nombre, re.I)
        if nombre == "":
            txtbox.setStyleSheet("border: 1px solid yellow;")
            return None
        elif not validar:
            txtbox.setStyleSheet("border: 1px solid red;")
            return False
        else:
            txtbox.setStyleSheet("border: 1px solid green;")
            return True
        

    def fn_validar_cedulanatural(self,txtbox):
        ced = txtbox.text()
        validarced = re.match('^[0-9]{10,10}$', ced, re.I)
        validarruc = re.match('^[0-9]{13,13}$', ced, re.I)

        if ced == "":
            txtbox.setStyleSheet("border: 1px solid yellow;")
            return None
        elif not validarced and not validarruc:
            txtbox.setStyleSheet("border: 1px solid red;")
            return False
        elif self.cedularucnatural(ced) == False:
            txtbox.setStyleSheet("border: 1px solid red;")
            return False
        else:
            txtbox.setStyleSheet("border: 1px solid green;")
            return True
        

    def fn_validar_email(self, txtbox):
        email = txtbox.text()
        validar = re.match('^[a-zA-Z0-9\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}([.]{1}[a-zA-Z]{2}){0,3}$', email, re.I)
        if email == "":
            txtbox.setStyleSheet("border: 1px solid yellow;")
            return None
        elif not validar:
            txtbox.setStyleSheet("border: 1px solid red;")
            return False
        else:
            txtbox.setStyleSheet("border: 1px solid green;")
            return True
        
    def fn_validar_telefono(self, txtbox):
        telefono = txtbox.text()
        validar = re.match('^[0-9]{7,10}$', telefono, re.I)
        if telefono == "":
            txtbox.setStyleSheet("border: 1px solid yellow;")
            return None
        elif not validar:
            txtbox.setStyleSheet("border: 1px solid red;")
            return False
        else:
            txtbox.setStyleSheet("border: 1px solid green;")
            return True
        

    def cedularucnatural(self, cedula):
        if len(cedula) != 10 and len(cedula) != 13:
            return False
        else:
            if len(cedula) == 13:
                cedula = cedula[:10]#Obtengo los 10 primeros dígitos del RUC
            multiplicador = [2, 1, 2, 1, 2, 1, 2, 1, 2]
            ced_array = map(lambda k: int(k), list(cedula))
            ultimo_digito = int(cedula[9])
            resultado = []
            arr = map(lambda x, j: (x, j), ced_array, multiplicador)
            for (i, j) in arr:
                if i * j < 10:
                    resultado.append(i * j)
                else:
                    resultado.append((i * j)-9)
            if ultimo_digito == int(math.ceil(float(sum(resultado)) / 10) * 10) - sum(resultado):
                return True
            else:
                return False