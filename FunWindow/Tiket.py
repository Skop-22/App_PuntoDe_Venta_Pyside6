from GUI.ui_TIKET import *
from .Mens import Mensage
from DataBase.coneccion import insertarCompra

class TiketWindow(QDialog):
    def __init__(self,parent=None):
        QDialog.__init__(self,parent)
        self.Tiketwind = Ui_Dialog()
        self.Tiketwind.setupUi(self)  
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)#elimina el titulo
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Men = Mensage()
        self.Tiketwind.pushButton_4.clicked.connect(lambda: self.elimiarCompras())
        self.Tiketwind.pushButton_3.clicked.connect(lambda: self.close())
        self.Tiketwind.pushButton_2.clicked.connect(lambda: self.comprar())
        self.Tiketwind.pushButton_5.clicked.connect(lambda: self.eliminarItenCompra())
        self.precio=0
        self.ListaInfo=[]
        self.Lista=[]

    def infoCompra(self,ListaPro,Cantidad,tipo,InfoAdicional):  
        self.Tiketwind.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.Tiketwind.dateEdit.setDisplayFormat("dd/MM/yyyy")
        self.precio=0
        if tipo=='agregar':
            self.ListaInfo.append(InfoAdicional)
            self.Lista.append(ListaPro)
        elif tipo=='eliminar':
            self.ListaInfo=[]
            self.Lista=[]
            self.Tiketwind.Total.setText('')
        self.Tiketwind.tableWidget.setRowCount(len(self.Lista))
        for (index_col, col) in enumerate(self.Lista):
            self.precio=col[1]+self.precio
            self.Tiketwind.Total.setText(str(self.precio))
            for (index_cell, cell) in enumerate(col):
                self.Tiketwind.tableWidget.setItem(index_col,index_cell, QTableWidgetItem(str(cell)))
        self.Tiketwind.ProductosTotales.setText(str(Cantidad))

    def elimiarCompras(self):
        self.infoCompra([],'','eliminar',[])

    def comprar(self):
        fecha=str(self.Tiketwind.dateEdit.date().day())+"/"+str(self.Tiketwind.dateEdit.date().month())+"/"+str(self.Tiketwind.dateEdit.date().year())
        if self.ListaInfo[0] == 0:
            self.Men.Titulo("¡Error!","Para comprar productos debe iniciar sesion")
            self.Men.exec()
        else:
            for i,j in enumerate(self.ListaInfo):
                insertarCompra((j[0],j[1],j[2],j[3],fecha))
            self.Men.Titulo("¡Compra!","Compra Realizada :)")
            self.Men.exec()
            self.elimiarCompras()
        #print(insertarCompra())

    def eliminarItenCompra(self):
        NombreProduc=self.Tiketwind.lineEdit.text()
        for i,j in enumerate(self.Lista):
            if j[0] == NombreProduc:
                self.Lista.pop(i)
                self.ListaInfo.pop(i)
                self.precio=self.precio-int(j[1])
        self.Tiketwind.tableWidget.setRowCount(len(self.Lista))
        for (index_col, col) in enumerate(self.Lista):
            for (index_cell, cell) in enumerate(col):
                self.Tiketwind.tableWidget.setItem(index_col,index_cell, QTableWidgetItem(str(cell)))
        self.Tiketwind.ProductosTotales.setText(str(len(self.Lista)))
        self.Tiketwind.Total.setText(str(self.precio))
        self.Tiketwind.lineEdit.clear()
        return len(self.Lista)
