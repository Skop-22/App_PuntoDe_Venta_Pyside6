from GUI.ui_untitled import *
from FunWindow.Mens import Mensage
from FunWindow.MensPas import MensageTex
from PySide6 import QtCore
from DataBase.coneccion import insertar, BuscarUser, Actuali 
from PySide6.QtGui import QColor
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QParallelAnimationGroup

class UsuarioGUI(QDialog):
    def __init__(self,parent=None):
        QDialog.__init__(self,parent)
        self.prin = Ui_UsuarioGUI()
        self.prin.setupUi(self) 
        self.Mens=Mensage()
        self.MenTex=MensageTex()#manda a llamar al wiget mensage de texto
        #---------------------
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #--------------------
        self.prin.pushButton_3.clicked.connect(lambda: self.animatio2())
        self.prin.pushButton_6.clicked.connect(lambda: self.animation())
        self.prin.pushButton_5.clicked.connect(lambda: self.AgregarUseario())
        self.prin.pushButton_2.clicked.connect(lambda: self.BuscarUsuario())
        self.prin.pushButton_10.clicked.connect(lambda: self.CerrarSesion())
        self.prin.pushButton_7.clicked.connect(lambda: self.ModificarInfoDelUser())
        self.prin.pushButton_8.clicked.connect(lambda: self.CancelarACTU())
        self.prin.pushButton_11.clicked.connect(lambda: self.cerrarVentana())
        self.prin.pushButton_9.clicked.connect(lambda: self.ActuliUser())
        self.prin.comboBox_2.currentTextChanged.connect(lambda: self.Estilos())
        self.prin.pushButton_2.setDefault(True)
        self.data=0
        with open("CSS/styles.css","r") as f:
            self.setStyleSheet(f.read())

    def AgregarUseario(self): 
        Nombre= self.prin.lineEdit_3.text()
        user= self.prin.lineEdit_4.text()
        contra =self.prin.lineEdit_5.text()
        valContra =self.prin.lineEdit_6.text()
        Tipo= self.prin.comboBox.currentText()
        if Nombre=="" or user == "" or contra == "" or valContra == "" or Tipo == "":
            self.Mens.Titulo("Error","Falta llenar un campo")
            self.Mens.exec()
        elif contra != valContra:
            self.Mens.Titulo("Error","Contraseña no es la misma")
            self.Mens.exec()
        else:
            if insertar((Nombre,user,contra,Tipo)):
                self.Mens.Titulo(" Informacion ", "Informacion guardada del usuario")
                self.Mens.exec()
            else: 
                self.Mens.Titulo(" Error ", "El usuario ya existe")
                self.Mens.exec()
        self.prin.lineEdit_3.clear()
        self.prin.lineEdit_4.clear()
        self.prin.lineEdit_5.clear()
        self.prin.lineEdit_6.clear()

    def Estilos(self):
        if self.prin.comboBox_2.currentText()=="Estilo clasico":
            with open("CSS/styles.css","r") as f:
                self.setStyleSheet(f.read())
        else:
            with open("CSS/styles2.css","r") as f:
                self.setStyleSheet(f.read())

    def BuscarUsuario(self):
        user= self.prin.lineEdit.text()
        contra= self.prin.lineEdit_2.text()
        self.data=BuscarUser(user)
        if self.data!=None:
            if contra == self.data[2] and user == self.data[1]:
                self.prin.lineEdit.clear()
                self.prin.lineEdit_2.clear()
                self.Mens.Titulo("Bienvenida","Bienvenido user "+user)
                self.Mens.exec()
                self.infoActualiUser(user)
                if self.data[3]=="Vendedor":
                    self.prin.comboBox_3.setCurrentIndex(0)
                else:
                    self.prin.comboBox_3.setCurrentIndex(1)
                self.prin.stackedWidget.setCurrentIndex(2)
                self.close()
            elif contra != self.data[2]:
                self.Mens.Titulo("Error","La contraseña es incorrecta")
                self.Mens.exec()
        else:
            self.Mens.Titulo("error","el usuario no existe")
            self.Mens.exec()
            self.data=0
            

    def infoActualiUser(self,user):
        self.data=BuscarUser(user)
        self.prin.label_11.setText(self.data[0])
        self.prin.lineEdit_7.setText(self.data[0])
        self.prin.label_12.setText(self.data[1])
        self.prin.lineEdit_8.setText(self.data[1])
        self.prin.lineEdit_10.setText(self.data[2])
        self.prin.lineEdit_9.setText(self.data[2])
        self.prin.label_13.setText(self.data[3])


    def animation(self):
        self.prin.stackedWidget.setCurrentIndex(0)
        self.animationWidget(self.prin.page,250,(400,0,368,478),(0,0,368,478),False,False,'geometry')

    def animatio2(self):
        self.prin.stackedWidget.setCurrentIndex(1)
        self.animationWidget(self.prin.page_2,250,(-400,0,368,478),(0,0,368,478),False,False,'geometry')

    def animationWidget(self,Widget,Duracion,posIni,posEnd,Curva,grupo,tipoDeAnimacion):
        if tipoDeAnimacion=='geometry':
            self.Animacion= QPropertyAnimation(Widget, b'geometry')
            self.Animacion.setStartValue(QRect(posIni[0],posIni[1],posIni[2],posIni[3]))
            self.Animacion.setEndValue(QRect(posEnd[0],posEnd[1],posEnd[2],posEnd[3]))
        elif tipoDeAnimacion=='color':
            self.Animacion =QPropertyAnimation(Widget, b'palette')
            self.Animacion.setStartValue(QColor(posIni[0],posIni[1],posIni[2]))
            self.Animacion.setEndValue(QColor(posEnd[0],posEnd[1],posEnd[2]))
            pass
        elif tipoDeAnimacion=='maximumWidth':
            self.Animacion =QPropertyAnimation(Widget, b'maximumWidth')
            self.Animacion.setStartValue(posIni)
            self.Animacion.setEndValue(posEnd)
        if Curva:
            self.Animacion.setEasingCurve(QEasingCurve.OutElastic)
            self.Animacion.setDuration(Duracion)
        else:
            self.Animacion.setDuration(Duracion)
        
        if grupo:
            return self.Animacion
        else:
            self.Animacion.start()

    def CerrarSesion(self):
        self.prin.stackedWidget.setCurrentIndex(0)
        self.data= 0
        self.close()

    def ModificarInfoDelUser(self):
        self.MenTex.MensT.stackedWidget.setCurrentIndex(0)
        self.MenTex.exec()
        if self.MenTex.contra != 0 and self.MenTex.contra != '':
            if self.MenTex.contra==self.data[2]:
                self.AnimacionEnGrupo=QParallelAnimationGroup()
                init=(0,0,362,264)
                fin=(0,0,0,264)
                self.AnimacionEnGrupo.addAnimation(self.animationWidget(self.prin.frame_4,250,init,fin,False,True,'geometry'))
                init=(362,0,0,264)
                fin=(0,0,362,264)
                self.AnimacionEnGrupo.addAnimation(self.animationWidget(self.prin.frame_5,250,init,fin,False,True,'geometry'))
                self.AnimacionEnGrupo.start()
            else:
                self.Mens.Titulo("  ¡Error! ","La contraseña es incorrecta")
                self.Mens.exec()
        else:
            self.Mens.Titulo("  ¡Error! ","La contraseña es incorrecta")
            self.Mens.exec()
        self.MenTex.contra=0


    def ActuliUser(self):
        Nombre=self.prin.lineEdit_7.text()
        user=self.prin.lineEdit_8.text()
        contra=self.prin.lineEdit_10.text()
        Valicontra=self.prin.lineEdit_9.text()
        tipo=self.prin.comboBox_3.currentText()
        if (Nombre==self.data[0])and(user==self.data[1])and(contra==self.data[2])and(tipo==self.data[3]):
            self.Mens.Titulo("Advertencia"," los datos son iguales")
            self.Mens.exec()
            return 
        elif contra==Valicontra:
            if Actuali(user,(Nombre,user,contra,tipo)):
                self.infoActualiUser(user)
                self.Mens.Titulo("  ¡Actualización! ","Actualizacion generada")
                self.Mens.exec()
                self.CancelarACTU()
            else:
                self.Mens.Titulo("  ¡Error!","Ubo un error al actulizar los datos")
                self.Mens.exec()
            pass

    def CancelarACTU(self):
        self.AnimacionEnGrupo=QParallelAnimationGroup()
        self.AnimacionEnGrupo.addAnimation(self.animationWidget(self.prin.frame_5,250,(0,0,362,264),(362,0,0,264),False,True,'geometry'))
        self.AnimacionEnGrupo.addAnimation(self.animationWidget(self.prin.frame_4,250,(0,0,0,264),(0,0,362,264),False,True,'geometry'))
        self.AnimacionEnGrupo.start()

    def cerrarVentana(self):
        if self.prin.frame_5.x() == 0:
            self.CancelarACTU()
        self.close()
