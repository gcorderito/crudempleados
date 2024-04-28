import sys, re
import os

myDir = os.getcwd()
sys.path.append(myDir)
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from View.empleadoEditarView import empleadoEditarView
from Controller.empleadocontroller import empleadocontroller

class empleadoView(QWidget):
    def __init__(self):
        super().__init__()
        #GUI = self
        uic.loadUi("View/GUI/empleado.ui",self)
        self.empleadocontroller = empleadocontroller()
        self.btnbuscar.clicked.connect(self.cargarempleados)
        self.btncancelar.clicked.connect(self.limpiar)
        self.btnnuevo.clicked.connect(self.nuevoempleado)
        self.btncerrar.clicked.connect(self.close)

    def cargarempleados(self):
        cedula = self.txtcedula.text()
        nombre = self.txtnombre.text()

        self.empleados = None
        self.empleados = self.empleadocontroller.obtenerempleadosxfiltro(cedula,nombre)

        if self.empleados != None:
            self.tblempleado.clearContents()
            row = 0
            self.tblempleado.setRowCount(len(self.empleados))

            for empleado in self.empleados:
                #Cedula
                self.tblempleado.setItem(row,0,QTableWidgetItem(empleado['cedula']))
                #Nombre
                self.tblempleado.setItem(row,1,QTableWidgetItem(empleado['nombre']))
                #Edad
                self.tblempleado.setItem(row,2,QTableWidgetItem(str(empleado['edad'])))
                #Departamento
                self.tblempleado.setItem(row,3,QTableWidgetItem(empleado['departamento']))
                #Editar
                self.btneditar = QtWidgets.QPushButton('Editar')
                self.btneditar.clicked.connect(lambda:self.editarempleado(self.empleados[self.tblempleado.currentRow()]['id']))
                self.tblempleado.setCellWidget(row,4,self.btneditar)
                #Eliminar
                self.btneliminar = QtWidgets.QPushButton('Eliminar')
                self.btneliminar.clicked.connect(lambda:self.eliminarempleado(self.empleados[self.tblempleado.currentRow()]['id']))
                self.tblempleado.setCellWidget(row,5,self.btneliminar)
                row+=1
        else:
            msgbox = QMessageBox()
            msgbox.setIcon(QMessageBox.Warning)
            msgbox.setWindowTitle("Empleado no encontrado")
            msgbox.setText("No se encontraron empleados con el número de cédula o nombre de empleado ingresado.")
            msgbox.exec()


    def limpiar(self):
        self.txtcedula.setText("")
        self.txtnombre.setText("")
        self.empleados = None
        self.tblempleado.clearContents()


    def nuevoempleado(self):
        self.empleadonuevoview = empleadoEditarView()
        self.empleadonuevoview.setWindowTitle("Nuevo Empleado")
        self.empleadonuevoview.btnguardar.clicked.connect(lambda:self.empleadonuevoview.guardar(None))
        self.empleadonuevoview.btnguardar.clicked.connect(self.cargarempleados)
        self.empleadonuevoview.show()

    def editarempleado(self,id):
        self.editarempleadoview = empleadoEditarView()
        self.editarempleadoview.setWindowTitle("Editar Empleado")
        self.editarempleadoview.cargarformulario(id)
        self.editarempleadoview.btnguardar.clicked.connect(lambda:self.editarempleadoview.guardar(id))
        self.empleadonuevoview.btnguardar.clicked.connect(self.cargarempleados)
        self.editarempleadoview.show()

    def eliminarempleado(self,id):
        respuesta = QMessageBox.warning(self, "Eliminar empleado", "¿Está seguro/a que desea eliminar el empleado?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if respuesta == QMessageBox.Yes:
            self.empleadocontroller.eliminarempleado(id)
            self.cargarempleados()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = empleadoView()
    GUI.show()
    sys.exit(app.exec_())
