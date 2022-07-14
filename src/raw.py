from PySide2.QtWidgets import QWidget
from PySide2.QtGui import (
    QIcon, QContextMenuEvent, QStandardItem, QStandardItemModel
)
from PySide2.QtCore import QSettings

from src.ui_raw import Ui_Raw
import src.order
import src.article
import src.db as DB


class Raw(Ui_Raw):
    table_header = [
        'Artikel-UUID',
        'Auftrags-UUID',
        'Bezeichnung',
        'Name',
        'Farbe',
        'Auftragstyp',
        'Wareneingang'
    ]

    def __init__(self):
        self.widget = QWidget()
        self.setupUi(self.widget)

        settings = QSettings()
        self.tmp_dir = settings.value('dir/temp', '')
        self.srv_dir = settings.value('dir/server', '')
        self.use_daydir = settings.value('daydir', True, type=bool)
        self.day_dir = settings.value('dir/day', '')
        self.thumb_size = settings.value('preview_size', 128, type=int)
        self.table_orders.setModel(QStandardItemModel())
        self.table_orders.model().setHorizontalHeaderLabels(self.table_header)

        # Signal/Slots
        self.le_search.returnPressed.connect(self.search)
        self.list_images.contextMenuEvent = self.show_list_menu
        self.table_orders.contextMenuEvent = self.show_order_menu
        self.pb_apply.clicked.connect(self.apply)
        self.pb_cancel.clicked.connect(self.cancel)
        self.pb_insert.clicked.connect(self.insert)
        self.pb_search.clicked.connect(self.search)
        self.tb_csv.setIcon(QIcon('res/icons/csv.ico'))

    def apply(self) -> None:
        # TODO
        pass

    def cancel(self) -> None:
        # TODO
        pass

    def close(self) -> bool:
        # TODO
        return True

    def insert(self) -> None:
        # TODO
        pass

    def search(self) -> None:
        search_box = [
            'ident',
            'name'
            'ean',
            'uuid'
        ]

        text = self.le_search.text()
        index = self.cb_search.currentIndex()
        client = self.le_customer.text()
        use_date = self.chk_date.isChecked()
        date_from = self.date_from.date().toString('yyyyMMdd')
        date_to = self.date_to.date().toString('yyyyMMdd')
        status = self.cb_state.currentIndex()

        params = {}
        params['status'] = self.cb_state.currentIndex() + 9
        if text != '':
            params[search_box[index]] = text
        if client != '':
            params['client'] = client
        if use_date:
            params['datefrom'] = date_from
            params['dateto'] = date_to
        params['status'] = 1

        data = src.article.fetch_articles(**params)
        if len(data) == 0:
            return
        for (uuid, ident, client, colour, name, status,
             inbound_scan, outbound_scan) in data:
            orders = src.order.fetch_order(article_uuid=uuid, status=1)
            if len(orders) == 0:
                continue

            for (_, order_uuid, order_type, raw,
                 edit, dout_ts, order_status) in orders:
                row = [
                    QStandardItem(uuid),
                    QStandardItem(order_uuid),
                    QStandardItem(ident),
                    QStandardItem(name),
                    QStandardItem(colour),
                    QStandardItem(order_type),
                    QStandardItem(inbound_scan)]
                self.table_orders.model().appendRow(row)

    def show_list_menu(self, event: QContextMenuEvent) -> None:
        # TODO
        pass

    def show_order_menu(self, event: QContextMenuEvent) -> None:
        # TODO
        pass
