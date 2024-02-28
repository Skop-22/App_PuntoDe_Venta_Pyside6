from qfluentwidgets import (
                            FluentWindow, 
                            FluentIcon,
                            setTheme, 
                            Theme, 
                            LineEdit, 
                            SearchLineEdit,
                            BodyLabel

)
from PySide6.QtWidgets import QApplication
import sys

#  ------------> Ventana Ventanas
#    -> Vendedor
from GUI.Ventanas.Vendedor.ui_Home_Vendedor import *
from GUI.Ventanas.Vendedor.ui_productos_vendedor import *

#  ------------> Funsionalidad de las ventanas
#    -> Vendedor
from FunWin.Vendedor.HomeVendedor import *
from FunWin.Vendedor.ProductosVendedor import *

