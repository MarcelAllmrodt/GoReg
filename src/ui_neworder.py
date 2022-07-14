# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_neworder.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NewOrder(object):
    def setupUi(self, NewOrder):
        if not NewOrder.objectName():
            NewOrder.setObjectName(u"NewOrder")
        NewOrder.resize(244, 86)
        NewOrder.setLocale(QLocale(QLocale.German, QLocale.Germany))
        self.verticalLayout = QVBoxLayout(NewOrder)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.flayout_data = QFormLayout()
        self.flayout_data.setObjectName(u"flayout_data")
        self.l_type = QLabel(NewOrder)
        self.l_type.setObjectName(u"l_type")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.l_type.setFont(font)

        self.flayout_data.setWidget(0, QFormLayout.LabelRole, self.l_type)

        self.le_type = QLineEdit(NewOrder)
        self.le_type.setObjectName(u"le_type")

        self.flayout_data.setWidget(0, QFormLayout.FieldRole, self.le_type)


        self.verticalLayout.addLayout(self.flayout_data)

        self.hlayout_buttons = QHBoxLayout()
        self.hlayout_buttons.setObjectName(u"hlayout_buttons")
        self.pb_create = QPushButton(NewOrder)
        self.pb_create.setObjectName(u"pb_create")

        self.hlayout_buttons.addWidget(self.pb_create)

        self.hspacer_buttons = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlayout_buttons.addItem(self.hspacer_buttons)

        self.pb_cancel = QPushButton(NewOrder)
        self.pb_cancel.setObjectName(u"pb_cancel")

        self.hlayout_buttons.addWidget(self.pb_cancel)


        self.verticalLayout.addLayout(self.hlayout_buttons)


        self.retranslateUi(NewOrder)
        self.pb_create.clicked.connect(NewOrder.accept)
        self.pb_cancel.clicked.connect(NewOrder.reject)

        QMetaObject.connectSlotsByName(NewOrder)
    # setupUi

    def retranslateUi(self, NewOrder):
        NewOrder.setWindowTitle(QCoreApplication.translate("NewOrder", u"Neuer Auftrag", None))
        self.l_type.setText(QCoreApplication.translate("NewOrder", u"Typ", None))
        self.pb_create.setText(QCoreApplication.translate("NewOrder", u"Erstellen", None))
        self.pb_cancel.setText(QCoreApplication.translate("NewOrder", u"Abbrechen", None))
    # retranslateUi

