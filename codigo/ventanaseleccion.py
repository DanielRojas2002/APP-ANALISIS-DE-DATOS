# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaSeleccionar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaSeleccionar(object):
    def setupUi(self, VentanaSeleccionar):
        VentanaSeleccionar.setObjectName("VentanaSeleccionar")
        VentanaSeleccionar.resize(897, 538)
        VentanaSeleccionar.setMinimumSize(QtCore.QSize(897, 538))
        VentanaSeleccionar.setMaximumSize(QtCore.QSize(897, 538))
        VentanaSeleccionar.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(VentanaSeleccionar)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(280, 20, 601, 491))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("multimedia/vector.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VentanaSeleccionar.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.frame_particular = QtWidgets.QFrame(self.centralwidget)
        self.frame_particular.setGeometry(QtCore.QRect(10, 10, 251, 511))
        self.frame_particular.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_particular.setObjectName("frame_particular")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_particular)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.dato = QtWidgets.QLineEdit(self.frame_particular)
        self.dato.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dato.setAlignment(QtCore.Qt.AlignCenter)
        self.dato.setObjectName("dato")
        self.gridLayout.addWidget(self.dato, 7, 0, 1, 1)
        self.info = QtWidgets.QPushButton(self.frame_particular)
        self.info.setMaximumSize(QtCore.QSize(198, 285))
        self.info.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.info.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"    border:1.5px solid black;\n"
"}\n"
"")
        self.info.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("multimedia/info.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info.setIcon(icon)
        self.info.setObjectName("info")
        self.gridLayout.addWidget(self.info, 7, 1, 1, 1)
        self.atras = QtWidgets.QPushButton(self.frame_particular)
        self.atras.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.atras.setStyleSheet("QPushButton:hover{\n"
"    \n"
"    background-color: rgb(165, 175, 173);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.atras.setObjectName("atras")
        self.gridLayout.addWidget(self.atras, 0, 0, 1, 2)
        self.titulo = QtWidgets.QLabel(self.frame_particular)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.gridLayout.addWidget(self.titulo, 1, 0, 1, 2)
        self.opciones = QtWidgets.QComboBox(self.frame_particular)
        self.opciones.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.opciones.setObjectName("opciones")
        self.opciones.addItem("")
        self.opciones.addItem("")
        self.gridLayout.addWidget(self.opciones, 2, 0, 1, 2)
        self.seleccionar = QtWidgets.QPushButton(self.frame_particular)
        self.seleccionar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seleccionar.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(255, 170, 0);\n"
"}")
        self.seleccionar.setObjectName("seleccionar")
        self.gridLayout.addWidget(self.seleccionar, 3, 0, 1, 2)
        self.imagen = QtWidgets.QLabel(self.frame_particular)
        self.imagen.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.imagen.setText("")
        self.imagen.setPixmap(QtGui.QPixmap("multimedia/buscar_registro.png"))
        self.imagen.setScaledContents(True)
        self.imagen.setObjectName("imagen")
        self.gridLayout.addWidget(self.imagen, 4, 0, 1, 2)
        self.opciones_2 = QtWidgets.QComboBox(self.frame_particular)
        self.opciones_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.opciones_2.setObjectName("opciones_2")
        self.gridLayout.addWidget(self.opciones_2, 6, 0, 1, 2)
        self.realizar = QtWidgets.QPushButton(self.frame_particular)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.realizar.setFont(font)
        self.realizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.realizar.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(255, 170, 0);\n"
"}")
        self.realizar.setObjectName("realizar")
        self.gridLayout.addWidget(self.realizar, 8, 0, 1, 2)
        self.generarinforme = QtWidgets.QPushButton(self.frame_particular)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.generarinforme.setFont(font)
        self.generarinforme.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generarinforme.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.generarinforme.setObjectName("generarinforme")
        self.gridLayout.addWidget(self.generarinforme, 9, 0, 1, 2)
        self.progressBar = QtWidgets.QProgressBar(self.frame_particular)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 5, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.frame_ventana = QtWidgets.QFrame(self.centralwidget)
        self.frame_ventana.setGeometry(QtCore.QRect(0, -10, 911, 551))
        self.frame_ventana.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_ventana.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ventana.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ventana.setObjectName("frame_ventana")
        self.frame_ventana.raise_()
        self.frame_particular.raise_()
        self.tableWidget.raise_()
        VentanaSeleccionar.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaSeleccionar)
        QtCore.QMetaObject.connectSlotsByName(VentanaSeleccionar)

    def retranslateUi(self, VentanaSeleccionar):
        _translate = QtCore.QCoreApplication.translate
        VentanaSeleccionar.setWindowTitle(_translate("VentanaSeleccionar", "Buscador de Registros"))
        self.dato.setPlaceholderText(_translate("VentanaSeleccionar", "Ingrese el dato a buscar "))
        self.atras.setText(_translate("VentanaSeleccionar", "<-"))
        self.titulo.setText(_translate("VentanaSeleccionar", "OPCIONES DE BUSQUEDA:"))
        self.opciones.setItemText(0, _translate("VentanaSeleccionar", "TODOS"))
        self.opciones.setItemText(1, _translate("VentanaSeleccionar", "Especifico"))
        self.seleccionar.setText(_translate("VentanaSeleccionar", "SELECCIONAR OPCION"))
        self.realizar.setText(_translate("VentanaSeleccionar", "BUSCAR"))
        self.generarinforme.setText(_translate("VentanaSeleccionar", "GENERAR CSV DE LA BUSQUEDA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaSeleccionar = QtWidgets.QMainWindow()
    ui = Ui_VentanaSeleccionar()
    ui.setupUi(VentanaSeleccionar)
    VentanaSeleccionar.show()
    sys.exit(app.exec_())
