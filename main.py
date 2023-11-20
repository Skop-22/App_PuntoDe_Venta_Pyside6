from Rutas.Rutas import *

class VentanaPrincipal (FluentWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(900,560)
        self.setWindowTitle("Punto De Venta")
        self.menuCliente()

    #configuración de la interfas grafica del usuario tipo vendedor
    def menuVendedor(self):
        self.vendedor = HomeVendedor()
        self.addSubInterface(self.vendedor, FluentIcon.HOME_FILL, "Vendedor")

    #configuración de la interfas grafica del usuario tipo vendedor
    def menuCliente(self):
        self.cliente = HomeCliente()
        self.addSubInterface(self.cliente, FluentIcon.HOME_FILL, "Cliente")
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    app.exec()
