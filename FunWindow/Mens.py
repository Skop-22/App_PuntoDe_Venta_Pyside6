from GUI.GUIMens.ui_untitled import *
from PySide6.QtCore import QPropertyAnimation
from PySide6 import QtCore

class Mensage(QDialog):
    def __init__(self,parent=None):
        QDialog.__init__(self,parent)
        self.Prin = Ui_Dialog()
        self.Prin.setupUi(self)
        #----------------------------------
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #---------------------------------
        self.Prin.Cerrar.clicked.connect(lambda: self.close())
        with open("CSS/stylesMes.css","r") as f:
            self.setStyleSheet(f.read())

    def anima(self):
        self.Animacion= QPropertyAnimation(self.Prin.widget, b'geometry')
        self.Animacion.setDuration(200)
        self.Animacion.setStartValue(QRect(0,100,470,0))
        self.Animacion.setEndValue(QRect(0,0,470,200))
        self.Animacion.start()
        
    def Titulo(self,Titulo,Contexto):
        self.Prin.label.setText(Titulo)
        self.Prin.label_3.setText(Contexto)
        self.anima()
