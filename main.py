from Rutas.Rutas import *

class VentanaPrincipal (FluentWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(1080,650)
        self.setWindowTitle("Punto De Venta")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    app.exec()
