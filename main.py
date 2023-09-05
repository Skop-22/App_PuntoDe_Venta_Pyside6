from FunWindow.AnimacionButton.animaButon import AnimaButtonHover
from FunWindow.User import UsuarioGUI
from FunWindow.Tiket import TiketWindow
from FunWindow.Mens import Mensage

from DataBase.coneccion import *

from GUI.ui_MenuPrin import *
from GUI.ICONS.ICONS_rc import *
# -------------------------------------------------------------------------------------------
from PySide6 import QtCore
from functools import partial
import sys


class WindowPrin(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.PrinWin = Ui_MainWindow()
        self.PrinWin.setupUi(self)
        self.user = UsuarioGUI()
        self.Ticket = TiketWindow()
        self.Aviso = Mensage()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # elimina el titulo
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # ---------------------------------------------------------------------------------------
        self.ID_venta = None  # id venta
        self.ListaDeButons = []  # lista de botones
        self.ListaDeWidgets = []  # lista de widgets
        self.ListaDeWidgetsMensaje = []
        self.dato = 0  # la informaión del usuario se guarda en esta variable
        self.contadorDeCompras = 0
        self.contadorDeMensjes = 0
        self.configcolor = [0, 0, 0, 0]
        self.Product = None
        # ---------------------------------------------------------------------------------------
        # funcion para el movimento de la ventana

        def moWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        # ---------------------------------------------------------------------------------------
        self.PrinWin.label.mouseMoveEvent = moWindow
        self.PrinWin.pushButton.clicked.connect(lambda: self.InfoDelUser())
        self.PrinWin.pushButton_3.clicked.connect(lambda: self.Maxi())
        self.PrinWin.pushButton_11.clicked.connect(lambda: self.guardarVenta())
        self.PrinWin.pushButton_12.clicked.connect(
            lambda: self.EliminarVen(self.PrinWin.pushButton_12))
        self.PrinWin.pushButton_13.clicked.connect(lambda: self.Ticket.exec())
        self.PrinWin.lineEdit.textChanged.connect(
            lambda: self.buscarProducto())
        self.PrinWin.tabWidget.currentChanged.connect(self.onChange)
        self.PrinWin.tabWidget.tabBarClicked.connect(
            lambda: self.ProductosComprados())
        self.PrinWin.Enviar.clicked.connect(lambda: self.Visualizacion())
        self.PrinWin.MenuCasa.clicked.connect(lambda: self.menu())
        self.Sliderconfig()
        # ---------------------------------------------------------------------------------------
        self.Ticket.Tiketwind.pushButton_4.clicked.connect(
            lambda: self.eliminarCompras())
        self.user.prin.pushButton_10.clicked.connect(
            lambda: self.eliminarCompras())
        self.user.prin.pushButton_10.clicked.connect(
            lambda: self.Ticket.elimiarCompras())
        self.Ticket.Tiketwind.pushButton_2.clicked.connect(
            lambda: self.eliminarCompras())
        self.Ticket.Tiketwind.pushButton_5.clicked.connect(
            lambda: self.AjusteDeContador())
        # se manda a llamar el metodo para crear la lista de los productos
        self.botonesDeProduct(self.PrinWin.Casa, None)
        # ----------------------------------------------------------
        with open("CSS/stylesMenuPrinw.css", "r") as f:
            # abre el archivo de estilos para el menu principal
            self.setStyleSheet(f.read())

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def Maxi(self):
        if self.isMaximized():
            self.iconba = QIcon()
            self.iconba.addFile(u":/ICONS/maximizar.png",
                                QSize(), QIcon.Normal, QIcon.Off)
            self.PrinWin.pushButton_3.setIcon(self.iconba)
            self.PrinWin.pushButton_3.setIconSize(QSize(30, 30))
            self.showNormal()
        else:
            self.iconba2 = QIcon()
            self.iconba2.addFile(u":/ICONS/cuadricula.png",
                                 QSize(), QIcon.Normal, QIcon.Off)
            self.PrinWin.pushButton_3.setIcon(self.iconba2)
            self.PrinWin.pushButton_3.setIconSize(QSize(30, 30))
            self.showMaximized()

    def onChange(self, i):
        if i == 0:
            self.botonesDeProduct(self.PrinWin.Casa, None)
        elif i == 1:
            if self.dato != 0:
                if self.dato[3] == "Vendedor":
                    self.botonesDeProduct(self.PrinWin.widget_6, None)
                elif self.dato[3] == "Cliente":
                    self.botonesDeProduct(self.PrinWin.frame_8, None)
            else:
                self.botonesDeProduct(self.PrinWin.frame_8, None)

    def AjusteDeContador(self):
        self.contadorDeCompras = len(self.Ticket.Lista)
        with open("CSS/stylesBoton.css", "r") as f:
            self.PrinWin.pushButton_13.setStyleSheet(
                f.read())  # estilos para el boton
        self.PrinWin.pushButton_13.setText(
            str(self.contadorDeCompras))  # visualizción de compras

    def eliminarCompras(self):
        self.dato = self.user.data
        self.ProductosComprados()
        self.contadorDeCompras = 0
        with open("CSS/stylesMenuPrinw.css", "r") as f:
            self.PrinWin.pushButton_13.setStyleSheet(f.read())
        self.PrinWin.pushButton_13.setText("")

    def InfoDelUser(self):  # para la tratar con la informacion del usuario
        self.user.exec()  # executa el widget para el usuario
        if self.dato != self.user.data:
            self.eliminarCompras()
            self.Ticket.elimiarCompras()
        self.dato = self.user.data  # gurda la informacion del usuario
        if self.dato != 0:
            self.PrinWin.pushButton.setText(self.dato[1])
            # si el usuario es un vendedor abre el menu para crear productos o eliminarlos
            if self.dato[3] == "Vendedor":
                self.PrinWin.stackedWidget.setCurrentIndex(1)
                self.PrinWin.pushButton_13.setEnabled(False)
                with open("CSS/stylesMenuPrinw.css", "r") as f:
                    self.PrinWin.pushButton_13.setStyleSheet(f.read())
                self.PrinWin.pushButton_13.setText("")
                if self.PrinWin.tabWidget.currentIndex() == 1:
                    self.botonesDeProduct(self.PrinWin.widget_6, None)
                else:
                    self.botonesDeProduct(self.PrinWin.Casa, None)
            # si el usuario es cliente abre la lista de productos
            elif self.dato[3] == "Cliente":
                self.PrinWin.stackedWidget.setCurrentIndex(0)
                if self.PrinWin.tabWidget.currentIndex() == 1:
                    self.botonesDeProduct(self.PrinWin.frame_8, None)
                else:
                    self.botonesDeProduct(self.PrinWin.Casa, None)
        else:
            self.PrinWin.stackedWidget.setCurrentIndex(0)
            if self.PrinWin.tabWidget.currentIndex() == 0:
                self.botonesDeProduct(self.PrinWin.Casa, None)
            elif self.PrinWin.tabWidget.currentIndex() == 1:
                self.botonesDeProduct(self.PrinWin.frame_8, None)
            # si el usuario cerro secion se elimina la informacion gurdada y se refleja en este boton
            self.PrinWin.pushButton.setText("")
        self.MensajeDeProduc()
    # busca los productos que el cliente desea dependiendo de su busqueda

    def buscarProducto(self):
        Busqueda = self.PrinWin.lineEdit.text()
        if self.PrinWin.radioButton_2.isChecked():
            self.botonesDeProduct(self.PrinWin.frame_8,
                                  BuscarProducto(Busqueda, "Vendedor"))
        elif self.PrinWin.radioButton.isChecked():
            self.botonesDeProduct(self.PrinWin.frame_8,
                                  BuscarProducto(Busqueda, "Producto"))
        elif self.PrinWin.radioButton_5.isChecked():
            self.botonesDeProduct(self.PrinWin.frame_8,
                                  BuscarProducto(Busqueda, "Tipo"))
        elif self.PrinWin.radioButton_3.isChecked():
            self.botonesDeProduct(self.PrinWin.frame_8,
                                  BuscarProducto(Busqueda, "Precio"))
        elif self.PrinWin.radioButton_4.isChecked():
            self.botonesDeProduct(self.PrinWin.frame_8,
                                  BuscarProducto(Busqueda, "Cantidad"))

    def botonesDeProduct(self, widget, actuali):
        self.i = 0  # reinisia el contador para la lista de prodcutos
        self.contadorY = 0  # contador para la posicion en x
        self.contadorX = 0  # contador para la posición en y
        if actuali == None:
            Data = Ventas()  # venta en general
        else:
            Data = actuali  # dependiendo de la busqueda del cliente
        if Data != []:  # si la lista de productos no esta vacia
            while (len(Data) == len(self.ListaDeWidgets) or len(self.ListaDeWidgets) != 0):
                # para la actualizacion de productos se eliminan los anteriores widget
                i = len(self.ListaDeWidgets)-1
                self.ListaDeButons[i].close()  # cierra la posicion
                self.ListaDeWidgets[i].close()
                self.ListaDeButons.pop(i)  # lo elimina de la ListaDeButons
                self.ListaDeWidgets.pop(i)

            while (len(Data) > len(self.ListaDeWidgets)):
                self.ListaDeWidgets.insert(self.i, AnimaButtonHover(
                    widget))  # crea un boton animado en la lista
                self.ListaDeButons.insert(self.i, QPushButton(
                    widget))  # crea un boton en la lista
                self.ListaDeButons[self.i].setObjectName("Boton_"+str(self.i))
                self.ListaDeWidgets[self.i].setObjectName(
                    str(self.i))  # nombre
                with open("CSS/stylesBoton.css", "r") as f:
                    self.ListaDeWidgets[self.i].setStyleSheet(
                        f.read())  # estilos para cada boton
                if widget != self.PrinWin.Casa:
                    # tamaño del widget
                    widget.setMinimumSize(QSize(1300, self.contadorY+415))
                    self.ListaDeWidgets[self.i].setGeometry(
                        QRect((315*self.contadorX)+90, self.contadorY+75, 200, 300))  # posicion
                    self.ListaDeButons[self.i].setGeometry(
                        QRect((315*self.contadorX)+115, self.contadorY+320, 150, 35))
                elif widget == self.PrinWin.Casa:
                    # tamaño del widget
                    widget.setMinimumSize(QSize(1300, self.contadorY+315))
                    self.ListaDeWidgets[self.i].setGeometry(
                        QRect((315*self.contadorX)+60, self.contadorY+15, 200, 300))  # posicion
                    self.ListaDeButons[self.i].setGeometry(
                        QRect((315*self.contadorX)+85, self.contadorY+260, 150, 35))
                # conectar cada uno de los metos con la posicion de cada boton
                if widget == self.PrinWin.frame_8:  # si es cliente
                    self.ListaDeWidgets[self.i].clicked.connect(
                        partial(self.CompraProduc, Data[self.i]))
                    self.ListaDeButons[self.i].clicked.connect(
                        partial(self.CompraProduc, Data[self.i]))
                    self.ListaDeButons[self.i].setText("Comprar")
                elif widget == self.PrinWin.widget_6:  # si es vendedor
                    self.ListaDeWidgets[self.i].clicked.connect(
                        partial(self.ProductoVen, Data[self.i]))
                    self.ListaDeButons[self.i].clicked.connect(
                        partial(self.ProductoVen, Data[self.i]))
                    self.ListaDeButons[self.i].setText("Seleccionar")
                else:
                    self.ListaDeWidgets[self.i].clicked.connect(
                        partial(self.ComentarioProduc, Data[self.i]))
                    self.ListaDeButons[self.i].clicked.connect(
                        partial(self.ComentarioProduc, Data[self.i]))
                    self.ListaDeButons[self.i].setText("Comentarios")
                self.ListaDeWidgets[self.i].setVisible(True)  # se visualiza
                self.ListaDeButons[self.i].setVisible(True)
                # se agregan caracteristicas de la vista
                self.WidgetInfoProduc(
                    self.ListaDeWidgets[self.i], Data[self.i])
                if self.contadorX == 3:  # contador con cada salto
                    self.contadorY += 315
                    self.contadorX = 0
                else:
                    self.contadorX += 1
                self.i += 1
        else:
            # si la lista de ventas no existe se elimina los widgets creados con la anterior busqueda
            while (len(self.ListaDeWidgets) != 0):
                i = len(self.ListaDeWidgets)-1
                self.ListaDeButons[i].close()
                self.ListaDeWidgets[i].close()
                self.ListaDeButons.pop(i)
                self.ListaDeWidgets.pop(i)

    def ProductoVen(self, data):
        # si el vendedor que inicio sesion es el que desea elimniar el producto
        if self.dato[1] == data[1]:
            self.PrinWin.lineEdit_4.setText(data[2])
            self.PrinWin.lineEdit_6.setText(data[3])
            self.PrinWin.lineEdit_7.setText(str(data[4]))
            self.PrinWin.lineEdit_8.setText(str(data[5]))
            self.EliminarVen(data[0])
            self.botonesDeProduct(self.PrinWin.widget_6, None)

    def EliminarVen(self, info):
        # si el boton de eliminar se manda a llamar
        if self.PrinWin.pushButton_12 == info and self.ID_venta != None:
            EliminarVenta(self.ID_venta)
            # Elimina el contenido de los lineEdit
            self.PrinWin.lineEdit_4.clear()
            self.PrinWin.lineEdit_6.clear()
            self.PrinWin.lineEdit_7.clear()
            self.PrinWin.lineEdit_8.clear()
            # Actualiza lista de Productos
            self.botonesDeProduct(self.PrinWin.widget_6, None)
            # de lo contrario la informacion se aguarda
        else:
            self.ID_venta = info

    def CompraProduc(self, data):
        self.contadorDeCompras += 1  # contador de compras relizadas
        self.PrinWin.pushButton_13.setEnabled(True)
        with open("CSS/stylesBoton.css", "r") as f:
            self.PrinWin.pushButton_13.setStyleSheet(
                f.read())  # estilos para el boton
        self.PrinWin.pushButton_13.setText(
            str(self.contadorDeCompras))  # visualizción de compras
        if self.dato != 0:
            self.Ticket.infoCompra((data[2], data[4]), self.contadorDeCompras, 'agregar', [
                                   self.dato[1], data[2], data[3], data[4]])
        else:
            self.Ticket.infoCompra(
                (data[2], data[4]), self.contadorDeCompras, 'agregar', 0)

    # para cada lista de wiget creados se agrega los elementos para la visualizción de la invormacion de la venta
    def WidgetInfoProduc(self, widget, info):
        self.gridLayout_2 = QGridLayout(widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_2 = QWidget(widget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(
            41, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)
        self.toolButton = QToolButton(self.widget_2)
        self.toolButton.setObjectName(u"toolButton")
        icon = QIcon()
        icon.addFile(u":/ICONS/carrito-de-compras.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(56, 52))
        self.gridLayout.addWidget(self.toolButton, 0, 1, 1, 1)
        self.horizontalSpacer_2 = QSpacerItem(
            41, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)
        self.label = QLabel(widget)
        self.label.setObjectName(u"label")
        self.label.setText("Producto: "+info[2] +
                           "\nTipo: "+info[3] +
                           "\nPrecio: $ "+str(info[4])+" MX" +
                           "\nCantidad: "+str(info[5]) +
                           "\nVendedor: "+info[1])
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.verticalSpacer = QSpacerItem(
            22, 41, QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)

    def guardarVenta(self):
        if self.dato[3] == "Vendedor":
            Nombre = self.PrinWin.lineEdit_4.text()
            Tipo = self.PrinWin.lineEdit_6.text()
            Precio = self.PrinWin.lineEdit_7.text()
            Cantidad = self.PrinWin.lineEdit_8.text()
            if Nombre != '' and Tipo != '' and Precio != '' and Cantidad != '':
                insertarVenta(
                    (self.dato[1], Nombre, Tipo, int(Precio), int(Cantidad)))
                self.PrinWin.lineEdit_4.clear()
                self.PrinWin.lineEdit_6.clear()
                self.PrinWin.lineEdit_7.clear()
                self.PrinWin.lineEdit_8.clear()
        self.botonesDeProduct(self.PrinWin.widget_6, None)

    def ProductosComprados(self):
        if self.dato != 0:
            compra = BuscarCompras(self.dato[1])
            self.PrinWin.tableWidget.setRowCount(len(compra))
            for (index_col, col) in enumerate(compra):
                for (index_cell, cell) in enumerate(col):
                    self.PrinWin.tableWidget.setItem(
                        index_col, index_cell, QTableWidgetItem(str(cell)))
        else:
            compra = []
            self.PrinWin.tableWidget.setRowCount(len(compra))
            for (index_col, col) in enumerate(compra):
                for (index_cell, cell) in enumerate(col):
                    self.PrinWin.tableWidget.setItem(
                        index_col, index_cell, QTableWidgetItem(str(cell)))

    # configuracion de casa
    def menu(self):
        # configuración de animacion para widget_5 y 7 sus tamaños
        if self.PrinWin.widget_7.width() == 0:
            TamaxWidget_7 = (0, 340)
        elif self.PrinWin.widget_7.width() == 340:
            TamaxWidget_7 = (340, 0)
        self.user.animationWidget(
            self.PrinWin.widget_7, 200, TamaxWidget_7[0], TamaxWidget_7[1], False, False, 'maximumWidth')

    def Sliderconfig(self):
        self.PrinWin.verticalSlider.sliderReleased.connect(
            lambda: self.valueSlider(self.PrinWin.verticalSlider))
        self.PrinWin.verticalSlider_2.sliderReleased.connect(
            lambda: self.valueSlider(self.PrinWin.verticalSlider_2))
        self.PrinWin.verticalSlider_3.sliderReleased.connect(
            lambda: self.valueSlider(self.PrinWin.verticalSlider_3))
        self.PrinWin.verticalSlider_4.sliderReleased.connect(
            lambda: self.valueSlider(self.PrinWin.verticalSlider_4))

    def valueSlider(self, widget):
        if widget == self.PrinWin.verticalSlider:
            self.configcolor[0] = self.PrinWin.verticalSlider.value()
        elif widget == self.PrinWin.verticalSlider_2:
            self.configcolor[1] = self.PrinWin.verticalSlider_2.value()
        elif widget == self.PrinWin.verticalSlider_3:
            self.configcolor[2] = self.PrinWin.verticalSlider_3.value()
        elif widget == self.PrinWin.verticalSlider_4:
            self.configcolor[3] = self.PrinWin.verticalSlider_4.value()
        self.PrinWin.frame.setStyleSheet(
            f"background-color:rgba({self.configcolor[0]},{self.configcolor[1]},{self.configcolor[2]},{self.configcolor[3]});")
        self.PrinWin.ColorRGBA.setText(
            f"  R={self.configcolor[0]}     G={self.configcolor[1]}    B={self.configcolor[2]}   A={self.configcolor[3]}")

    def ComentarioProduc(self, __id):
        self.PrinWin.label_6.setText("Producto: "+__id[2] +
                                     "\nTipo:  "+__id[3] +
                                     "\nPrecio: $ "+str(__id[4])+" MX" +
                                     "\nVendedor: "+__id[1])
        self.Product = __id[0]
        self.MensajeDeProduc()

    def Visualizacion(self):
        Mensaje = self.PrinWin.plainTextEdit.toPlainText()
        if self.dato != 0 and Mensaje != "":
            EnviarMen((self.dato[1], Mensaje, self.Product))
            self.PrinWin.plainTextEdit.clear()
        else:
            self.Aviso.Titulo("Error", "El Mensaje No fue Guardado")
            self.Aviso.exec()
        self.MensajeDeProduc()

    def MensajeDeProduc(self):
        BusquedaMens = BuscarMensajeProduc(self.Product)
        tamano = 0
        while (len(self.ListaDeWidgetsMensaje) != 0):
            i = len(self.ListaDeWidgetsMensaje)-1
            self.ListaDeWidgetsMensaje[i].close()
            self.ListaDeWidgetsMensaje.pop(i)
            self.contadorDeMensjes = 0

        for i in BusquedaMens:
            for j in range(len(i)):
                if j != 0 and j % 3 == 0:
                    user = i[j-2]
                    aux = " ->"+user+"\n"
                    Mensaje = i[j-1]
                    self.ListaDeWidgetsMensaje.insert(
                        self.contadorDeMensjes, QWidget(self.PrinWin.MensajesDeTexto))
                    self.ListaDeWidgetsMensaje[self.contadorDeMensjes].setVisible(
                        True)
                    TamTaxto = 0
                    contador = 0
                    for i in Mensaje:
                        aux += i
                        if i == " " and contador >= 18:
                            aux += "\n"
                            contador = 0
                            TamTaxto += 15
                        contador += 1
                    if self.dato != 0:
                        if user == self.dato[1]:
                            self.MensUser1(
                                self.ListaDeWidgetsMensaje[self.contadorDeMensjes], aux)
                            self.ListaDeWidgetsMensaje[self.contadorDeMensjes].setGeometry(
                                QRect(90, tamano, 240, 71+TamTaxto))
                        else:
                            self.Mensuser2(
                                self.ListaDeWidgetsMensaje[self.contadorDeMensjes], aux)
                            self.ListaDeWidgetsMensaje[self.contadorDeMensjes].setGeometry(
                                QRect(10, tamano, 240, 71+TamTaxto))
                    else:
                        self.Mensuser2(
                            self.ListaDeWidgetsMensaje[self.contadorDeMensjes], aux)
                        self.ListaDeWidgetsMensaje[self.contadorDeMensjes].setGeometry(
                            QRect(10, tamano, 240, 71+TamTaxto))
                    tamano = tamano+TamTaxto+60  # +TamTaxto
                    self.PrinWin.MensajesDeTexto.setMinimumSize(
                        QSize(320, tamano+20))
                    aux = ""
                    self.contadorDeMensjes += 1

    def MensUser1(self, widget, texto):
        Layout1 = QGridLayout(widget)
        Layout1.setObjectName(u"gridLayout")
        Textouser1 = QLabel(widget)
        Textouser1.setObjectName(u"label_3")
        Textouser1.setScaledContents(True)
        Textouser1.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        Layout1.addWidget(Textouser1, 0, 0, 1, 1)
        IconUser1 = QToolButton(widget)
        IconUser1.setObjectName(u"IconUser1")
        icon = QIcon()
        icon.addFile(u":/ICONS/usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        IconUser1.setIcon(icon)
        IconUser1.setIconSize(QSize(50, 50))
        Layout1.addWidget(IconUser1, 0, 1, 1, 1)
        Textouser1.setText(texto)

    def Mensuser2(self, widget, texto2):
        Layout = QGridLayout(widget)
        Layout.setObjectName(u"gridLayout_2")
        IconDeUser = QToolButton(widget)
        IconDeUser.setObjectName(u"toolButton_2")
        icon = QIcon()
        icon.addFile(u":/ICONS/usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        IconDeUser.setIcon(icon)
        IconDeUser.setIconSize(QSize(50, 50))
        Layout.addWidget(IconDeUser, 0, 0, 1, 1)
        TextoMens = QLabel(widget)
        TextoMens.setObjectName(u"label_3")
        TextoMens.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        Layout.addWidget(TextoMens, 0, 1, 1, 1)
        TextoMens.setText(texto2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WindowPrin()
    window.show()
    sys.exit(app.exec())
