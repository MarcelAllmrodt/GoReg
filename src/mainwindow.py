import threading
import logging
import time

from PySide2.QtWidgets import QMainWindow, QApplication, QMdiSubWindow, QMessageBox
from PySide2.QtGui import QCloseEvent
from PySide2.QtCore import Qt, QCoreApplication, QSettings

from src.ui_mainwindow import Ui_MainWindow
from src.settings import Settings
from src.goodsin import GoodsIn
from src.goodsout import GoodsOut
from src.raw import Raw
from src.edit import Edit
from src.dataout import DataOut
from src.admin import Admin
import src.db as DB


ABOUT = '# TODO'
APPLICATION = 'GoReg'
DOMAIN = 'https://www.tmstudios.de/'
ORGANIZATION = 'tm studios'
VERSION = '0.0.2'
PING_DELAY = 60


class MainWindow(Ui_MainWindow):
    Modules = {
        'gin': GoodsIn,
        'gout': GoodsOut,
        'raw': Raw,
        'edit': Edit,
        'dout': DataOut,
        'admin': Admin
    }

    def __init__(self):
        self.app = QApplication([])
        QCoreApplication.setApplicationName(APPLICATION)
        QCoreApplication.setApplicationVersion(VERSION)
        QCoreApplication.setOrganizationDomain(DOMAIN)
        QCoreApplication.setOrganizationName(ORGANIZATION)
        self.widget = QMainWindow()
        self.setupUi(self.widget)
        self.setting = QSettings('GoReg.conf', QSettings.IniFormat)

        self.modules = {}

        self.action_settings.triggered.connect(self.show_settings)
        self.action_login.triggered.connect(self.login)
        self.action_logout.triggered.connect(self.logout)
        self.action_goods_in.triggered.connect(
            lambda: self.add_module('gin'))
        self.action_goods_out.triggered.connect(
            lambda: self.add_module('gout'))
        self.action_raw.triggered.connect(lambda: self.add_module('raw'))
        self.action_edit.triggered.connect(lambda: self.add_module('edit'))
        self.action_do.triggered.connect(lambda: self.add_module('dout'))
        self.action_admin.triggered.connect(lambda: self.add_module('admin'))
        self.action_aboutqt.triggered.connect(
            lambda: QMessageBox.aboutQt(self.widget))
        self.action_about.triggered.connect(
            lambda: QMessageBox.about(
                self.widget, APPLICATION, '\n'.join([VERSION, ORGANIZATION, ABOUT])))
        self.widget.closeEvent = self.on_quit

        self.do_ping = False
        self.ping_thread = None

        self.widget.show()
        self.app.exec_()

    def add_module(self, name: str) -> None:
        if name not in self.modules:
            self.modules[name] = self.Modules[name]()
            widget = self.modules[name].widget
            window = QMdiSubWindow(self.mdiArea)
            window.setWidget(widget)
            window.closeEvent = lambda evt: self.close_widget(name, evt)
            window.resize(640, 480)

            self.mdiArea.addSubWindow(window)
            widget.show()

    def close_widget(self, name: str, event: QCloseEvent) -> None:
        module = self.modules[name]
        if module.close() == True:
            self.modules.pop(name)
            event.accept()
        else:
            event.ignore()

    def login(self) -> bool:
        config = {
            'host': self.setting.value('database/address'),
            'port': self.setting.value('database/port'),
            'database': 'GoReg',
            'user': self.setting.value('database/user'),
            'password': self.setting.value('database/password')
        }

        if config['host'] == None:
            QMessageBox.critical(self.widget,
                                 'Fehler',
                                 'Software wurde noch nicht konfiguriert')
            return False

        try:
            DB.connect(config)
        except DB.MySQL.Error as err:
            QMessageBox.critical(self.widget,
                                 'Fehler',
                                 'Keine Verbindung zur Datenbank')
            return False

        self.ping_thread = threading.Thread(target=self.ping)
        self.do_ping = True
        self.ping_thread.start()

        self.action_login.setDisabled(True)
        self.action_logout.setDisabled(False)
        self.action_settings.setDisabled(True)
        self.action_admin.setDisabled(False)
        self.action_do.setDisabled(False)
        self.action_edit.setDisabled(False)
        self.action_goods_in.setDisabled(False)
        self.action_goods_out.setDisabled(False)
        self.action_raw.setDisabled(False)

        self.statusbar.showMessage('Verbunden mit Datenbank', 10000)
        return True

    def logout(self) -> bool:
        do_close = True
        arr = [x for x in self.modules.values()]
        for module in arr:
            do_close &= module.widget.parentWidget().close()
        if not do_close:
            return False

        try:
            DB.disconnect()
        except DB.MySQL.Error as err:
            QMessageBox(self.widget, 'Fehler',
                        'Keine Verbindung zur Datenbank')
            return False

        self.do_ping = False
        if self.ping_thread is not None:
            if self.ping_thread.is_alive():
                self.ping_thread.join()

        self.action_login.setDisabled(False)
        self.action_logout.setDisabled(True)
        self.action_settings.setDisabled(False)
        self.action_admin.setDisabled(True)
        self.action_do.setDisabled(True)
        self.action_edit.setDisabled(True)
        self.action_goods_in.setDisabled(True)
        self.action_goods_out.setDisabled(True)
        self.action_raw.setDisabled(True)

        self.statusbar.showMessage('Verbindung zur Datenbank beendet', 10000)
        return True

    def on_quit(self, event: QCloseEvent) -> None:
        if self.logout():
            event.accept()
        else:
            event.ignore()

    def ping(self) -> None:
        delay = 0
        while self.do_ping:
            if delay < PING_DELAY:
                delay += 1
                time.sleep(1)
            else:
                delay = 0
                DB.ping()

    def show_settings(self):
        dialog = Settings(self.widget)
        # TODO

