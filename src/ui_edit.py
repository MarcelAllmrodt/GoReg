# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_edit.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Edit(object):
    def setupUi(self, Edit):
        if not Edit.objectName():
            Edit.setObjectName(u"Edit")
        Edit.resize(640, 480)
        Edit.setMinimumSize(QSize(0, 0))
        Edit.setLocale(QLocale(QLocale.German, QLocale.Germany))
        self.verticalLayout = QVBoxLayout(Edit)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fr_search = QFrame(Edit)
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
        self.le_search.setClearButtonEnabled(False)

        self.hl_search.addWidget(self.le_search)

        self.pb_search = QPushButton(self.fr_search)
        self.pb_search.setObjectName(u"pb_search")

        self.hl_search.addWidget(self.pb_search)


        self.verticalLayout.addWidget(self.fr_search)

        self.fr_search_options = QFrame(Edit)
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

        self.l_state = QLabel(self.fr_search_options)
        self.l_state.setObjectName(u"l_state")

        self.hl_options.addWidget(self.l_state)

        self.comboBox = QComboBox(self.fr_search_options)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.hl_options.addWidget(self.comboBox)

        self.hspacer_options = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_options.addItem(self.hspacer_options)


        self.verticalLayout.addWidget(self.fr_search_options)

        self.fr_oder_buttons = QFrame(Edit)
        self.fr_oder_buttons.setObjectName(u"fr_oder_buttons")
        self.fr_oder_buttons.setFrameShape(QFrame.NoFrame)
        self.fr_oder_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fr_oder_buttons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tb_export = QToolButton(self.fr_oder_buttons)
        self.tb_export.setObjectName(u"tb_export")

        self.horizontalLayout.addWidget(self.tb_export)

        self.tb_import = QToolButton(self.fr_oder_buttons)
        self.tb_import.setObjectName(u"tb_import")

        self.horizontalLayout.addWidget(self.tb_import)

        self.tb_csv = QToolButton(self.fr_oder_buttons)
        self.tb_csv.setObjectName(u"tb_csv")

        self.horizontalLayout.addWidget(self.tb_csv)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.fr_oder_buttons)

        self.splitter = QSplitter(Edit)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.fr_orders = QFrame(self.splitter)
        self.fr_orders.setObjectName(u"fr_orders")
        self.fr_orders.setFrameShape(QFrame.NoFrame)
        self.fr_orders.setFrameShadow(QFrame.Raised)
        self.hlayout_orders = QHBoxLayout(self.fr_orders)
        self.hlayout_orders.setObjectName(u"hlayout_orders")
        self.hlayout_orders.setContentsMargins(0, 0, 0, 0)
        self.table_orders = QTableView(self.fr_orders)
        self.table_orders.setObjectName(u"table_orders")
        self.table_orders.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_orders.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_orders.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.hlayout_orders.addWidget(self.table_orders)

        self.splitter.addWidget(self.fr_orders)
        self.fr_bottom = QFrame(self.splitter)
        self.fr_bottom.setObjectName(u"fr_bottom")
        self.fr_bottom.setFrameShape(QFrame.NoFrame)
        self.fr_bottom.setFrameShadow(QFrame.Raised)
        self.vl_bottom = QVBoxLayout(self.fr_bottom)
        self.vl_bottom.setObjectName(u"vl_bottom")
        self.vl_bottom.setContentsMargins(0, 0, 0, 0)
        self.spl_lists = QSplitter(self.fr_bottom)
        self.spl_lists.setObjectName(u"spl_lists")
        self.spl_lists.setOrientation(Qt.Horizontal)
        self.list_raws = QListView(self.spl_lists)
        self.list_raws.setObjectName(u"list_raws")
        self.list_raws.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list_raws.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.spl_lists.addWidget(self.list_raws)
        self.list_edits = QListView(self.spl_lists)
        self.list_edits.setObjectName(u"list_edits")
        self.list_edits.setDragDropMode(QAbstractItemView.DropOnly)
        self.list_edits.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.spl_lists.addWidget(self.list_edits)

        self.vl_bottom.addWidget(self.spl_lists)

        self.fr_buttons = QFrame(self.fr_bottom)
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
        self.pb_apply = QPushButton(self.fr_buttons)
        self.pb_apply.setObjectName(u"pb_apply")
        self.pb_apply.setEnabled(False)

        self.hl_buttons.addWidget(self.pb_apply)

        self.pb_insert = QPushButton(self.fr_buttons)
        self.pb_insert.setObjectName(u"pb_insert")
        self.pb_insert.setEnabled(False)

        self.hl_buttons.addWidget(self.pb_insert)

        self.pb_reset = QPushButton(self.fr_buttons)
        self.pb_reset.setObjectName(u"pb_reset")
        self.pb_reset.setEnabled(False)

        self.hl_buttons.addWidget(self.pb_reset)

        self.pb_cancel = QPushButton(self.fr_buttons)
        self.pb_cancel.setObjectName(u"pb_cancel")
        self.pb_cancel.setEnabled(False)

        self.hl_buttons.addWidget(self.pb_cancel)

        self.hspace_btns = QSpacerItem(330, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_buttons.addItem(self.hspace_btns)


        self.vl_bottom.addWidget(self.fr_buttons)

        self.splitter.addWidget(self.fr_bottom)

        self.verticalLayout.addWidget(self.splitter)

        QWidget.setTabOrder(self.cb_search, self.le_search)
        QWidget.setTabOrder(self.le_search, self.pb_search)
        QWidget.setTabOrder(self.pb_search, self.le_customer)
        QWidget.setTabOrder(self.le_customer, self.date_from)
        QWidget.setTabOrder(self.date_from, self.date_to)
        QWidget.setTabOrder(self.date_to, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.tb_export)
        QWidget.setTabOrder(self.tb_export, self.tb_import)
        QWidget.setTabOrder(self.tb_import, self.tb_csv)
        QWidget.setTabOrder(self.tb_csv, self.table_orders)
        QWidget.setTabOrder(self.table_orders, self.list_raws)
        QWidget.setTabOrder(self.list_raws, self.list_edits)
        QWidget.setTabOrder(self.list_edits, self.pb_apply)
        QWidget.setTabOrder(self.pb_apply, self.pb_insert)
        QWidget.setTabOrder(self.pb_insert, self.pb_reset)
        QWidget.setTabOrder(self.pb_reset, self.pb_cancel)

        self.retranslateUi(Edit)

        QMetaObject.connectSlotsByName(Edit)
    # setupUi

    def retranslateUi(self, Edit):
        Edit.setWindowTitle(QCoreApplication.translate("Edit", u"EBV", None))
        self.cb_search.setItemText(0, QCoreApplication.translate("Edit", u"Bezeichnung", None))
        self.cb_search.setItemText(1, QCoreApplication.translate("Edit", u"Name", None))
        self.cb_search.setItemText(2, QCoreApplication.translate("Edit", u"EAN", None))

#if QT_CONFIG(tooltip)
        self.pb_search.setToolTip(QCoreApplication.translate("Edit", u"Auftrag suchen", None))
#endif // QT_CONFIG(tooltip)
        self.pb_search.setText(QCoreApplication.translate("Edit", u"Suchen", None))
        self.l_customer.setText(QCoreApplication.translate("Edit", u"Kunde", None))
#if QT_CONFIG(tooltip)
        self.le_customer.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.l_date_from.setText(QCoreApplication.translate("Edit", u"von", None))
        self.date_from.setDisplayFormat(QCoreApplication.translate("Edit", u"dd.MM.yyyy", None))
        self.l_date_to.setText(QCoreApplication.translate("Edit", u"bis", None))
        self.date_to.setDisplayFormat(QCoreApplication.translate("Edit", u"dd.MM.yyyy", None))
        self.l_state.setText(QCoreApplication.translate("Edit", u"Status", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Edit", u"offen", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Edit", u"neu", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Edit", u"unbeendet", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Edit", u"abgeschlossen", None))

#if QT_CONFIG(tooltip)
        self.tb_export.setToolTip(QCoreApplication.translate("Edit", u"Auftr\u00e4ge exportieren f\u00fcr Outsourcer", None))
#endif // QT_CONFIG(tooltip)
        self.tb_export.setText(QCoreApplication.translate("Edit", u"...", None))
#if QT_CONFIG(tooltip)
        self.tb_import.setToolTip(QCoreApplication.translate("Edit", u"Auftr\u00e4ge von Outsourcer importieren", None))
#endif // QT_CONFIG(tooltip)
        self.tb_import.setText(QCoreApplication.translate("Edit", u"...", None))
#if QT_CONFIG(tooltip)
        self.tb_csv.setToolTip(QCoreApplication.translate("Edit", u"Auftragsliste als CSV exportieren", None))
#endif // QT_CONFIG(tooltip)
        self.tb_csv.setText(QCoreApplication.translate("Edit", u"...", None))
#if QT_CONFIG(tooltip)
        self.table_orders.setToolTip(QCoreApplication.translate("Edit", u"Auftrag mit Doppelklick ausw\u00e4hlen", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.list_raws.setToolTip(QCoreApplication.translate("Edit", u"Fotos vom Foto-Modul", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.list_edits.setToolTip(QCoreApplication.translate("Edit", u"Bild-Dateien hier herein ziehen", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pb_apply.setToolTip(QCoreApplication.translate("Edit", u"ausgew\u00e4hlten Auftrag abschlie\u00dfen", None))
#endif // QT_CONFIG(tooltip)
        self.pb_apply.setText(QCoreApplication.translate("Edit", u"Abschlie\u00dfen", None))
#if QT_CONFIG(tooltip)
        self.pb_insert.setToolTip(QCoreApplication.translate("Edit", u"\u00c4nderungen \u00fcbernehmen ohne abschlie\u00dfen", None))
#endif // QT_CONFIG(tooltip)
        self.pb_insert.setText(QCoreApplication.translate("Edit", u"\u00dcbernehmen", None))
#if QT_CONFIG(tooltip)
        self.pb_reset.setToolTip(QCoreApplication.translate("Edit", u"Auftrag auf Foto zur\u00fccksetzen", None))
#endif // QT_CONFIG(tooltip)
        self.pb_reset.setText(QCoreApplication.translate("Edit", u"R\u00fccksetzen", None))
#if QT_CONFIG(tooltip)
        self.pb_cancel.setToolTip(QCoreApplication.translate("Edit", u"Auftragsbearbeitung abbrechen", None))
#endif // QT_CONFIG(tooltip)
        self.pb_cancel.setText(QCoreApplication.translate("Edit", u"Abbrechen", None))
    # retranslateUi

