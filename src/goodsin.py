from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QIcon, QContextMenuEvent

from src.ui_goodsin import Ui_Goods_In


class GoodsIn(Ui_Goods_In):
    def __init__(self):
        self.widget = QWidget()
        self.setupUi(self.widget)

        self.le_search.returnPressed.connect(self.register)
        self.pb_search.clicked.connect(self.register)
        self.table_articles.contextMenuEvent = self.show_menu
        self.tb_csv.clicked.connect(self.export_csv)
        self.tb_csv.setIcon(QIcon('res/icons/csv.ico'))

    def close(self) -> bool:
        # TODO
        return True

    def export_csv(self) -> None:
        # TODO
        pass

    def register(self) -> None:
        # TODO
        pass

    def show_menu(self, event: QContextMenuEvent) -> None:
        # TODO
        pass
