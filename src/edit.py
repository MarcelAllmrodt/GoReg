from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QIcon, QContextMenuEvent

from src.ui_edit import Ui_Edit


class Edit(Ui_Edit):
    def __init__(self):
        self.widget = QWidget()
        self.setupUi(self.widget)

        self.le_search.returnPressed.connect(self.search)
        self.list_edits.contextMenuEvent = self.show_edit_menu
        self.list_raws.contextMenuEvent = self.show_raw_menu
        self.pb_apply.clicked.connect(self.apply)
        self.pb_cancel.clicked.connect(self.cancel)
        self.pb_insert.clicked.connect(self.insert)
        self.pb_reset.clicked.connect(self.reset)
        self.pb_search.clicked.connect(self.search)
        self.table_orders.contextMenuEvent = self.show_order_menu
        self.tb_csv.clicked.connect(self.export_csv)
        self.tb_csv.setIcon(QIcon('res/icons/csv.ico'))
        self.tb_export.clicked.connect(self.outsourcer_export)
        self.tb_export.setIcon(QIcon('res/icons/export.ico'))
        self.tb_import.clicked.connect(self.outsourcer_import)
        self.tb_import.setIcon(QIcon('res/icons/import.ico'))

    def apply(self) -> None:
        # TODO
        pass

    def cancel(self) -> None:
        # TODO
        pass

    def close(self) -> bool:
        # TODO
        return True

    def export_csv(self) -> None:
        # TODO
        pass

    def insert(self) -> None:
        # TODO
        pass

    def outsourcer_export(self) -> None:
        # TODO
        pass

    def outsourcer_import(self) -> None:
        # TODO
        pass

    def reset(self) -> None:
        # TODO
        pass

    def search(self) -> None:
        # TODO
        pass

    def show_edit_menu(self, event: QContextMenuEvent) -> None:
        # TODO
        pass

    def show_order_menu(self, event: QContextMenuEvent) -> None:
        # TODO
        pass

    def show_raw_menu(self, event: QContextMenuEvent) -> None:
        # TODO
        pass
