# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_newarticle.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NewArticle(object):
    def setupUi(self, NewArticle):
        if not NewArticle.objectName():
            NewArticle.setObjectName(u"NewArticle")
        NewArticle.resize(264, 191)
        NewArticle.setLocale(QLocale(QLocale.German, QLocale.Germany))
        self.verticalLayout = QVBoxLayout(NewArticle)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.flayout_data = QFormLayout()
        self.flayout_data.setObjectName(u"flayout_data")
        self.l_ident = QLabel(NewArticle)
        self.l_ident.setObjectName(u"l_ident")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.l_ident.setFont(font)
        self.l_ident.setScaledContents(False)

        self.flayout_data.setWidget(0, QFormLayout.LabelRole, self.l_ident)

        self.le_ident = QLineEdit(NewArticle)
        self.le_ident.setObjectName(u"le_ident")
        self.le_ident.setMaxLength(11)

        self.flayout_data.setWidget(0, QFormLayout.FieldRole, self.le_ident)

        self.l_name = QLabel(NewArticle)
        self.l_name.setObjectName(u"l_name")

        self.flayout_data.setWidget(2, QFormLayout.LabelRole, self.l_name)

        self.le_name = QLineEdit(NewArticle)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setMaxLength(20)

        self.flayout_data.setWidget(2, QFormLayout.FieldRole, self.le_name)

        self.l_colour = QLabel(NewArticle)
        self.l_colour.setObjectName(u"l_colour")

        self.flayout_data.setWidget(3, QFormLayout.LabelRole, self.l_colour)

        self.le_colour = QLineEdit(NewArticle)
        self.le_colour.setObjectName(u"le_colour")
        self.le_colour.setMaxLength(10)

        self.flayout_data.setWidget(3, QFormLayout.FieldRole, self.le_colour)

        self.l_client = QLabel(NewArticle)
        self.l_client.setObjectName(u"l_client")
        self.l_client.setFont(font)

        self.flayout_data.setWidget(1, QFormLayout.LabelRole, self.l_client)

        self.le_customer = QLineEdit(NewArticle)
        self.le_customer.setObjectName(u"le_customer")
        self.le_customer.setMaxLength(20)

        self.flayout_data.setWidget(1, QFormLayout.FieldRole, self.le_customer)


        self.verticalLayout.addLayout(self.flayout_data)

        self.hlayout_buttons = QHBoxLayout()
        self.hlayout_buttons.setObjectName(u"hlayout_buttons")
        self.hlayout_buttons.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.pb_create = QPushButton(NewArticle)
        self.pb_create.setObjectName(u"pb_create")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_create.sizePolicy().hasHeightForWidth())
        self.pb_create.setSizePolicy(sizePolicy)

        self.hlayout_buttons.addWidget(self.pb_create)

        self.hspacer_buttons = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlayout_buttons.addItem(self.hspacer_buttons)

        self.pb_cancel = QPushButton(NewArticle)
        self.pb_cancel.setObjectName(u"pb_cancel")
        sizePolicy.setHeightForWidth(self.pb_cancel.sizePolicy().hasHeightForWidth())
        self.pb_cancel.setSizePolicy(sizePolicy)

        self.hlayout_buttons.addWidget(self.pb_cancel)


        self.verticalLayout.addLayout(self.hlayout_buttons)

        QWidget.setTabOrder(self.le_ident, self.le_customer)
        QWidget.setTabOrder(self.le_customer, self.le_name)
        QWidget.setTabOrder(self.le_name, self.le_colour)
        QWidget.setTabOrder(self.le_colour, self.pb_create)
        QWidget.setTabOrder(self.pb_create, self.pb_cancel)

        self.retranslateUi(NewArticle)
        self.pb_cancel.clicked.connect(NewArticle.reject)
        self.pb_create.clicked.connect(NewArticle.accept)

        QMetaObject.connectSlotsByName(NewArticle)
    # setupUi

    def retranslateUi(self, NewArticle):
        NewArticle.setWindowTitle(QCoreApplication.translate("NewArticle", u"Neuer Artikel", None))
        self.l_ident.setText(QCoreApplication.translate("NewArticle", u"Bezeichnung", None))
        self.l_name.setText(QCoreApplication.translate("NewArticle", u"Name", None))
        self.l_colour.setText(QCoreApplication.translate("NewArticle", u"Farbe", None))
        self.l_client.setText(QCoreApplication.translate("NewArticle", u"Kunde", None))
        self.pb_create.setText(QCoreApplication.translate("NewArticle", u"Erstellen", None))
        self.pb_cancel.setText(QCoreApplication.translate("NewArticle", u"Abbrechen", None))
    # retranslateUi

