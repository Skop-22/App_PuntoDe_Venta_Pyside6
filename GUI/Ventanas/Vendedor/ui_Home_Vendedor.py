# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Home_VendedorWDZdzO.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QWidget)

from qfluentwidgets import (LineEdit, SearchLineEdit)

class Ui_HomeVendedor(object):
    def setupUi(self, HomeVendedor):
        if not HomeVendedor.objectName():
            HomeVendedor.setObjectName(u"HomeVendedor")
        HomeVendedor.resize(780, 514)
        self.gridLayout_2 = QGridLayout(HomeVendedor)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(25)
        self.gridLayout_2.setContentsMargins(10, 20, 20, 20)
        self.SearchLineEdit = SearchLineEdit(HomeVendedor)
        self.SearchLineEdit.setObjectName(u"SearchLineEdit")

        self.gridLayout_2.addWidget(self.SearchLineEdit, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)


        self.retranslateUi(HomeVendedor)

        QMetaObject.connectSlotsByName(HomeVendedor)
    # setupUi

    def retranslateUi(self, HomeVendedor):
        HomeVendedor.setWindowTitle(QCoreApplication.translate("HomeVendedor", u"Form", None))
    # retranslateUi
