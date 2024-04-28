import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from datetime import datetime
from Controller.empleadocontroller import empleadocontroller
from View.validaciones import validaciones

class empleadoEditarView(QWidget):
    
    def __init__(self):
        super().__init__()
        uic.loadUi("View/GUI/empleadoeditar.ui",self)
        self.chkestado.setEnabled(False)
        self.empleadocontroller = empleadocontroller()
        self.validaciones = validaciones()
        self.cargarcombodepartamento()
        self.hoy = datetime.now().date()
        self.txtcedula.setValidator(QtGui.QIntValidator())
        self.txttelefono.setValidator(QtGui.QIntValidator())
        #self.txttelefono.setValidator(QtGui.QDoubleValidator())
        self.datenacimiento.setDate(self.hoy)
        self.datenacimiento.dateChanged.connect(self.calcularedad)
        #self.btnguardar.clicked.connect(self.guardar)
        self.btnlimpiar.clicked.connect(self.limpiar)
        self.btncerrar.clicked.connect(self.close)

    def cargarcombodepartamento(self):
        departamentos = self.empleadocontroller.obtenerdepartamento()
        if departamentos != None:
            for x in range(len(departamentos)):
                self.cbxdepartamento.addItem(departamentos[x]['nombre'])

    def calcularedad(self):
        anioactual = datetime.now().date().year
        mesactual = datetime.now().date().month
        diaactual = datetime.now().date().day

        fecha = self.datenacimiento.date().toPyDate()
        anionacimiento = fecha.year
        mesnacimiento  = fecha.month
        dianacimiento  = fecha.day

        if mesactual >= mesnacimiento and diaactual >= dianacimiento:
            edad = anioactual - anionacimiento
        else:
            edad = anioactual - anionacimiento
            edad = edad - 1
        self.spbedad.setValue(edad)

    def validarformulario(self):
        numobservaciones = 0
        observaciones = "Por favor revise lo siguiente: "

        #Cedula
        cedula = self.validaciones.fn_validar_cedulanatural(self.txtcedula)
        if cedula == None:
            observaciones = observaciones + "\nIngrese el número de cédula o RUC"
            numobservaciones+=1
        elif cedula == False:
            observaciones = observaciones + "\nCédula inválida"
            numobservaciones+=1

        #Nombre
        nombres = self.validaciones.fn_validar_nombre(self.txtnombre)
        if nombres == None:
            observaciones = observaciones + "\nIngrese Nombres del empleado"
            numobservaciones+=1
        elif nombres == False:
            observaciones = observaciones + "\nNombres del empleado son incorrectos"
            numobservaciones+=1

        #Telefono
        telefono = self.validaciones.fn_validar_telefono(self.txttelefono)
        if telefono == None:
            observaciones = observaciones + "\nIngrese telefono del empleado"
            numobservaciones+=1
        elif telefono == False:
            observaciones = observaciones + "\nTelefono del empleado son incorrectos"
            numobservaciones+=1

        #Correo
        email = self.validaciones.fn_validar_email(self.txtcorreo)
        if email == None:
            observaciones = observaciones + "\nIngrese email del empleado"
            numobservaciones+=1
        elif email == False:
            observaciones = observaciones + "\nemail del empleado son incorrectos"
            numobservaciones+=1

        #Sexo
        if self.rbmasculino.isChecked() == False and self.rbfemenino.isChecked() == False and self.rbninguno.isChecked() == False:
                observaciones = observaciones + "\nSeleccione el sexo del empleado"
                numobservaciones+=1

        if numobservaciones == 0:
            return True
        else:
            msgbox = QMessageBox()
            msgbox.setIcon(QMessageBox.Warning)
            msgbox.setWindowTitle("Datos Incorrectos")
            msgbox.setText(observaciones + "\nErrores a corregir: "+ str(numobservaciones))
            msgbox.exec()
            return False
        
    def cargarformulario(self,id):
        empleado = self.empleadocontroller.obtenerempleadoxid(id)

        self.txtcedula.setText(empleado['cedula'])
        self.txtnombre.setText(empleado['nombre'])
        self.txttelefono.setText(empleado['telefono'])
        self.txtcorreo.setText(empleado['correo'])
        self.datenacimiento.setDate(empleado['fecha_nacimiento'])
        if empleado['inicial_sexo'] == "M":
            self.rbmasculino.setChecked(True)
        elif empleado['inicial_sexo'] == "F":
            self.rbfemenino.setChecked(True)
        else:
            self.rbninguno.setChecked(True)
        self.spbedad.setValue(empleado['edad'])
        self.cbxdepartamento.setCurrentIndex(empleado['id_departamento']-1)
        self.spbsueldo.setValue(empleado['sueldo'])
        self.chkestado.setChecked(empleado['estado'])


    def guardar(self,id):
        validado = self.validarformulario()
        if validado == True:
            empleado = {}
            empleado['cedula'] = self.txtcedula.text()
            empleado['nombre'] = self.txtnombre.text()
            empleado['telefono'] = self.txttelefono.text()
            empleado['correo'] = self.txtcorreo.text()
            empleado['fechanacimiento'] = self.datenacimiento.date().toString('yyyy-MM-dd')
            if self.rbmasculino.isChecked() == True:
                empleado['sexo'] = "M"
            elif self.rbfemenino.isChecked() == True:
                empleado['sexo'] = "F"
            else:
                empleado['sexo'] = "N/A"
            empleado['edad'] = self.spbedad.value()
            empleado['strdepartamento'] = self.cbxdepartamento.currentText()
            empleado['indexdepartamento'] = self.cbxdepartamento.currentIndex() + 1
            empleado['sueldo'] = self.spbsueldo.value()
            empleado['estado'] = self.chkestado.isChecked()

            if id == None or id == 0:
                self.empleadocontroller.insertarempleado(empleado)
                titulomensaje = "Guaradado"
                mensaje = "Empleado guardado correctamente"
            else:
                empleado['id'] = id
                self.empleadocontroller.editarempleado(empleado)
                titulomensaje = "Modificado"
                mensaje = "Empleado "+ empleado['nombre'] +" modificado correctamente."

            msgbox = QMessageBox()
            msgbox.setIcon(QMessageBox.Information)
            msgbox.setWindowTitle(titulomensaje)
            msgbox.setText(mensaje)
            msgbox.exec()

            self.limpiar()

            self.close()


    def limpiar(self):
        self.txtcedula.setText("")
        self.txtnombre.setText("")
        self.txttelefono.setText("")
        self.txtcorreo.setText("")
        self.datenacimiento.setDate(self.hoy)
        self.rbmasculino.setChecked(False)
        self.rbfemenino.setChecked(False)
        self.spbedad.setValue(0)
        self.cbxdepartamento.setCurrentIndex(0)
        self.spbsueldo.setValue(0)
        self.chkestado.setChecked(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = empleadoEditarView()
    GUI.show()
    sys.exit(app.exec_())