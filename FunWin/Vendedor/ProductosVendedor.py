from Rutas.Rutas import *

class ProductosVendedor(Ui_productos_vendedor, QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.busqueda()
    
    def busqueda(self):
        self.muestra = [[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]
        self.TableWidget.verticalHeader().hide()
        self.TableWidget.setRowCount(len(self.muestra))
        for x,dato in enumerate(self.muestra):
            for y,valor in enumerate(dato):
                self.TableWidget.setItem(x,y,QTableWidgetItem(str(valor)))

