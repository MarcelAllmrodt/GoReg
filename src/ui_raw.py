# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_raw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ressource_rc

class Ui_Raw(object):
    def setupUi(self, Raw):
        if not Raw.objectName():
            Raw.setObjectName(u"Raw")
        Raw.resize(640, 480)
        Raw.setMinimumSize(QSize(0, 0))
        Raw.setLocale(QLocale(QLocale.German, QLocale.Germany))
        self.vl_raw = QVBoxLayout(Raw)
        self.vl_raw.setObjectName(u"vl_raw")
        self.fr_search = QFrame(Raw)
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


        self.vl_raw.addWidget(self.fr_search)

        self.fr_search_options = QFrame(Raw)
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

        self.chk_date = QCheckBox(self.fr_search_options)
        self.chk_date.setObjectName(u"chk_date")
        self.chk_date.setChecked(True)

        self.hl_options.addWidget(self.chk_date)

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

        self.l_state = QLabel(self.fr_search_options)
        self.l_state.setObjectName(u"l_state")

        self.hl_options.addWidget(self.l_state)

        self.cb_state = QComboBox(self.fr_search_options)
        self.cb_state.addItem("")
        self.cb_state.addItem("")
        self.cb_state.addItem("")
        self.cb_state.addItem("")
        self.cb_state.setObjectName(u"cb_state")

        self.hl_options.addWidget(self.cb_state)

        self.h_sapcer_options = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_options.addItem(self.h_sapcer_options)

        self.tb_csv = QToolButton(self.fr_search_options)
        self.tb_csv.setObjectName(u"tb_csv")
        icon = QIcon()
        icon.addFile(u":/icons/icons/csv.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.tb_csv.setIcon(icon)

        self.hl_options.addWidget(self.tb_csv)


        self.vl_raw.addWidget(self.fr_search_options)

        self.spl_tables = QSplitter(Raw)
        self.spl_tables.setObjectName(u"spl_tables")
        self.spl_tables.setOrientation(Qt.Vertical)
        self.spl_tables.setChildrenCollapsible(False)
        self.table_orders = QTableView(self.spl_tables)
        self.table_orders.setObjectName(u"table_orders")
        self.table_orders.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_orders.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_orders.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.spl_tables.addWidget(self.table_orders)
        self.fr_bottom = QFrame(self.spl_tables)
        self.fr_bottom.setObjectName(u"fr_bottom")
        self.fr_bottom.setFrameShape(QFrame.NoFrame)
        self.fr_bottom.setFrameShadow(QFrame.Raised)
        self.vl_bottom = QVBoxLayout(self.fr_bottom)
        self.vl_bottom.setObjectName(u"vl_bottom")
        self.vl_bottom.setContentsMargins(0, 0, 0, 0)
        self.list_images = QListView(self.fr_bottom)
        self.list_images.setObjectName(u"list_images")
        self.list_images.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list_images.setDragDropMode(QAbstractItemView.DropOnly)
        self.list_images.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.vl_bottom.addWidget(self.list_images)

        self.fr_buttons = QFrame(self.fr_bottom)
        self.fr_buttons.setObjectName(u"fr_buttons")
        self.fr_buttons.setFrameShape(QFrame.NoFrame)
        self.fr_buttons.setFrameShadow(QFrame.Raised)
        self.hl_buttons = QHBoxLayout(self.fr_buttons)
        self.hl_buttons.setObjectName(u"hl_buttons")
        self.hl_buttons.setContentsMargins(0, 0, 0, 0)
        self.pb_apply = QPushButton(self.fr_buttons)
        self.pb_apply.setObjectName(u"pb_apply")
        self.pb_apply.setEnabled(False)

        self.hl_buttons.addWidget(self.pb_apply)

        self.pb_insert = QPushButton(self.fr_buttons)
        self.pb_insert.setObjectName(u"pb_insert")
        self.pb_insert.setEnabled(False)

        self.hl_buttons.addWidget(self.pb_insert)

        self.pb_cancel = QPushButton(self.fr_buttons)
        self.pb_cancel.setObjectName(u"pb_cancel")
        self.pb_cancel.setEnabled(False)

        self.hl_buttons.addWidget(self.pb_cancel)

        self.hspacer_btns = QSpacerItem(330, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_buttons.addItem(self.hspacer_btns)


        self.vl_bottom.addWidget(self.fr_buttons)

        self.spl_tables.addWidget(self.fr_bottom)

        self.vl_raw.addWidget(self.spl_tables)


        self.retranslateUi(Raw)

        QMetaObject.connectSlotsByName(Raw)
    # setupUi

    def retranslateUi(self, Raw):
        Raw.setWindowTitle(QCoreApplication.translate("Raw", u"Foto", None))
        self.cb_search.setItemText(0, QCoreApplication.translate("Raw", u"Bezeichnung", None))
        self.cb_search.setItemText(1, QCoreApplication.translate("Raw", u"Name", None))
        self.cb_search.setItemText(2, QCoreApplication.translate("Raw", u"EAN", None))
        self.cb_search.setItemText(3, QCoreApplication.translate("Raw", u"Article-UUID", None))

#if QT_CONFIG(tooltip)
        self.pb_search.setToolTip(QCoreApplication.translate("Raw", u"Auftrag suchen", None))
#endif // QT_CONFIG(tooltip)
        self.pb_search.setText(QCoreApplication.translate("Raw", u"Suchen", None))
        self.l_customer.setText(QCoreApplication.translate("Raw", u"Kunde", None))
#if QT_CONFIG(tooltip)
        self.le_customer.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.chk_date.setText(QCoreApplication.translate("Raw", u"Datum", None))
        self.l_date_from.setText(QCoreApplication.translate("Raw", u"von", None))
        self.date_from.setDisplayFormat(QCoreApplication.translate("Raw", u"dd.MM.yyyy", None))
        self.l_date_to.setText(QCoreApplication.translate("Raw", u"bis", None))
        self.date_to.setDisplayFormat(QCoreApplication.translate("Raw", u"dd.MM.yyyy", None))
        self.l_state.setText(QCoreApplication.translate("Raw", u"Status", None))
        self.cb_state.setItemText(0, QCoreApplication.translate("Raw", u"offen", None))
        self.cb_state.setItemText(1, QCoreApplication.translate("Raw", u"neu", None))
        self.cb_state.setItemText(2, QCoreApplication.translate("Raw", u"unbeendet", None))
        self.cb_state.setItemText(3, QCoreApplication.translate("Raw", u"abgeschlossen", None))

#if QT_CONFIG(tooltip)
        self.tb_csv.setToolTip(QCoreApplication.translate("Raw", u"Auftragsliste als CSV exportieren", None))
#endif // QT_CONFIG(tooltip)
        self.tb_csv.setText(QCoreApplication.translate("Raw", u"...", None))
#if QT_CONFIG(tooltip)
        self.table_orders.setToolTip(QCoreApplication.translate("Raw", u"Auftrag mit Doppelklick ausw\u00e4hlen", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.list_images.setToolTip(QCoreApplication.translate("Raw", u"Bild-Dateien hier herein ziehen", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pb_apply.setToolTip(QCoreApplication.translate("Raw", u"Auftrag abschlie\u00dfen", None))
#endif // QT_CONFIG(tooltip)
        self.pb_apply.setText(QCoreApplication.translate("Raw", u"Abschlie\u00dfen", None))
#if QT_CONFIG(tooltip)
        self.pb_insert.setToolTip(QCoreApplication.translate("Raw", u"\u00c4nderungen \u00fcbernehmen ohne abschlie\u00dfen", None))
#endif // QT_CONFIG(tooltip)
        self.pb_insert.setText(QCoreApplication.translate("Raw", u"\u00dcbernehmen", None))
#if QT_CONFIG(tooltip)
        self.pb_cancel.setToolTip(QCoreApplication.translate("Raw", u"Auftragsbearbeitung abbrechen", None))
#endif // QT_CONFIG(tooltip)
        self.pb_cancel.setText(QCoreApplication.translate("Raw", u"Abbrechen", None))
    # retranslateUi

