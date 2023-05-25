from GUI.GUIMens.ui_Mensage_Tex import *

class MensageTex(QDialog):
    def __init__(self,paret=None):
        QDialog.__init__(self,paret)
        self.MensT = Ui_MensageCon()
        self.MensT.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.MensT.pushButton_2.clicked.connect(lambda: self.close())
        self.MensT.pushButton_3.clicked.connect(lambda: self.PasswordUser())
        self.MensT.label_2.setText("Favor de incertar su \ncontraseña")
        self.contra=0
        with open("CSS/styles2.css","r") as f:
            self.setStyleSheet(f.read())

    def PasswordUser(self):
        self.contra=self.MensT.lineEdit.text()
        self.MensT.lineEdit.clear()
        self.close()
    
    def MensAccep(self,Titulo,texto):
        self.MensT.stackedWidget.setCurrentIndex(1)
        self.MensT.label_2.setText(Titulo)
        self.MensT.label.setText(texto)
        pass
