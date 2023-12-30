# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'productos_vendedorOLlnwm.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QSizePolicy,
    QTableWidgetItem, QWidget)

from qfluentwidgets import TableWidget

class Ui_productos_vendedor(object):
    def setupUi(self, productos_vendedor):
        if not productos_vendedor.objectName():
            productos_vendedor.setObjectName(u"productos_vendedor")
        productos_vendedor.resize(772, 476)
        self.gridLayout = QGridLayout(productos_vendedor)
        self.gridLayout.setObjectName(u"gridLayout")
        self.TableWidget = TableWidget(productos_vendedor)
        if (self.TableWidget.columnCount() < 6):
            self.TableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.TableWidget.setObjectName(u"TableWidget")
        self.TableWidget.setProperty("selectRightClickedRow", False)
        self.TableWidget.horizontalHeader().setVisible(True)
        self.TableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.TableWidget.horizontalHeader().setDefaultSectionSize(110)
        self.TableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.TableWidget.horizontalHeader().setStretchLastSection(True)
        self.TableWidget.verticalHeader().setVisible(True)
        self.TableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.TableWidget.verticalHeader().setProperty("showSortIndicator", False)

        self.gridLayout.addWidget(self.TableWidget, 0, 0, 1, 1)


        self.retranslateUi(productos_vendedor)

        QMetaObject.connectSlotsByName(productos_vendedor)
    # setupUi

    def retranslateUi(self, productos_vendedor):
        productos_vendedor.setWindowTitle(QCoreApplication.translate("productos_vendedor", u"productos vendedor", None))
        ___qtablewidgetitem = self.TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("productos_vendedor", u"Id", None));
        ___qtablewidgetitem1 = self.TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("productos_vendedor", u"Nombre", None));
        ___qtablewidgetitem2 = self.TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("productos_vendedor", u"Tipo", None));
        ___qtablewidgetitem3 = self.TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("productos_vendedor", u"Detalles", None));
        ___qtablewidgetitem4 = self.TableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("productos_vendedor", u"precio", None));
        ___qtablewidgetitem5 = self.TableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("productos_vendedor", u"cantidad", None));
    # retranslateUi

