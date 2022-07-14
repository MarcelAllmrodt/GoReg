# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_settings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(251, 466)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Settings.sizePolicy().hasHeightForWidth())
        Settings.setSizePolicy(sizePolicy)
        Settings.setLocale(QLocale(QLocale.German, QLocale.Germany))
        self.vlayout_settings = QVBoxLayout(Settings)
        self.vlayout_settings.setSpacing(6)
        self.vlayout_settings.setObjectName(u"vlayout_settings")
        self.vlayout_settings.setContentsMargins(9, 9, 9, 9)
        self.fr_import_export = QFrame(Settings)
        self.fr_import_export.setObjectName(u"fr_import_export")
        self.hlayout_import_export = QHBoxLayout(self.fr_import_export)
        self.hlayout_import_export.setObjectName(u"hlayout_import_export")
        self.hlayout_import_export.setContentsMargins(0, 0, 0, 0)
        self.pb_import = QPushButton(self.fr_import_export)
        self.pb_import.setObjectName(u"pb_import")

        self.hlayout_import_export.addWidget(self.pb_import)

        self.pb_export = QPushButton(self.fr_import_export)
        self.pb_export.setObjectName(u"pb_export")

        self.hlayout_import_export.addWidget(self.pb_export)

        self.hspacer_import_export = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlayout_import_export.addItem(self.hspacer_import_export)


        self.vlayout_settings.addWidget(self.fr_import_export)

        self.gb_preview = QGroupBox(Settings)
        self.gb_preview.setObjectName(u"gb_preview")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gb_preview.sizePolicy().hasHeightForWidth())
        self.gb_preview.setSizePolicy(sizePolicy1)
        self.gb_preview.setCheckable(True)
        self.flayout_preview = QFormLayout(self.gb_preview)
        self.flayout_preview.setObjectName(u"flayout_preview")
        self.flayout_preview.setHorizontalSpacing(6)
        self.flayout_preview.setVerticalSpacing(6)
        self.flayout_preview.setContentsMargins(0, 0, 0, 0)
        self.l_previewdir = QLabel(self.gb_preview)
        self.l_previewdir.setObjectName(u"l_previewdir")

        self.flayout_preview.setWidget(0, QFormLayout.LabelRole, self.l_previewdir)

        self.sb_preview = QSpinBox(self.gb_preview)
        self.sb_preview.setObjectName(u"sb_preview")
        sizePolicy.setHeightForWidth(self.sb_preview.sizePolicy().hasHeightForWidth())
        self.sb_preview.setSizePolicy(sizePolicy)
        self.sb_preview.setMinimum(64)
        self.sb_preview.setMaximum(256)
        self.sb_preview.setSingleStep(32)
        self.sb_preview.setValue(128)

        self.flayout_preview.setWidget(0, QFormLayout.FieldRole, self.sb_preview)


        self.vlayout_settings.addWidget(self.gb_preview)

        self.gb_server = QGroupBox(Settings)
        self.gb_server.setObjectName(u"gb_server")
        sizePolicy1.setHeightForWidth(self.gb_server.sizePolicy().hasHeightForWidth())
        self.gb_server.setSizePolicy(sizePolicy1)
        self.hlayout_server = QHBoxLayout(self.gb_server)
        self.hlayout_server.setObjectName(u"hlayout_server")
        self.hlayout_server.setContentsMargins(0, 0, 0, 0)
        self.le_serverdir = QLineEdit(self.gb_server)
        self.le_serverdir.setObjectName(u"le_serverdir")

        self.hlayout_server.addWidget(self.le_serverdir)

        self.pb_serverdir = QPushButton(self.gb_server)
        self.pb_serverdir.setObjectName(u"pb_serverdir")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pb_serverdir.sizePolicy().hasHeightForWidth())
        self.pb_serverdir.setSizePolicy(sizePolicy2)
        self.pb_serverdir.setMaximumSize(QSize(29, 16777215))
        self.pb_serverdir.setCheckable(False)
        self.pb_serverdir.setFlat(False)

        self.hlayout_server.addWidget(self.pb_serverdir)


        self.vlayout_settings.addWidget(self.gb_server)

        self.gb_tempdir = QGroupBox(Settings)
        self.gb_tempdir.setObjectName(u"gb_tempdir")
        sizePolicy1.setHeightForWidth(self.gb_tempdir.sizePolicy().hasHeightForWidth())
        self.gb_tempdir.setSizePolicy(sizePolicy1)
        self.hlayout_tempdir = QHBoxLayout(self.gb_tempdir)
        self.hlayout_tempdir.setObjectName(u"hlayout_tempdir")
        self.hlayout_tempdir.setContentsMargins(0, 0, 0, 0)
        self.le_tempdir = QLineEdit(self.gb_tempdir)
        self.le_tempdir.setObjectName(u"le_tempdir")

        self.hlayout_tempdir.addWidget(self.le_tempdir)

        self.pb_tempdir = QPushButton(self.gb_tempdir)
        self.pb_tempdir.setObjectName(u"pb_tempdir")
        sizePolicy2.setHeightForWidth(self.pb_tempdir.sizePolicy().hasHeightForWidth())
        self.pb_tempdir.setSizePolicy(sizePolicy2)
        self.pb_tempdir.setMaximumSize(QSize(29, 16777215))
        self.pb_tempdir.setCheckable(False)
        self.pb_tempdir.setFlat(False)

        self.hlayout_tempdir.addWidget(self.pb_tempdir)


        self.vlayout_settings.addWidget(self.gb_tempdir)

        self.gb_daydir = QGroupBox(Settings)
        self.gb_daydir.setObjectName(u"gb_daydir")
        sizePolicy1.setHeightForWidth(self.gb_daydir.sizePolicy().hasHeightForWidth())
        self.gb_daydir.setSizePolicy(sizePolicy1)
        self.gb_daydir.setCheckable(True)
        self.hlayout_daydir = QHBoxLayout(self.gb_daydir)
        self.hlayout_daydir.setObjectName(u"hlayout_daydir")
        self.hlayout_daydir.setContentsMargins(0, 0, 0, 0)
        self.le_daydir = QLineEdit(self.gb_daydir)
        self.le_daydir.setObjectName(u"le_daydir")

        self.hlayout_daydir.addWidget(self.le_daydir)

        self.pb_daydir = QPushButton(self.gb_daydir)
        self.pb_daydir.setObjectName(u"pb_daydir")
        sizePolicy2.setHeightForWidth(self.pb_daydir.sizePolicy().hasHeightForWidth())
        self.pb_daydir.setSizePolicy(sizePolicy2)
        self.pb_daydir.setMaximumSize(QSize(29, 16777215))
        self.pb_daydir.setCheckable(False)
        self.pb_daydir.setFlat(False)

        self.hlayout_daydir.addWidget(self.pb_daydir)


        self.vlayout_settings.addWidget(self.gb_daydir)

        self.gb_database = QGroupBox(Settings)
        self.gb_database.setObjectName(u"gb_database")
        sizePolicy1.setHeightForWidth(self.gb_database.sizePolicy().hasHeightForWidth())
        self.gb_database.setSizePolicy(sizePolicy1)
        self.hlayout_database = QFormLayout(self.gb_database)
        self.hlayout_database.setObjectName(u"hlayout_database")
        self.hlayout_database.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.hlayout_database.setContentsMargins(0, 0, 0, 0)
        self.l_address = QLabel(self.gb_database)
        self.l_address.setObjectName(u"l_address")
        self.l_address.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hlayout_database.setWidget(0, QFormLayout.LabelRole, self.l_address)

        self.le_address = QLineEdit(self.gb_database)
        self.le_address.setObjectName(u"le_address")
        self.le_address.setClearButtonEnabled(False)

        self.hlayout_database.setWidget(0, QFormLayout.FieldRole, self.le_address)

        self.l_port = QLabel(self.gb_database)
        self.l_port.setObjectName(u"l_port")
        self.l_port.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hlayout_database.setWidget(1, QFormLayout.LabelRole, self.l_port)

        self.sb_port = QSpinBox(self.gb_database)
        self.sb_port.setObjectName(u"sb_port")
        sizePolicy.setHeightForWidth(self.sb_port.sizePolicy().hasHeightForWidth())
        self.sb_port.setSizePolicy(sizePolicy)
        self.sb_port.setMinimum(1)
        self.sb_port.setMaximum(65535)
        self.sb_port.setValue(3306)

        self.hlayout_database.setWidget(1, QFormLayout.FieldRole, self.sb_port)

        self.l_user = QLabel(self.gb_database)
        self.l_user.setObjectName(u"l_user")
        self.l_user.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hlayout_database.setWidget(2, QFormLayout.LabelRole, self.l_user)

        self.le_user = QLineEdit(self.gb_database)
        self.le_user.setObjectName(u"le_user")

        self.hlayout_database.setWidget(2, QFormLayout.FieldRole, self.le_user)

        self.l_password = QLabel(self.gb_database)
        self.l_password.setObjectName(u"l_password")
        self.l_password.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hlayout_database.setWidget(3, QFormLayout.LabelRole, self.l_password)

        self.le_password = QLineEdit(self.gb_database)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.hlayout_database.setWidget(3, QFormLayout.FieldRole, self.le_password)


        self.vlayout_settings.addWidget(self.gb_database)

        self.fr_buttons = QFrame(Settings)
        self.fr_buttons.setObjectName(u"fr_buttons")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.fr_buttons.sizePolicy().hasHeightForWidth())
        self.fr_buttons.setSizePolicy(sizePolicy3)
        self.fr_buttons.setFrameShape(QFrame.NoFrame)
        self.fr_buttons.setFrameShadow(QFrame.Raised)
        self.hlayout_buttons = QHBoxLayout(self.fr_buttons)
        self.hlayout_buttons.setObjectName(u"hlayout_buttons")
        self.hlayout_buttons.setContentsMargins(0, 0, 0, 0)
        self.pb_ok = QPushButton(self.fr_buttons)
        self.pb_ok.setObjectName(u"pb_ok")

        self.hlayout_buttons.addWidget(self.pb_ok)

        self.hspacer_buttons = QSpacerItem(48, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlayout_buttons.addItem(self.hspacer_buttons)

        self.pb_cancel = QPushButton(self.fr_buttons)
        self.pb_cancel.setObjectName(u"pb_cancel")

        self.hlayout_buttons.addWidget(self.pb_cancel)


        self.vlayout_settings.addWidget(self.fr_buttons)


        self.retranslateUi(Settings)
        self.pb_ok.clicked.connect(Settings.accept)
        self.pb_cancel.clicked.connect(Settings.reject)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Einstellung", None))
        self.pb_import.setText(QCoreApplication.translate("Settings", u"Import", None))
        self.pb_export.setText(QCoreApplication.translate("Settings", u"Export", None))
        self.gb_preview.setTitle(QCoreApplication.translate("Settings", u"Vorschau", None))
        self.l_previewdir.setText(QCoreApplication.translate("Settings", u"Vorschaugr\u00f6\u00dfe", None))
        self.sb_preview.setSuffix(QCoreApplication.translate("Settings", u"px", None))
        self.sb_preview.setPrefix("")
        self.gb_server.setTitle(QCoreApplication.translate("Settings", u"Server", None))
        self.pb_serverdir.setText(QCoreApplication.translate("Settings", u"...", None))
        self.gb_tempdir.setTitle(QCoreApplication.translate("Settings", u"Arbeitsordner", None))
        self.pb_tempdir.setText(QCoreApplication.translate("Settings", u"...", None))
        self.gb_daydir.setTitle(QCoreApplication.translate("Settings", u"Tagesordner", None))
        self.pb_daydir.setText(QCoreApplication.translate("Settings", u"...", None))
        self.gb_database.setTitle(QCoreApplication.translate("Settings", u"Datenbank", None))
        self.l_address.setText(QCoreApplication.translate("Settings", u"Adresse", None))
        self.l_port.setText(QCoreApplication.translate("Settings", u"Port", None))
        self.l_user.setText(QCoreApplication.translate("Settings", u"Benutzer", None))
        self.l_password.setText(QCoreApplication.translate("Settings", u"Passwort", None))
        self.pb_ok.setText(QCoreApplication.translate("Settings", u"Ok", None))
        self.pb_cancel.setText(QCoreApplication.translate("Settings", u"Abbrechen", None))
    # retranslateUi

