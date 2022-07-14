import json

from PySide2.QtWidgets import QDialog, QMainWindow, QLineEdit, QFileDialog
from PySide2.QtGui import QCloseEvent
from PySide2.QtCore import QSettings

from src.ui_settings import Ui_Settings


class Settings(Ui_Settings):
    def __init__(self, parent: QMainWindow):
        self.widget = QDialog(parent)
        self.setupUi(self.widget)
        self.setting = QSettings('GoReg.conf', QSettings.IniFormat)

        # Signal/Slots
        self.pb_daydir.clicked.connect(
            lambda: self.locate_dir(self.le_daydir))
        self.pb_export.clicked.connect(self.do_export)
        self.pb_import.clicked.connect(self.do_import)
        self.pb_serverdir.clicked.connect(
            lambda: self.locate_dir(self.le_serverdir))
        self.pb_tempdir.clicked.connect(
            lambda: self.locate_dir(self.le_tempdir))
        self.widget.accepted.connect(lambda: self.save(self.setting))

        self.load(self.setting)
        self.widget.exec_()

    def do_export(self) -> None:
        path = QFileDialog.getSaveFileName(
            self.widget, 'Export', 'GoReg.conf', 'Config (*.conf)')[0]
        setting = QSettings(path, QSettings.IniFormat)
        self.save(setting)

    def do_import(self) -> None:
        path = QFileDialog.getOpenFileName(
            self.widget, 'Import', '~', 'Config (*.conf)')[0]
        setting = QSettings(path, QSettings.IniFormat)
        self.load(setting)

    def load(self, setting: QSettings) -> None:
        self.gb_preview.setChecked(
            setting.value('preview', True, type=bool))
        self.sb_preview.setValue(
            setting.value('preview_size', 128, type=int))
        self.le_serverdir.setText(setting.value('dir/server', ''))
        self.le_tempdir.setText(setting.value('dir/temp', ''))
        self.gb_daydir.setChecked(setting.value('daydir', True, type=bool))
        self.le_daydir.setText(setting.value('dir/day', ''))
        self.le_address.setText(setting.value('database/address', ''))
        self.sb_port.setValue(setting.value(
            'database/port', 3306, type=int))
        self.le_user.setText(setting.value('database/user', ''))
        self.le_password.setText(setting.value('database/password', ''))

    def locate_dir(self, widget: QLineEdit) -> None:
        path = QFileDialog.getExistingDirectory(
            self.widget,
            'Ordner auswählen',
            '~',
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )
        widget.setText(path)

    def save(self, setting: QSettings) -> None:
        setting.setValue('preview', self.gb_preview.isChecked())
        setting.setValue('preview_size', self.sb_preview.value())
        setting.setValue('dir/server', self.le_serverdir.text())
        setting.setValue('dir/temp', self.le_tempdir.text())
        setting.setValue('daydir', self.gb_daydir.isChecked())
        setting.setValue('dir/day', self.le_daydir.text())
        setting.setValue('database/address', self.le_address.text())
        setting.setValue('database/port', self.sb_port.value())
        setting.setValue('database/user', self.le_user.text())
        setting.setValue('database/password', self.le_password.text())
