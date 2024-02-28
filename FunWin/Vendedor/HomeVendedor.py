from qfluentwidgets import widgets
from Rutas.Rutas import *

class HomeVendedor(Ui_HomeVendedor,QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        widgetProduc = widgets
        self.windgetProduc(widgetProduc)

    def windgetProduc(self,widgets):
        print(widgets)
        for i in range(11):
            widget = BodyLabel(f"Widget {i+1}")
            widget.setAlignment(Qt.AlignCenter)#alinia al centro
            self.gridLayout.addWidget(widget, i // 4, i % 4)        
