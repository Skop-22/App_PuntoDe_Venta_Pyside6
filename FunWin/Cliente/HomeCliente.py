from Rutas.Rutas import *

class HomeCliente(Ui_VentanaCliente,QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
