from Rutas.Rutas import *

class ProductosVendedor(Ui_productos_vendedor, QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
