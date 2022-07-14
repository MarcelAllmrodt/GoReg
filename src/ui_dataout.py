# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dataout.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DataOut(object):
    def setupUi(self, DataOut):
        if not DataOut.objectName():
            DataOut.setObjectName(u"DataOut")
        DataOut.resize(640, 480)
        DataOut.setMinimumSize(QSize(0, 0))
        DataOut.setLocale(QLocale(QLocale.German, QLocale.Germany))
        self.verticalLayout = QVBoxLayout(DataOut)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fr_search = QFrame(DataOut)
        self.fr_search.setObjectName(u"fr_search")
        self.fr_search.setFrameShape(QFrame.NoFrame)
        self.fr_search.setFrameShadow(QFrame.Raised)
        self.hl_search = QHBoxLayout(self.fr_search)
        self.hl_search.setObjectName(u"hl_search")
        self.hl_search.setContentsMargins(0, 0, 0, 0)
        self.cb_search = QComboBox(self.fr_search)
        self.cb_search.addItem("")
        self.cb_search.addItem("")
        self.cb_search.addItem("")
        self.cb_search.setObjectName(u"cb_search")
        self.cb_search.setMinimumSize(QSize(110, 0))

        self.hl_search.addWidget(self.cb_search)

        self.le_search = QLineEdit(self.fr_search)
        self.le_search.setObjectName(u"le_search")
        self.le_search.setMaxLength(20)
        self.le_search.setFrame(True)

        self.hl_search.addWidget(self.le_search)

        self.pb_search = QPushButton(self.fr_search)
        self.pb_search.setObjectName(u"pb_search")

        self.hl_search.addWidget(self.pb_search)


        self.verticalLayout.addWidget(self.fr_search)

        self.fr_search_options = QFrame(DataOut)
        self.fr_search_options.setObjectName(u"fr_search_options")
        self.fr_search_options.setFrameShape(QFrame.NoFrame)
        self.fr_search_options.setFrameShadow(QFrame.Raised)
        self.hl_options = QHBoxLayout(self.fr_search_options)
        self.hl_options.setObjectName(u"hl_options")
        self.hl_options.setContentsMargins(0, 0, -1, 0)
        self.l_customer = QLabel(self.fr_search_options)
        self.l_customer.setObjectName(u"l_customer")
        self.l_customer.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hl_options.addWidget(self.l_customer)

        self.le_customer = QLineEdit(self.fr_search_options)
        self.le_customer.setObjectName(u"le_customer")
        self.le_customer.setMinimumSize(QSize(0, 0))
        self.le_customer.setMaxLength(20)

        self.hl_options.addWidget(self.le_customer)

        self.l_date_from = QLabel(self.fr_search_options)
        self.l_date_from.setObjectName(u"l_date_from")
        self.l_date_from.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hl_options.addWidget(self.l_date_from)

        self.date_from = QDateEdit(self.fr_search_options)
        self.date_from.setObjectName(u"date_from")
        self.date_from.setDateTime(QDateTime(QDate(2022, 1, 1), QTime(0, 0, 0)))
        self.date_from.setCalendarPopup(True)

        self.hl_options.addWidget(self.date_from)

        self.l_date_to = QLabel(self.fr_search_options)
        self.l_date_to.setObjectName(u"l_date_to")
        self.l_date_to.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hl_options.addWidget(self.l_date_to)

        self.date_to = QDateEdit(self.fr_search_options)
        self.date_to.setObjectName(u"date_to")
        self.date_to.setMinimumSize(QSize(0, 0))
        self.date_to.setDateTime(QDateTime(QDate(2220, 12, 31), QTime(0, 0, 0)))
        self.date_to.setCalendarPopup(True)

        self.hl_options.addWidget(self.date_to)

        self.h_spacer_options = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_options.addItem(self.h_spacer_options)

        self.tb_csv = QToolButton(self.fr_search_options)
        self.tb_csv.setObjectName(u"tb_csv")

        self.hl_options.addWidget(self.tb_csv)


        self.verticalLayout.addWidget(self.fr_search_options)

        self.tree_orders = QTreeView(DataOut)
        self.tree_orders.setObjectName(u"tree_orders")
        self.tree_orders.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout.addWidget(self.tree_orders)

        self.fr_buttons = QFrame(DataOut)
        self.fr_buttons.setObjectName(u"fr_buttons")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fr_buttons.sizePolicy().hasHeightForWidth())
        self.fr_buttons.setSizePolicy(sizePolicy)
        self.fr_buttons.setFrameShape(QFrame.NoFrame)
        self.fr_buttons.setFrameShadow(QFrame.Raised)
        self.hl_buttons = QHBoxLayout(self.fr_buttons)
        self.hl_buttons.setObjectName(u"hl_buttons")
        self.hl_buttons.setContentsMargins(0, 0, 0, 0)
        self.pb_as_folder = QPushButton(self.fr_buttons)
        self.pb_as_folder.setObjectName(u"pb_as_folder")
        self.pb_as_folder.setEnabled(True)

        self.hl_buttons.addWidget(self.pb_as_folder)

        self.pb_as_file = QPushButton(self.fr_buttons)
        self.pb_as_file.setObjectName(u"pb_as_file")
        self.pb_as_file.setEnabled(True)

        self.hl_buttons.addWidget(self.pb_as_file)

        self.hspacer_btns = QSpacerItem(330, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_buttons.addItem(self.hspacer_btns)


        self.verticalLayout.addWidget(self.fr_buttons)

        QWidget.setTabOrder(self.cb_search, self.le_search)
        QWidget.setTabOrder(self.le_search, self.pb_search)
        QWidget.setTabOrder(self.pb_search, self.le_customer)
        QWidget.setTabOrder(self.le_customer, self.date_from)
        QWidget.setTabOrder(self.date_from, self.date_to)
        QWidget.setTabOrder(self.date_to, self.tree_orders)
        QWidget.setTabOrder(self.tree_orders, self.pb_as_folder)
        QWidget.setTabOrder(self.pb_as_folder, self.pb_as_file)

        self.retranslateUi(DataOut)

        QMetaObject.connectSlotsByName(DataOut)
    # setupUi

    def retranslateUi(self, DataOut):
        DataOut.setWindowTitle(QCoreApplication.translate("DataOut", u"Datenabgabe", None))
        self.cb_search.setItemText(0, QCoreApplication.translate("DataOut", u"Bezeichnung", None))
        self.cb_search.setItemText(1, QCoreApplication.translate("DataOut", u"Name", None))
        self.cb_search.setItemText(2, QCoreApplication.translate("DataOut", u"EAN", None))

#if QT_CONFIG(tooltip)
        self.pb_search.setToolTip(QCoreApplication.translate("DataOut", u"Auftrag suchen", None))
#endif // QT_CONFIG(tooltip)
        self.pb_search.setText(QCoreApplication.translate("DataOut", u"Suchen", None))
        self.l_customer.setText(QCoreApplication.translate("DataOut", u"Kunde", None))
#if QT_CONFIG(tooltip)
        self.le_customer.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.l_date_from.setText(QCoreApplication.translate("DataOut", u"von", None))
        self.date_from.setDisplayFormat(QCoreApplication.translate("DataOut", u"dd.MM.yyyy", None))
        self.l_date_to.setText(QCoreApplication.translate("DataOut", u"bis", None))
        self.date_to.setDisplayFormat(QCoreApplication.translate("DataOut", u"dd.MM.yyyy", None))
#if QT_CONFIG(tooltip)
        self.tb_csv.setToolTip(QCoreApplication.translate("DataOut", u"Auftragsliste als CSV exportieren", None))
#endif // QT_CONFIG(tooltip)
        self.tb_csv.setText(QCoreApplication.translate("DataOut", u"...", None))
#if QT_CONFIG(tooltip)
        self.tree_orders.setToolTip(QCoreApplication.translate("DataOut", u"Tabelle f\u00fcr Auftr\u00e4ge", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pb_as_folder.setToolTip(QCoreApplication.translate("DataOut", u"Bilder als Ordner abgeben", None))
#endif // QT_CONFIG(tooltip)
        self.pb_as_folder.setText(QCoreApplication.translate("DataOut", u"als Ordner", None))
#if QT_CONFIG(tooltip)
        self.pb_as_file.setToolTip(QCoreApplication.translate("DataOut", u"Bilder als Zip-Datei abgeben", None))
#endif // QT_CONFIG(tooltip)
        self.pb_as_file.setText(QCoreApplication.translate("DataOut", u"als Zip", None))
    # retranslateUi

