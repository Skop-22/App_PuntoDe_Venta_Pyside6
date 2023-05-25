# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mensage_TexmlbYqe.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
from GUI.ICONS.ICONS_rc import *

class Ui_MensageCon(object):
    def setupUi(self, MensageCon):
        if not MensageCon.objectName():
            MensageCon.setObjectName(u"MensageCon")
        MensageCon.resize(300, 180)
        MensageCon.setMaximumSize(QSize(300, 200))
        self.gridLayout = QGridLayout(MensageCon)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(MensageCon)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        font = QFont()
        font.setPointSize(11)
        self.widget.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.widget_14 = QWidget(self.widget)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_5 = QGridLayout(self.widget_14)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(9, 9, 9, 9)
        self.Cerrar = QPushButton(self.widget_14)
        self.Cerrar.setObjectName(u"Cerrar")
        icon = QIcon()
        icon.addFile(u":/ICONS/cerrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Cerrar.setIcon(icon)
        self.Cerrar.setIconSize(QSize(25, 30))

        self.gridLayout_5.addWidget(self.Cerrar, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.widget_14, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.widget)

        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit = QLineEdit(self.page)
        self.lineEdit.setObjectName(u"lineEdit")
        font2 = QFont()
        font2.setPointSize(14)
        self.lineEdit.setFont(font2)
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.lineEdit.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_6 = QGridLayout(self.page_2)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(12)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout = QHBoxLayout(self.widget_5)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 8)
        self.pushButton_3 = QPushButton(self.widget_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.widget_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.gridLayout_4.addWidget(self.widget_5, 0, 0, 1, 1, Qt.AlignRight)


        self.verticalLayout.addWidget(self.widget_2)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(MensageCon)
        self.Cerrar.clicked.connect(MensageCon.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MensageCon)
    # setupUi

    def retranslateUi(self, MensageCon):
        MensageCon.setWindowTitle(QCoreApplication.translate("MensageCon", u"Dialog", None))
        self.label_2.setText("")
        self.Cerrar.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MensageCon", u"****************", None))
        self.label.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MensageCon", u"Aceptar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MensageCon", u"Cancelar", None))
    # retranslateUi

