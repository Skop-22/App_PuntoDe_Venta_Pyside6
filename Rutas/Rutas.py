from qfluentwidgets import (FluentWindow, FluentIcon,
                            setTheme, Theme)
from PySide6.QtWidgets import QApplication
import sys

#  ------------> Ventana Ventanas
#    -> Vendedor
from GUI.Ventanas.Vendedor.ui_Vendedor import *
from GUI.Ventanas.Vendedor.ui_productos_vendedor import *

#    -> Clientes
from GUI.Ventanas.Cliente.ui_Cliente import *

#  ------------> Funsionalidad de las ventanas
#    -> Vendedor
from FunWin.Vendedor.HomeVendedor import *
from FunWin.Vendedor.ProductosVendedor import *

#    -> Cliente
from FunWin.Cliente.HomeCliente import *



