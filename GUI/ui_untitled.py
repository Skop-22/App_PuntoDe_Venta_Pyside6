# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledxDbUXT.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QToolButton, QWidget)
from GUI.ICONS.ICONS_rc import *

class Ui_UsuarioGUI(object):
    def setupUi(self, UsuarioGUI):
        if not UsuarioGUI.objectName():
            UsuarioGUI.setObjectName(u"UsuarioGUI")
        UsuarioGUI.resize(380, 480)
        UsuarioGUI.setMinimumSize(QSize(380, 480))
        UsuarioGUI.setMaximumSize(QSize(380, 480))
        UsuarioGUI.setStyleSheet(u"")
        self.frame = QFrame(UsuarioGUI)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 380, 480))
        self.frame.setMaximumSize(QSize(380, 480))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(380, 480))
        self.stackedWidget.setMaximumSize(QSize(380, 480))
        self.stackedWidget.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.toolButton = QToolButton(self.page)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(140, 50, 110, 110))
        icon = QIcon()
        icon.addFile(u":/ICONS/usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(90, 90))
        self.lineEdit_2 = QLineEdit(self.page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(50, 260, 271, 31))
        font = QFont()
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(50, 380, 121, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton_2.setFont(font1)
        self.pushButton_3 = QPushButton(self.page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(40, 310, 291, 51))
        self.pushButton_3.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/ICONS/agregar-usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.lineEdit = QLineEdit(self.page)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 190, 271, 31))
        self.lineEdit.setFont(font)
        self.lineEdit.setClearButtonEnabled(True)
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 240, 101, 17))
        self.label_2.setFont(font1)
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 160, 81, 17))
        self.label.setFont(font1)
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 10, 41, 31))
        self.pushButton.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/ICONS/cerrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 10, 291, 31))
        self.label_4.setFont(font1)
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 430, 61, 21))
        self.comboBox_2 = QComboBox(self.page)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(240, 430, 111, 25))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 10, 291, 31))
        self.label_5.setFont(font1)
        self.lineEdit_3 = QLineEdit(self.page_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(130, 180, 221, 31))
        font2 = QFont()
        font2.setFamilies([u"Akaash"])
        font2.setPointSize(10)
        self.lineEdit_3.setFont(font2)
        self.lineEdit_3.setClearButtonEnabled(True)
        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 180, 101, 31))
        self.label_6.setFont(font1)
        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(18, 220, 101, 31))
        self.label_7.setFont(font1)
        self.lineEdit_4 = QLineEdit(self.page_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(130, 220, 221, 31))
        self.lineEdit_4.setFont(font2)
        self.lineEdit_4.setClearButtonEnabled(True)
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(18, 260, 101, 31))
        self.label_8.setFont(font1)
        self.lineEdit_5 = QLineEdit(self.page_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(130, 260, 221, 31))
        self.lineEdit_5.setFont(font2)
        self.lineEdit_5.setEchoMode(QLineEdit.Password)
        self.lineEdit_5.setClearButtonEnabled(True)
        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(18, 340, 101, 31))
        self.label_9.setFont(font1)
        self.comboBox = QComboBox(self.page_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(120, 340, 231, 31))
        self.lineEdit_6 = QLineEdit(self.page_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(130, 300, 221, 31))
        self.lineEdit_6.setFont(font2)
        self.lineEdit_6.setEchoMode(QLineEdit.Password)
        self.lineEdit_6.setClearButtonEnabled(True)
        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 300, 101, 31))
        self.label_10.setFont(font1)
        self.pushButton_5 = QPushButton(self.page_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(220, 400, 121, 31))
        self.pushButton_5.setFont(font1)
        self.pushButton_6 = QPushButton(self.page_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(50, 400, 121, 31))
        self.pushButton_6.setFont(font1)
        self.pushButton_4 = QPushButton(self.page_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(320, 10, 41, 31))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setIcon(icon2)
        self.toolButton_2 = QToolButton(self.page_2)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(150, 50, 110, 110))
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QSize(90, 90))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setMinimumSize(QSize(380, 480))
        self.page_3.setMaximumSize(QSize(380, 480))
        self.gridLayout_2 = QGridLayout(self.page_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_11 = QPushButton(self.page_3)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setIcon(icon2)
        self.pushButton_11.setIconSize(QSize(31, 28))

        self.gridLayout_2.addWidget(self.pushButton_11, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.page_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(96, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toolButton_3 = QToolButton(self.frame_2)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setIcon(icon)
        self.toolButton_3.setIconSize(QSize(125, 125))

        self.horizontalLayout.addWidget(self.toolButton_3)

        self.horizontalSpacer_2 = QSpacerItem(95, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 2)

        self.frame_3 = QFrame(self.page_3)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 0, 362, 264))
        self.frame_4.setMaximumSize(QSize(362, 264))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_7 = QPushButton(self.frame_4)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_4.addWidget(self.pushButton_7, 1, 1, 1, 1)

        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_4.addWidget(self.label_19, 2, 0, 1, 2)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        self.label_16.setFont(font3)

        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)

        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)

        self.gridLayout_3.addWidget(self.label_13, 2, 1, 1, 1)

        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)

        self.gridLayout_3.addWidget(self.label_11, 0, 1, 1, 1)

        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)

        self.gridLayout_3.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)

        self.gridLayout_3.addWidget(self.label_17, 2, 0, 1, 1)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.gridLayout_3.addWidget(self.label_12, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_6, 0, 0, 1, 2)

        self.pushButton_10 = QPushButton(self.frame_4)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_4.addWidget(self.pushButton_10, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(362, 0, 0, 264))
        self.frame_5.setMaximumSize(QSize(362, 264))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_9 = QPushButton(self.frame_5)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_6.addWidget(self.pushButton_9, 1, 1, 1, 1)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_20 = QLabel(self.frame_7)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_5.addWidget(self.label_20, 3, 0, 1, 1)

        self.label_22 = QLabel(self.frame_7)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_5.addWidget(self.label_22, 2, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_7)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_5.addWidget(self.lineEdit_8, 1, 1, 1, 1)

        self.lineEdit_10 = QLineEdit(self.frame_7)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_5.addWidget(self.lineEdit_10, 2, 1, 1, 1)

        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_5.addWidget(self.label_14, 0, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.frame_7)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_5.addWidget(self.comboBox_3, 4, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.frame_7)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_5.addWidget(self.lineEdit_7, 0, 1, 1, 1)

        self.label_21 = QLabel(self.frame_7)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_5.addWidget(self.label_21, 4, 0, 1, 1)

        self.label_18 = QLabel(self.frame_7)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_5.addWidget(self.label_18, 1, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.frame_7)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_5.addWidget(self.lineEdit_9, 3, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_7, 0, 0, 1, 2)

        self.pushButton_8 = QPushButton(self.frame_5)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_6.addWidget(self.pushButton_8, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 2, 0, 1, 2)

        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.retranslateUi(UsuarioGUI)
        self.pushButton_4.clicked.connect(UsuarioGUI.close)
        self.pushButton.clicked.connect(UsuarioGUI.close)
        self.pushButton_11.clicked.connect(UsuarioGUI.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(UsuarioGUI)
    # setupUi

    def retranslateUi(self, UsuarioGUI):
        UsuarioGUI.setWindowTitle(QCoreApplication.translate("UsuarioGUI", u"Dialog", None))
        self.toolButton.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("UsuarioGUI", u"***********", None))
        self.pushButton_2.setText(QCoreApplication.translate("UsuarioGUI", u"Iniciar sesi\u00f3n", None))
        self.pushButton_3.setText(QCoreApplication.translate("UsuarioGUI", u"Para poder iniciar sesi\u00f3n se necesita\n"
"registrarse", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("UsuarioGUI", u"Usuario", None))
        self.label_2.setText(QCoreApplication.translate("UsuarioGUI", u"Contrase\u00f1a", None))
        self.label.setText(QCoreApplication.translate("UsuarioGUI", u"Usuario", None))
        self.pushButton.setText("")
        self.label_4.setText(QCoreApplication.translate("UsuarioGUI", u"Pantalla de inicio de sesi\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("UsuarioGUI", u"Estilos", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("UsuarioGUI", u"Estilo clasico", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("UsuarioGUI", u"Estilo Black", None))

        self.label_5.setText(QCoreApplication.translate("UsuarioGUI", u"Inicio de registro", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("UsuarioGUI", u"Nombre del usuario", None))
        self.label_6.setText(QCoreApplication.translate("UsuarioGUI", u"Nombre", None))
        self.label_7.setText(QCoreApplication.translate("UsuarioGUI", u"Usuario", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("UsuarioGUI", u"Usuario", None))
        self.label_8.setText(QCoreApplication.translate("UsuarioGUI", u"Contrase\u00f1a", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("UsuarioGUI", u"Contrase\u00f1a", None))
        self.label_9.setText(QCoreApplication.translate("UsuarioGUI", u"Tipo", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("UsuarioGUI", u"Cliente", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("UsuarioGUI", u"Vendedor", None))

        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("UsuarioGUI", u"Contrase\u00f1a", None))
        self.label_10.setText(QCoreApplication.translate("UsuarioGUI", u"Validar Contra", None))
        self.pushButton_5.setText(QCoreApplication.translate("UsuarioGUI", u"Registrar", None))
        self.pushButton_6.setText(QCoreApplication.translate("UsuarioGUI", u"Iniciar sesion", None))
        self.pushButton_4.setText("")
        self.toolButton_2.setText("")
        self.pushButton_11.setText("")
        self.toolButton_3.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("UsuarioGUI", u"Modificar", None))
        self.label_19.setText(QCoreApplication.translate("UsuarioGUI", u"Modificaci\u00f3n de la informaci\u00f3n personal del usuario\n"
"al finalizar la actualizaci\u00f3n de los datos corrobore\n"
"que la informaci\u00f3n sea correcta si desea cambiar a\n"
"vendedor es mejor crear una cuenta tipo vendedor\n"
"para que la informaci\u00f3n de sus compras sean guardados", None))
        self.label_16.setText(QCoreApplication.translate("UsuarioGUI", u"Usuario:", None))
        self.label_13.setText("")
        self.label_11.setText("")
        self.label_15.setText(QCoreApplication.translate("UsuarioGUI", u"Nombre:", None))
        self.label_17.setText(QCoreApplication.translate("UsuarioGUI", u"Tipo:", None))
        self.label_12.setText("")
        self.pushButton_10.setText(QCoreApplication.translate("UsuarioGUI", u"Cerrar sesi\u00f3n", None))
        self.pushButton_9.setText(QCoreApplication.translate("UsuarioGUI", u"Guardar", None))
        self.label_20.setText(QCoreApplication.translate("UsuarioGUI", u"Validaci\u00f3n de Contrase\u00f1a", None))
        self.label_22.setText(QCoreApplication.translate("UsuarioGUI", u"Contrase\u00f1a", None))
        self.label_14.setText(QCoreApplication.translate("UsuarioGUI", u"Nombre", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("UsuarioGUI", u"Vendedor", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("UsuarioGUI", u"Cliente", None))

        self.label_21.setText(QCoreApplication.translate("UsuarioGUI", u"Tipo", None))
        self.label_18.setText(QCoreApplication.translate("UsuarioGUI", u"Usuario", None))
        self.pushButton_8.setText(QCoreApplication.translate("UsuarioGUI", u"Cancelar", None))
    # retranslateUi

