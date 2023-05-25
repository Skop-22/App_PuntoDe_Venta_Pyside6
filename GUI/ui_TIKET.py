# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TIKETZAquTE.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFrame,
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QProgressBar, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)
from GUI.ICONS.ICONS_rc import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(385, 520)
        Dialog.setStyleSheet(u"QWidget#widget{\n"
"	background-color: rgb(30, 30, 30);\n"
"}\n"
"*{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(385, 520))
        self.frame.setMaximumSize(QSize(385, 520))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 391, 521))
        self.widget_2.setStyleSheet(u"background-color: rgba(30, 28, 26, 255);")
        self.progressBar = QProgressBar(self.widget_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(-1, -1, 391, 541))
        self.progressBar.setStyleSheet(u"QProgressBar::chunk{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0.5, x2:0.518, y2:0.517045, stop:0.27957 rgba(30, 28, 26, 206), stop:0.913978 rgba(58, 119, 196, 255));}")
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(-1)
        self.progressBar.setTextVisible(False)
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(9, 9, 368, 501))
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 10, 36, 30))
        icon = QIcon()
        icon.addFile(u":/ICONS/cerrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(24, 24))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 301, 28))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 101, 17))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(270, 450, 81, 31))
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 450, 121, 31))
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 290, 341, 111))
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.ProductosTotales = QLabel(self.widget_3)
        self.ProductosTotales.setObjectName(u"ProductosTotales")

        self.gridLayout_2.addWidget(self.ProductosTotales, 0, 1, 1, 1)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.dateEdit = QDateEdit(self.widget_3)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout_2.addWidget(self.dateEdit, 1, 1, 1, 1)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.Total = QLabel(self.widget_3)
        self.Total.setObjectName(u"Total")

        self.gridLayout_2.addWidget(self.Total, 2, 1, 1, 1)

        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(15, 91, 341, 201))
        self.tableWidget.horizontalHeader().setDefaultSectionSize(169)
        self.Numero_De_Tiket = QLabel(self.widget)
        self.Numero_De_Tiket.setObjectName(u"Numero_De_Tiket")
        self.Numero_De_Tiket.setGeometry(QRect(214, 60, 141, 20))
        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(140, 450, 121, 31))
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 400, 201, 31))
        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(229, 400, 111, 31))
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(230, 60, 131, 16))
        self.label_6.setFont(font1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.progressBar.setFormat(QCoreApplication.translate("Dialog", u"%p%", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"COMPRAS A REALIZAR", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Productos ", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Comprar", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Seguir comprando", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Cantidad", None))
        self.ProductosTotales.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Fecha de compra", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Total a pagar", None))
        self.Total.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Nombre del producto", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Precio", None));
        self.Numero_De_Tiket.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Eliminar Compras", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Eliminar Producto", None))
        self.label_6.setText("")
    # retranslateUi

