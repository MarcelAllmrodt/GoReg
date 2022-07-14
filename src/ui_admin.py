# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_admin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ressource_rc

class Ui_Admin(object):
    def setupUi(self, Admin):
        if not Admin.objectName():
            Admin.setObjectName(u"Admin")
        Admin.resize(640, 480)
        self.verticalLayout = QVBoxLayout(Admin)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fr_search = QFrame(Admin)
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

        self.fr_search_options = QFrame(Admin)
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

        self.cb_date = QCheckBox(self.fr_search_options)
        self.cb_date.setObjectName(u"cb_date")

        self.hl_options.addWidget(self.cb_date)

        self.date_from = QDateEdit(self.fr_search_options)
        self.date_from.setObjectName(u"date_from")
        self.date_from.setEnabled(False)
        self.date_from.setDateTime(QDateTime(QDate(2022, 1, 1), QTime(0, 0, 0)))
        self.date_from.setCalendarPopup(True)

        self.hl_options.addWidget(self.date_from)

        self.l_date_to = QLabel(self.fr_search_options)
        self.l_date_to.setObjectName(u"l_date_to")
        self.l_date_to.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hl_options.addWidget(self.l_date_to)

        self.date_to = QDateEdit(self.fr_search_options)
        self.date_to.setObjectName(u"date_to")
        self.date_to.setEnabled(False)
        self.date_to.setMinimumSize(QSize(0, 0))
        self.date_to.setDateTime(QDateTime(QDate(2220, 12, 31), QTime(0, 0, 0)))
        self.date_to.setCalendarPopup(True)

        self.hl_options.addWidget(self.date_to)

        self.le_status = QLabel(self.fr_search_options)
        self.le_status.setObjectName(u"le_status")

        self.hl_options.addWidget(self.le_status)

        self.cb_status = QComboBox(self.fr_search_options)
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.setObjectName(u"cb_status")

        self.hl_options.addWidget(self.cb_status)

        self.hspacer_options = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_options.addItem(self.hspacer_options)


        self.verticalLayout.addWidget(self.fr_search_options)

        self.fr_buttons = QFrame(Admin)
        self.fr_buttons.setObjectName(u"fr_buttons")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fr_buttons.sizePolicy().hasHeightForWidth())
        self.fr_buttons.setSizePolicy(sizePolicy)
        self.fr_buttons.setFrameShape(QFrame.NoFrame)
        self.fr_buttons.setFrameShadow(QFrame.Raised)
        self.hlayout_buttons = QHBoxLayout(self.fr_buttons)
        self.hlayout_buttons.setObjectName(u"hlayout_buttons")
        self.hlayout_buttons.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.hlayout_buttons.setContentsMargins(0, 0, 0, 0)
        self.tb_lock = QToolButton(self.fr_buttons)
        self.tb_lock.setObjectName(u"tb_lock")
        icon = QIcon()
        icon.addFile(u":/icons/icons/lock.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.tb_lock.setIcon(icon)

        self.hlayout_buttons.addWidget(self.tb_lock)

        self.tb_reset = QToolButton(self.fr_buttons)
        self.tb_reset.setObjectName(u"tb_reset")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/reset.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.tb_reset.setIcon(icon1)

        self.hlayout_buttons.addWidget(self.tb_reset)

        self.vline_buttons_1 = QFrame(self.fr_buttons)
        self.vline_buttons_1.setObjectName(u"vline_buttons_1")
        self.vline_buttons_1.setFrameShape(QFrame.VLine)
        self.vline_buttons_1.setFrameShadow(QFrame.Sunken)

        self.hlayout_buttons.addWidget(self.vline_buttons_1)

        self.tb_import_csv = QToolButton(self.fr_buttons)
        self.tb_import_csv.setObjectName(u"tb_import_csv")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/csv.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.tb_import_csv.setIcon(icon2)

        self.hlayout_buttons.addWidget(self.tb_import_csv)

        self.tb_import_xml = QToolButton(self.fr_buttons)
        self.tb_import_xml.setObjectName(u"tb_import_xml")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/xml.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.tb_import_xml.setIcon(icon3)

        self.hlayout_buttons.addWidget(self.tb_import_xml)

        self.vline_buttons_2 = QFrame(self.fr_buttons)
        self.vline_buttons_2.setObjectName(u"vline_buttons_2")
        self.vline_buttons_2.setFrameShape(QFrame.VLine)
        self.vline_buttons_2.setFrameShadow(QFrame.Sunken)

        self.hlayout_buttons.addWidget(self.vline_buttons_2)

        self.tb_new_article = QToolButton(self.fr_buttons)
        self.tb_new_article.setObjectName(u"tb_new_article")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/article.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.tb_new_article.setIcon(icon4)

        self.hlayout_buttons.addWidget(self.tb_new_article)

        self.tb_new_order = QToolButton(self.fr_buttons)
        self.tb_new_order.setObjectName(u"tb_new_order")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/order.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.tb_new_order.setIcon(icon5)

        self.hlayout_buttons.addWidget(self.tb_new_order)

        self.vline_buttons_3 = QFrame(self.fr_buttons)
        self.vline_buttons_3.setObjectName(u"vline_buttons_3")
        self.vline_buttons_3.setFrameShape(QFrame.VLine)
        self.vline_buttons_3.setFrameShadow(QFrame.Sunken)

        self.hlayout_buttons.addWidget(self.vline_buttons_3)

        self.tb_export = QToolButton(self.fr_buttons)
        self.tb_export.setObjectName(u"tb_export")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/export.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.tb_export.setIcon(icon6)

        self.hlayout_buttons.addWidget(self.tb_export)

        self.tb_remove = QToolButton(self.fr_buttons)
        self.tb_remove.setObjectName(u"tb_remove")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/remove.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.tb_remove.setIcon(icon7)

        self.hlayout_buttons.addWidget(self.tb_remove)

        self.tb_clear = QToolButton(self.fr_buttons)
        self.tb_clear.setObjectName(u"tb_clear")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/clear.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.tb_clear.setIcon(icon8)

        self.hlayout_buttons.addWidget(self.tb_clear)

        self.hspacer_buttons = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlayout_buttons.addItem(self.hspacer_buttons)


        self.verticalLayout.addWidget(self.fr_buttons)

        self.tree_articles = QTreeView(Admin)
        self.tree_articles.setObjectName(u"tree_articles")
        self.tree_articles.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tree_articles.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tree_articles.setAutoExpandDelay(0)
        self.tree_articles.setSortingEnabled(True)
        self.tree_articles.header().setVisible(True)

        self.verticalLayout.addWidget(self.tree_articles)

        QWidget.setTabOrder(self.cb_search, self.le_search)
        QWidget.setTabOrder(self.le_search, self.pb_search)
        QWidget.setTabOrder(self.pb_search, self.le_customer)
        QWidget.setTabOrder(self.le_customer, self.cb_date)
        QWidget.setTabOrder(self.cb_date, self.date_from)
        QWidget.setTabOrder(self.date_from, self.date_to)
        QWidget.setTabOrder(self.date_to, self.cb_status)
        QWidget.setTabOrder(self.cb_status, self.tb_lock)
        QWidget.setTabOrder(self.tb_lock, self.tb_reset)
        QWidget.setTabOrder(self.tb_reset, self.tb_import_csv)
        QWidget.setTabOrder(self.tb_import_csv, self.tb_import_xml)
        QWidget.setTabOrder(self.tb_import_xml, self.tb_new_article)
        QWidget.setTabOrder(self.tb_new_article, self.tb_new_order)
        QWidget.setTabOrder(self.tb_new_order, self.tb_export)
        QWidget.setTabOrder(self.tb_export, self.tb_remove)
        QWidget.setTabOrder(self.tb_remove, self.tb_clear)
        QWidget.setTabOrder(self.tb_clear, self.tree_articles)

        self.retranslateUi(Admin)
        self.cb_date.toggled.connect(self.date_from.setEnabled)
        self.cb_date.toggled.connect(self.date_to.setEnabled)

        QMetaObject.connectSlotsByName(Admin)
    # setupUi

    def retranslateUi(self, Admin):
        Admin.setWindowTitle(QCoreApplication.translate("Admin", u"Administration", None))
        self.cb_search.setItemText(0, QCoreApplication.translate("Admin", u"Bezeichnung", None))
        self.cb_search.setItemText(1, QCoreApplication.translate("Admin", u"Name", None))
        self.cb_search.setItemText(2, QCoreApplication.translate("Admin", u"EAN", None))
        self.cb_search.setItemText(3, QCoreApplication.translate("Admin", u"Artikel-UUID", None))

#if QT_CONFIG(tooltip)
        self.pb_search.setToolTip(QCoreApplication.translate("Admin", u"Artikel und Auftr\u00e4ge suchen", None))
#endif // QT_CONFIG(tooltip)
        self.pb_search.setText(QCoreApplication.translate("Admin", u"Suchen", None))
        self.l_customer.setText(QCoreApplication.translate("Admin", u"Kunde", None))
#if QT_CONFIG(tooltip)
        self.le_customer.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.cb_date.setText(QCoreApplication.translate("Admin", u"WE", None))
        self.date_from.setDisplayFormat(QCoreApplication.translate("Admin", u"dd.MM.yyyy", None))
        self.l_date_to.setText(QCoreApplication.translate("Admin", u"bis", None))
        self.date_to.setDisplayFormat(QCoreApplication.translate("Admin", u"dd.MM.yyyy", None))
        self.le_status.setText(QCoreApplication.translate("Admin", u"Status", None))
        self.cb_status.setItemText(0, QCoreApplication.translate("Admin", u"-", None))
        self.cb_status.setItemText(1, QCoreApplication.translate("Admin", u"Auftrag offen", None))
        self.cb_status.setItemText(2, QCoreApplication.translate("Admin", u"Auftrag gesperrt", None))
        self.cb_status.setItemText(3, QCoreApplication.translate("Admin", u"WE ja", None))
        self.cb_status.setItemText(4, QCoreApplication.translate("Admin", u"WE nein", None))
        self.cb_status.setItemText(5, QCoreApplication.translate("Admin", u"WA ja", None))
        self.cb_status.setItemText(6, QCoreApplication.translate("Admin", u"WA nein", None))
        self.cb_status.setItemText(7, QCoreApplication.translate("Admin", u"Artikel offen", None))
        self.cb_status.setItemText(8, QCoreApplication.translate("Admin", u"Artikel gesperrt", None))
        self.cb_status.setItemText(9, QCoreApplication.translate("Admin", u"Foto offen", None))
        self.cb_status.setItemText(10, QCoreApplication.translate("Admin", u"Foto neu", None))
        self.cb_status.setItemText(11, QCoreApplication.translate("Admin", u"Foto unbeendet", None))
        self.cb_status.setItemText(12, QCoreApplication.translate("Admin", u"Foto abgschlossen", None))
        self.cb_status.setItemText(13, QCoreApplication.translate("Admin", u"EBV offen", None))
        self.cb_status.setItemText(14, QCoreApplication.translate("Admin", u"EBV neu", None))
        self.cb_status.setItemText(15, QCoreApplication.translate("Admin", u"EBV unbeendet", None))
        self.cb_status.setItemText(16, QCoreApplication.translate("Admin", u"EBV abgschlossen", None))
        self.cb_status.setItemText(17, QCoreApplication.translate("Admin", u"DA offen", None))
        self.cb_status.setItemText(18, QCoreApplication.translate("Admin", u"DA abgschlossen", None))

#if QT_CONFIG(tooltip)
        self.tb_lock.setToolTip(QCoreApplication.translate("Admin", u"Auftrag/Artikel sperren", None))
#endif // QT_CONFIG(tooltip)
        self.tb_lock.setText(QCoreApplication.translate("Admin", u"...", None))
#if QT_CONFIG(tooltip)
        self.tb_reset.setToolTip(QCoreApplication.translate("Admin", u"Auftrag r\u00fccksetzen", None))
#endif // QT_CONFIG(tooltip)
        self.tb_reset.setText(QCoreApplication.translate("Admin", u"...", None))
#if QT_CONFIG(tooltip)
        self.tb_import_csv.setToolTip(QCoreApplication.translate("Admin", u"Artikel/Auftr\u00e4ge per CSV importieren", None))
#endif // QT_CONFIG(tooltip)
        self.tb_import_csv.setText(QCoreApplication.translate("Admin", u"...", None))
#if QT_CONFIG(tooltip)
        self.tb_import_xml.setToolTip(QCoreApplication.translate("Admin", u"Artikel/Auftr\u00e4ge per XML importieren", None))
#endif // QT_CONFIG(tooltip)
        self.tb_import_xml.setText(QCoreApplication.translate("Admin", u"...", None))
#if QT_CONFIG(tooltip)
        self.tb_new_article.setToolTip(QCoreApplication.translate("Admin", u"neuen Artikel anlegen", None))
#endif // QT_CONFIG(tooltip)
        self.tb_new_article.setText(QCoreApplication.translate("Admin", u"...", None))
#if QT_CONFIG(tooltip)
        self.tb_new_order.setToolTip(QCoreApplication.translate("Admin", u"neuen Auftrag anlegen", None))
#endif // QT_CONFIG(tooltip)
        self.tb_new_order.setText(QCoreApplication.translate("Admin", u"...", None))
#if QT_CONFIG(tooltip)
        self.tb_export.setToolTip(QCoreApplication.translate("Admin", u"Tabelle als JSON exportieren", None))
#endif // QT_CONFIG(tooltip)
        self.tb_export.setText(QCoreApplication.translate("Admin", u"...", None))
#if QT_CONFIG(tooltip)
        self.tb_remove.setToolTip(QCoreApplication.translate("Admin", u"Eintrag aus Tabelle entfernen", None))
#endif // QT_CONFIG(tooltip)
        self.tb_remove.setText(QCoreApplication.translate("Admin", u"...", None))
#if QT_CONFIG(tooltip)
        self.tb_clear.setToolTip(QCoreApplication.translate("Admin", u"Tabelle leeren", None))
#endif // QT_CONFIG(tooltip)
        self.tb_clear.setText(QCoreApplication.translate("Admin", u"...", None))
#if QT_CONFIG(tooltip)
        self.tree_articles.setToolTip(QCoreApplication.translate("Admin", u"Tabelle mit Artikeln und deren Auftr\u00e4ge", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

