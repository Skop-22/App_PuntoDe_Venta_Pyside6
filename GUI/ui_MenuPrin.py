# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MenuPrinZmNIfa.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)
from GUI.ICONS.ICONS_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(828, 613)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{	border:none;}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, 3, 9, 9)
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setBold(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(28, 28))
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(True)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.tab_3)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(40, 0, 20, 0)
        self.horizontalSpacer_2 = QSpacerItem(120, 9, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(self.widget_8)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.label_2.setFont(font1)
        self.label_2.setMouseTracking(False)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_4.addWidget(self.label_2, 0, Qt.AlignVCenter)

        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_15 = QGridLayout(self.widget_9)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.MenuCasa = QPushButton(self.widget_9)
        self.MenuCasa.setObjectName(u"MenuCasa")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.MenuCasa.setFont(font2)

        self.gridLayout_15.addWidget(self.MenuCasa, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.widget_9, 0, Qt.AlignRight|Qt.AlignTop)


        self.gridLayout_4.addWidget(self.widget_8, 0, 0, 1, 2, Qt.AlignTop)

        self.widget_10 = QWidget(self.tab_3)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy1)
        self.gridLayout_16 = QGridLayout(self.widget_10)
        self.gridLayout_16.setSpacing(1)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(2, 2, 2, 2)
        self.widget_5 = QWidget(self.widget_10)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy2)
        self.gridLayout_17 = QGridLayout(self.widget_5)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.widget_5)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 805, 482))
        self.horizontalLayout_5 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Casa = QFrame(self.scrollAreaWidgetContents_3)
        self.Casa.setObjectName(u"Casa")
        self.Casa.setMinimumSize(QSize(0, 0))
        self.Casa.setFrameShape(QFrame.StyledPanel)
        self.Casa.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.Casa)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_17.addWidget(self.scrollArea_3, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.widget_5, 0, 0, 1, 1)

        self.widget_7 = QWidget(self.widget_10)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy2.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy2)
        self.widget_7.setMinimumSize(QSize(0, 0))
        self.widget_7.setMaximumSize(QSize(0, 16777215))
        self.widget_7.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.widget_7)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.widget_7)
        self.widget_13.setObjectName(u"widget_13")
        self.gridLayout_19 = QGridLayout(self.widget_13)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_5 = QLabel(self.widget_13)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setPointSize(21)
        font3.setBold(True)
        self.label_5.setFont(font3)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setTextFormat(Qt.PlainText)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_19.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_6 = QLabel(self.widget_13)
        self.label_6.setObjectName(u"label_6")
        font4 = QFont()
        font4.setPointSize(18)
        self.label_6.setFont(font4)

        self.gridLayout_19.addWidget(self.label_6, 1, 0, 1, 1)

        self.toolButton_2 = QToolButton(self.widget_13)
        self.toolButton_2.setObjectName(u"toolButton_2")
        icon = QIcon()
        icon.addFile(u":/ICONS/carrito-de-compras.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QSize(70, 70))

        self.gridLayout_19.addWidget(self.toolButton_2, 0, 2, 2, 1)


        self.verticalLayout_4.addWidget(self.widget_13)

        self.scrollArea_5 = QScrollArea(self.widget_7)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 16, 319))
        self.horizontalLayout_6 = QHBoxLayout(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.MensajesDeTexto = QWidget(self.scrollAreaWidgetContents_5)
        self.MensajesDeTexto.setObjectName(u"MensajesDeTexto")
        sizePolicy1.setHeightForWidth(self.MensajesDeTexto.sizePolicy().hasHeightForWidth())
        self.MensajesDeTexto.setSizePolicy(sizePolicy1)
        self.MensajesDeTexto.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_6.addWidget(self.MensajesDeTexto)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_4.addWidget(self.scrollArea_5)

        self.widget_14 = QWidget(self.widget_7)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_20 = QGridLayout(self.widget_14)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.plainTextEdit = QPlainTextEdit(self.widget_14)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(0, 30))
        self.plainTextEdit.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_20.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        self.Enviar = QPushButton(self.widget_14)
        self.Enviar.setObjectName(u"Enviar")
        font5 = QFont()
        font5.setPointSize(23)
        self.Enviar.setFont(font5)
        icon1 = QIcon()
        iconThemeName = u"system-file-manager"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.Enviar.setIcon(icon1)
        self.Enviar.setIconSize(QSize(0, 0))

        self.gridLayout_20.addWidget(self.Enviar, 0, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.widget_14, 0, Qt.AlignBottom)


        self.gridLayout_16.addWidget(self.widget_7, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.widget_10, 1, 0, 1, 1)

        icon2 = QIcon()
        icon2.addFile(u":/ICONS/hogar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_6 = QGridLayout(self.tab_4)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.tab_4)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.pageCliente = QWidget()
        self.pageCliente.setObjectName(u"pageCliente")
        self.verticalLayout = QVBoxLayout(self.pageCliente)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.pageCliente)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1300, 1000))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(1300, 1000))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame_8)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 431, 31))
        self.lineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.lineEdit.setClearButtonEnabled(True)
        self.groupBox = QGroupBox(self.frame_8)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 40, 411, 31))
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.gridLayout_3.addWidget(self.radioButton, 0, 1, 1, 1)

        self.radioButton_5 = QRadioButton(self.groupBox)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.gridLayout_3.addWidget(self.radioButton_5, 0, 2, 1, 1)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_3.addWidget(self.radioButton_2, 0, 0, 1, 1)

        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout_3.addWidget(self.radioButton_3, 0, 4, 1, 1)

        self.radioButton_4 = QRadioButton(self.groupBox)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout_3.addWidget(self.radioButton_4, 0, 5, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.pageCliente)
        self.pageVendedor = QWidget()
        self.pageVendedor.setObjectName(u"pageVendedor")
        self.gridLayout_8 = QGridLayout(self.pageVendedor)
        self.gridLayout_8.setSpacing(3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(3, 3, 3, 3)
        self.frame_9 = QFrame(self.pageVendedor)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_9)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setVerticalSpacing(0)
        self.horizontalSpacer_8 = QSpacerItem(76, 10, QSizePolicy.Ignored, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_8, 0, 1, 1, 1)

        self.label_19 = QLabel(self.frame_9)
        self.label_19.setObjectName(u"label_19")
        font6 = QFont()
        font6.setPointSize(11)
        font6.setBold(True)
        self.label_19.setFont(font6)
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_19.setMargin(0)
        self.label_19.setIndent(0)

        self.gridLayout_13.addWidget(self.label_19, 0, 0, 1, 1, Qt.AlignTop)

        self.scrollArea_2 = QScrollArea(self.frame_9)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 0))

        self.verticalLayout_3.addWidget(self.widget_6)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_13.addWidget(self.scrollArea_2, 1, 0, 1, 2)


        self.gridLayout_8.addWidget(self.frame_9, 0, 0, 1, 1)

        self.frame_10 = QFrame(self.pageVendedor)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_10)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.widget_3 = QWidget(self.frame_10)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy4)
        self.gridLayout_11 = QGridLayout(self.widget_3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.pushButton_12 = QPushButton(self.widget_3)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout_11.addWidget(self.pushButton_12, 5, 0, 1, 1)

        self.label_17 = QLabel(self.widget_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_11.addWidget(self.label_17, 3, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.widget_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_11.addWidget(self.lineEdit_4, 1, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.widget_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_11.addWidget(self.lineEdit_6, 2, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.widget_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_11.addWidget(self.lineEdit_7, 3, 1, 1, 1)

        self.label_15 = QLabel(self.widget_3)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_11.addWidget(self.label_15, 1, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.widget_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_11.addWidget(self.lineEdit_8, 4, 1, 1, 1)

        self.label_18 = QLabel(self.widget_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_11.addWidget(self.label_18, 4, 0, 1, 1)

        self.label_16 = QLabel(self.widget_3)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_11.addWidget(self.label_16, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(11, 125, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_2, 6, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.widget_3)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_11.addWidget(self.pushButton_11, 5, 1, 1, 1)


        self.gridLayout_10.addWidget(self.widget_3, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.frame_10)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_9 = QGridLayout(self.widget_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalSpacer_4 = QSpacerItem(133, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.toolButton = QToolButton(self.widget_2)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(68, 68))

        self.gridLayout_9.addWidget(self.toolButton, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(132, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)


        self.gridLayout_10.addWidget(self.widget_2, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(21, 67, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_10.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_10, 0, 1, 1, 1, Qt.AlignRight)

        self.stackedWidget.addWidget(self.pageVendedor)

        self.gridLayout_6.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, icon, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_7 = QGridLayout(self.tab_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.tableWidget = QTableWidget(self.tab_5)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setMinimumSectionSize(41)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(194)

        self.gridLayout_7.addWidget(self.tableWidget, 1, 0, 1, 2)

        icon3 = QIcon()
        icon3.addFile(u":/ICONS/menu-hamburguesa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_5, icon3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_12 = QGridLayout(self.tab)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.tab)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.widget_4.setMinimumSize(QSize(200, 0))
        self.gridLayout_5 = QGridLayout(self.widget_4)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.widget_4)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 796, 900))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 900))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_6)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setVerticalSpacing(6)
        self.gridLayout_14.setContentsMargins(80, 20, 80, 20)
        self.widget = QWidget(self.frame_6)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.widget_11 = QWidget(self.widget)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(210, 90, 341, 171))
        self.gridLayout_18 = QGridLayout(self.widget_11)
        self.gridLayout_18.setSpacing(1)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(1, 1, 1, 1)
        self.verticalSlider_2 = QSlider(self.widget_11)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setMaximum(255)
        self.verticalSlider_2.setOrientation(Qt.Vertical)

        self.gridLayout_18.addWidget(self.verticalSlider_2, 0, 1, 1, 1)

        self.verticalSlider_4 = QSlider(self.widget_11)
        self.verticalSlider_4.setObjectName(u"verticalSlider_4")
        self.verticalSlider_4.setMaximum(255)
        self.verticalSlider_4.setOrientation(Qt.Vertical)

        self.gridLayout_18.addWidget(self.verticalSlider_4, 0, 3, 1, 1)

        self.verticalSlider = QSlider(self.widget_11)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMaximum(255)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_18.addWidget(self.verticalSlider, 0, 0, 1, 1)

        self.verticalSlider_3 = QSlider(self.widget_11)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        self.verticalSlider_3.setMaximum(255)
        self.verticalSlider_3.setOrientation(Qt.Vertical)

        self.gridLayout_18.addWidget(self.verticalSlider_3, 0, 2, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 90, 121, 41))
        font7 = QFont()
        font7.setPointSize(14)
        font7.setBold(True)
        self.label_3.setFont(font7)
        self.ColorRGBA = QLabel(self.widget)
        self.ColorRGBA.setObjectName(u"ColorRGBA")
        self.ColorRGBA.setGeometry(QRect(220, 50, 321, 31))
        font8 = QFont()
        font8.setPointSize(15)
        font8.setBold(False)
        self.ColorRGBA.setFont(font8)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 130, 181, 101))

        self.gridLayout_14.addWidget(self.widget, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_5.addWidget(self.scrollArea_4, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.widget_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font9 = QFont()
        font9.setPointSize(19)
        font9.setBold(True)
        self.label.setFont(font9)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_13 = QPushButton(self.frame_3)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setIcon(icon)
        self.pushButton_13.setIconSize(QSize(29, 32))

        self.horizontalLayout_2.addWidget(self.pushButton_13)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        font10 = QFont()
        font10.setPointSize(12)
        font10.setBold(True)
        self.pushButton.setFont(font10)
        icon4 = QIcon()
        icon4.addFile(u":/ICONS/usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QSize(29, 32))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(67, 25, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.horizontalLayout_3.addWidget(self.frame_3, 0, Qt.AlignRight)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon5 = QIcon()
        icon5.addFile(u":/ICONS/minimizar-signo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon5)
        self.pushButton_4.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon6 = QIcon()
        icon6.addFile(u":/ICONS/maximizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon6)
        self.pushButton_3.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon7 = QIcon()
        icon7.addFile(u":/ICONS/cerrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon7)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.horizontalLayout_3.addWidget(self.frame_4, 0, Qt.AlignRight)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 2)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_4.clicked.connect(MainWindow.showMinimized)

        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Valoraci\u00f3n de los Productos", None))
        self.MenuCasa.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Comentarios", None))
        self.label_6.setText("")
        self.toolButton_2.setText("")
        self.Enviar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Casa", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("")
        self.groupBox.setTitle("")
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Producto", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Vendedor", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Pre visualizaci\u00f3n de Todos los productos\n"
"En la Tienda", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.toolButton.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Productos", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Usuario", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nombre del Producto", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Precio", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Lista", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Color fondo ", None))
        self.ColorRGBA.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Congiruracion de color para \n"
"la Aplicacion", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Venta de Productos", None))
        self.pushButton_13.setText("")
        self.pushButton.setText("")
        self.pushButton_4.setText("")
        self.pushButton_3.setText("")
        self.pushButton_2.setText("")
    # retranslateUi

