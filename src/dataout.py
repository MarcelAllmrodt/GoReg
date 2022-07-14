from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QIcon, QContextMenuEvent

from src.ui_dataout import Ui_DataOut


class DataOut(Ui_DataOut):
    def __init__(self):
        self.widget = QWidget()
        self.setupUi(self.widget)

        self.le_search.returnPressed.connect(self.search)
        self.pb_as_file.clicked.connect(self.export_file)
        self.pb_as_folder.clicked.connect(self.export_folder)
        self.pb_search.clicked.connect(self.search)
        self.tb_csv.setIcon(QIcon('res/icons/csv.ico'))
        self.tree_orders.contextMenuEvent = self.show_menu

    def close(self) -> bool:
        # TODO
        return True

    def export_csv(self) -> None:
        # TODO
        pass

    def export_folder(self) -> None:
        # TODO
        pass

    def export_file(self) -> None:
        # TODO
        pass

    def search(self) -> None:
        # TODO
        pass

    def show_menu(self, event: QContextMenuEvent) -> None:
        # TODO
        pass
