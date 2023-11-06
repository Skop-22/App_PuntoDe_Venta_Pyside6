from Rutas.Rutas import *

class HomeVendedor(Ui_Vendedor,QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
