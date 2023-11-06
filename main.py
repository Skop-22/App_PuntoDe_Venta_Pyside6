from Rutas.Rutas import *

class VentanaPrincipal (FluentWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(900,560)
        self.setWindowTitle("Punto De Venta")
        self.menu()

    def menu(self):
        # -> modificar conforme a la session
        self.vendedor = HomeVendedor()
        self.addSubInterface(self.vendedor,FluentIcon.HOME_FILL,"Vendedor")
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    app.exec()
