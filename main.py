from Rutas.Rutas import *

class VentanaPrincipal (FluentWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(900,560)
        self.setWindowTitle("Punto De Venta")
        self.menuVendedor()

    #configuración de la interfas grafica del usuario tipo vendedor
    def menuVendedor(self):
        self.vendedor = HomeVendedor()
        self.addSubInterface(self.vendedor, FluentIcon.HOME_FILL, "Vendedor")
        self.vendedor_productos = ProductosVendedor()
        self.addSubInterface(self.vendedor_productos, FluentIcon.SETTING, "Productos")

if __name__ == "__main__":
    setTheme(Theme.DARK)#tema 
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    app.exec()
