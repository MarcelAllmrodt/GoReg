# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_goodsout.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Goods_Out(object):
    def setupUi(self, Goods_Out):
        if not Goods_Out.objectName():
            Goods_Out.setObjectName(u"Goods_Out")
        Goods_Out.resize(640, 480)
        Goods_Out.setLocale(QLocale(QLocale.German, QLocale.Germany))
        self.verticalLayout = QVBoxLayout(Goods_Out)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fr_search = QFrame(Goods_Out)
        self.fr_search.setObjectName(u"fr_search")
        self.fr_search.setFrameShape(QFrame.NoFrame)
        self.fr_search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fr_search)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cb_search = QComboBox(self.fr_search)
        self.cb_search.addItem("")
        self.cb_search.addItem("")
        self.cb_search.addItem("")
        self.cb_search.setObjectName(u"cb_search")
        self.cb_search.setMinimumSize(QSize(110, 0))

        self.horizontalLayout.addWidget(self.cb_search)

        self.le_search = QLineEdit(self.fr_search)
        self.le_search.setObjectName(u"le_search")
        self.le_search.setFrame(True)

        self.horizontalLayout.addWidget(self.le_search)

        self.pb_search = QPushButton(self.fr_search)
        self.pb_search.setObjectName(u"pb_search")

        self.horizontalLayout.addWidget(self.pb_search)


        self.verticalLayout.addWidget(self.fr_search)

        self.fr_search_options = QFrame(Goods_Out)
        self.fr_search_options.setObjectName(u"fr_search_options")
        self.fr_search_options.setFrameShape(QFrame.NoFrame)
        self.fr_search_options.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.fr_search_options)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.l_customer = QLabel(self.fr_search_options)
        self.l_customer.setObjectName(u"l_customer")
        self.l_customer.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.l_customer)

        self.le_customer = QLineEdit(self.fr_search_options)
        self.le_customer.setObjectName(u"le_customer")
        self.le_customer.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.le_customer)

        self.l_date_from = QLabel(self.fr_search_options)
        self.l_date_from.setObjectName(u"l_date_from")
        self.l_date_from.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.l_date_from)

        self.date_from = QDateEdit(self.fr_search_options)
        self.date_from.setObjectName(u"date_from")
        self.date_from.setDateTime(QDateTime(QDate(2022, 1, 1), QTime(0, 0, 0)))
        self.date_from.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.date_from)

        self.l_date_to = QLabel(self.fr_search_options)
        self.l_date_to.setObjectName(u"l_date_to")
        self.l_date_to.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.l_date_to)

        self.date_to = QDateEdit(self.fr_search_options)
        self.date_to.setObjectName(u"date_to")
        self.date_to.setMinimumSize(QSize(0, 0))
        self.date_to.setDateTime(QDateTime(QDate(2220, 12, 31), QTime(0, 0, 0)))
        self.date_to.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.date_to)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.tb_csv = QToolButton(self.fr_search_options)
        self.tb_csv.setObjectName(u"tb_csv")

        self.horizontalLayout_2.addWidget(self.tb_csv)


        self.verticalLayout.addWidget(self.fr_search_options)

        self.table_articles = QTableView(Goods_Out)
        self.table_articles.setObjectName(u"table_articles")
        self.table_articles.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_articles.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.table_articles)

        QWidget.setTabOrder(self.cb_search, self.le_search)
        QWidget.setTabOrder(self.le_search, self.pb_search)
        QWidget.setTabOrder(self.pb_search, self.le_customer)
        QWidget.setTabOrder(self.le_customer, self.date_from)
        QWidget.setTabOrder(self.date_from, self.date_to)
        QWidget.setTabOrder(self.date_to, self.table_articles)

        self.retranslateUi(Goods_Out)

        QMetaObject.connectSlotsByName(Goods_Out)
    # setupUi

    def retranslateUi(self, Goods_Out):
        Goods_Out.setWindowTitle(QCoreApplication.translate("Goods_Out", u"Warenausgang", None))
        self.cb_search.setItemText(0, QCoreApplication.translate("Goods_Out", u"Bezeichnung", None))
        self.cb_search.setItemText(1, QCoreApplication.translate("Goods_Out", u"Name", None))
        self.cb_search.setItemText(2, QCoreApplication.translate("Goods_Out", u"EAN", None))

#if QT_CONFIG(tooltip)
        self.pb_search.setToolTip(QCoreApplication.translate("Goods_Out", u"Artikel im Warenausgang registrieren", None))
#endif // QT_CONFIG(tooltip)
        self.pb_search.setText(QCoreApplication.translate("Goods_Out", u"Registrieren", None))
        self.l_customer.setText(QCoreApplication.translate("Goods_Out", u"Kunde", None))
#if QT_CONFIG(tooltip)
        self.le_customer.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.l_date_from.setText(QCoreApplication.translate("Goods_Out", u"von", None))
        self.date_from.setDisplayFormat(QCoreApplication.translate("Goods_Out", u"dd.MM.yyyy", None))
        self.l_date_to.setText(QCoreApplication.translate("Goods_Out", u"bis", None))
        self.date_to.setDisplayFormat(QCoreApplication.translate("Goods_Out", u"dd.MM.yyyy", None))
#if QT_CONFIG(tooltip)
        self.tb_csv.setToolTip(QCoreApplication.translate("Goods_Out", u"Auftragsliste als CSV exportieren", None))
#endif // QT_CONFIG(tooltip)
        self.tb_csv.setText(QCoreApplication.translate("Goods_Out", u"...", None))
#if QT_CONFIG(tooltip)
        self.table_articles.setToolTip(QCoreApplication.translate("Goods_Out", u"Tabelle von Artikeln", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

