from Rutas.Rutas import *

class HomeVendedor(Ui_HomeVendedor,QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.windgetProduc()

    def windgetProduc(self):
        for i in range(11):
            widget = BodyLabel(f"Widget {i+1}")
            widget.setStyleSheet(f"background-color : rgb(12{i//2},12{i//2},12{i//2});")
            widget.setAlignment(Qt.AlignCenter)#alinia al centro
            self.ordenadorProducto.addWidget(widget, i // 4, i % 4)        

    def widgetProducto(self):
        pass

    def productos(self):
        pass

