# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ressource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setLocale(QLocale(QLocale.German, QLocale.Germany))
        self.action_settings = QAction(MainWindow)
        self.action_settings.setObjectName(u"action_settings")
        self.action_quit = QAction(MainWindow)
        self.action_quit.setObjectName(u"action_quit")
        self.action_goods_in = QAction(MainWindow)
        self.action_goods_in.setObjectName(u"action_goods_in")
        self.action_goods_in.setEnabled(False)
        self.action_goods_out = QAction(MainWindow)
        self.action_goods_out.setObjectName(u"action_goods_out")
        self.action_goods_out.setEnabled(False)
        self.action_raw = QAction(MainWindow)
        self.action_raw.setObjectName(u"action_raw")
        self.action_raw.setEnabled(False)
        self.action_edit = QAction(MainWindow)
        self.action_edit.setObjectName(u"action_edit")
        self.action_edit.setEnabled(False)
        self.action_do = QAction(MainWindow)
        self.action_do.setObjectName(u"action_do")
        self.action_do.setEnabled(False)
        self.action_admin = QAction(MainWindow)
        self.action_admin.setObjectName(u"action_admin")
        self.action_admin.setEnabled(False)
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_logger = QAction(MainWindow)
        self.action_logger.setObjectName(u"action_logger")
        self.action_aboutqt = QAction(MainWindow)
        self.action_aboutqt.setObjectName(u"action_aboutqt")
        self.action_login = QAction(MainWindow)
        self.action_login.setObjectName(u"action_login")
        self.action_logout = QAction(MainWindow)
        self.action_logout.setObjectName(u"action_logout")
        self.action_logout.setEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")
        brush = QBrush(QColor(200, 200, 200, 255))
        brush.setStyle(Qt.SolidPattern)
        self.mdiArea.setBackground(brush)
        self.mdiArea.setDocumentMode(True)
        self.mdiArea.setTabsClosable(True)
        self.mdiArea.setTabsMovable(True)

        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_file.setLocale(QLocale(QLocale.German, QLocale.Germany))
        self.menu_modul = QMenu(self.menubar)
        self.menu_modul.setObjectName(u"menu_modul")
        self.menu_modul.setLocale(QLocale(QLocale.German, QLocale.Germany))
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_help.setLocale(QLocale(QLocale.German, QLocale.Germany))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_modul.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_file.addAction(self.action_settings)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_login)
        self.menu_file.addAction(self.action_logout)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_quit)
        self.menu_modul.addAction(self.action_goods_in)
        self.menu_modul.addAction(self.action_goods_out)
        self.menu_modul.addSeparator()
        self.menu_modul.addAction(self.action_raw)
        self.menu_modul.addAction(self.action_edit)
        self.menu_modul.addAction(self.action_do)
        self.menu_modul.addSeparator()
        self.menu_modul.addAction(self.action_admin)
        self.menu_help.addAction(self.action_aboutqt)
        self.menu_help.addAction(self.action_about)

        self.retranslateUi(MainWindow)
        self.action_quit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GoReg", None))
        self.action_settings.setText(QCoreApplication.translate("MainWindow", u"Einstellung", None))
#if QT_CONFIG(shortcut)
        self.action_settings.setShortcut(QCoreApplication.translate("MainWindow", u"F2", None))
#endif // QT_CONFIG(shortcut)
        self.action_quit.setText(QCoreApplication.translate("MainWindow", u"Ende", None))
#if QT_CONFIG(shortcut)
        self.action_quit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_goods_in.setText(QCoreApplication.translate("MainWindow", u"Wareneingang", None))
#if QT_CONFIG(shortcut)
        self.action_goods_in.setShortcut(QCoreApplication.translate("MainWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.action_goods_out.setText(QCoreApplication.translate("MainWindow", u"Warenausgang", None))
#if QT_CONFIG(shortcut)
        self.action_goods_out.setShortcut(QCoreApplication.translate("MainWindow", u"F6", None))
#endif // QT_CONFIG(shortcut)
        self.action_raw.setText(QCoreApplication.translate("MainWindow", u"Foto", None))
#if QT_CONFIG(shortcut)
        self.action_raw.setShortcut(QCoreApplication.translate("MainWindow", u"F7", None))
#endif // QT_CONFIG(shortcut)
        self.action_edit.setText(QCoreApplication.translate("MainWindow", u"EBV", None))
#if QT_CONFIG(shortcut)
        self.action_edit.setShortcut(QCoreApplication.translate("MainWindow", u"F8", None))
#endif // QT_CONFIG(shortcut)
        self.action_do.setText(QCoreApplication.translate("MainWindow", u"Abgabe", None))
#if QT_CONFIG(shortcut)
        self.action_do.setShortcut(QCoreApplication.translate("MainWindow", u"F9", None))
#endif // QT_CONFIG(shortcut)
        self.action_admin.setText(QCoreApplication.translate("MainWindow", u"Verwaltung", None))
#if QT_CONFIG(shortcut)
        self.action_admin.setShortcut(QCoreApplication.translate("MainWindow", u"F10", None))
#endif // QT_CONFIG(shortcut)
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u00dcber", None))
        self.action_logger.setText(QCoreApplication.translate("MainWindow", u"Logger", None))
        self.action_aboutqt.setText(QCoreApplication.translate("MainWindow", u"\u00dcberQt", None))
        self.action_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
#if QT_CONFIG(shortcut)
        self.action_login.setShortcut(QCoreApplication.translate("MainWindow", u"F3", None))
#endif // QT_CONFIG(shortcut)
        self.action_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
#if QT_CONFIG(shortcut)
        self.action_logout.setShortcut(QCoreApplication.translate("MainWindow", u"F4", None))
#endif // QT_CONFIG(shortcut)
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"Datei", None))
        self.menu_modul.setTitle(QCoreApplication.translate("MainWindow", u"Modul", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"Hilfe", None))
    # retranslateUi

