"""
TODO:
 import_csv()
 import_xml()
"""

import json

from PySide2.QtWidgets import (
    QWidget, QMessageBox, QDialog, QInputDialog, QFileDialog, QMenu, QAction
)
from PySide2.QtGui import (
    QIcon, QContextMenuEvent, QStandardItem, QStandardItemModel, QClipboard
)
from PySide2.QtCore import Qt

from src.ui_admin import Ui_Admin
from src.ui_newarticle import Ui_NewArticle
from src.ui_neworder import Ui_NewOrder
import src.article
import src.order


class Admin(Ui_Admin):
    tree_header = [
        'Uuid',
        'Bezeichnung/Auftragsart',
        'Kunde/Foto',
        'Farbe/EBV',
        'Name/Abgabe',
        'Status',
        'Wareneingang',
        'Warenausgang'
    ]

    def __init__(self):
        self.widget = QWidget()
        self.setupUi(self.widget)

        self.tree_articles.setModel(QStandardItemModel())
        self.tree_articles.model().setHorizontalHeaderLabels(self.tree_header)
        self.articles = []

        # Signal/Slots
        self.le_search.returnPressed.connect(self.search)
        self.pb_search.clicked.connect(self.search)
        self.tb_clear.clicked.connect(self.clear_table)
        self.tb_export.clicked.connect(self.export)
        self.tb_import_csv.clicked.connect(self.import_csv)
        self.tb_import_xml.clicked.connect(self.import_xml)
        self.tb_lock.clicked.connect(self.lock)
        self.tb_new_article.clicked.connect(self.new_article)
        self.tb_new_order.clicked.connect(self.new_order)
        self.tb_remove.clicked.connect(self.remove_entry)
        self.tb_reset.clicked.connect(self.reset)
        self.tree_articles.contextMenuEvent = self.show_menu

    def clear_table(self) -> None:
        self.tree_articles.model().removeRows(
            0, self.tree_articles.model().rowCount()
        )
        self.articles.clear()

    def close(self) -> bool:
        return True

    def export(self) -> None:
        if self.tree_articles.model().rowCount() == 0:
            return

        path, ok = QFileDialog.getSaveFileName(
            self.widget,
            'Speichern',
            '~/export.json',
            'JSON (*.json)'
        )

        if not ok:
            return

        art_head = [
            'Uuid', 'Bezeichnung', 'Kunde', 'Farbe', 'Name',
            'Status', 'Wareneingang', 'Warenausgang'
        ]
        ord_header = [
            'Uuid', 'Art', 'Foto', 'EBV', 'Abgabe', 'Status'
        ]

        data = []
        for i in range(self.tree_articles.model().rowCount()):
            entry = {}
            for j in range(len(art_head)):
                entry[art_head[j]] = self.tree_articles.model().item(
                    i, j).text()
            entry['Auftrag'] = []
            for k in range(self.tree_articles.model().item(i, 0).rowCount()):
                order_entry = {}
                for l in range(len(ord_header)):
                    order_entry[ord_header[l]] = self.tree_articles.model().item(
                        i, 0).child(k, l).text()
                entry['Auftrag'].append(order_entry)
            data.append(entry)

        try:
            file = open(path, 'w')
            json.dump(data, file, indent=' ', separators=(',', ': '))
            file.close()
        except OSError as err:
            QMessageBox.critical(str(err))

    def import_csv(self) -> None:
        # TODO
        pass

    def import_xml(self) -> None:
        # TODO
        pass

    def lock(self) -> None:
        indexes = self.tree_articles.selectionModel().selectedRows(0)
        if len(indexes) == 0:
            return

        ok = QMessageBox.question(
            self.widget,
            'Sperren',
            'gewählte Artikel und Aufträge sperren/reaktivieren?',
            QMessageBox.Yes | QMessageBox.Abort
        )
        if ok == QMessageBox.Abort:
            return

        items = [self.tree_articles.model().itemFromIndex(x)
                 for x in indexes]

        for item in items:
            if item.parent() is not None:
                uuid = item.text()
                status_item = item.parent().child(item.row(), 5)
                status = status_item.data(Qt.UserRole)
                if status == 1:
                    src.order.set_status(uuid, 0)
                    status_item.setData(0, Qt.UserRole)
                    status_item.setText('gesperrt')
                else:
                    src.order.set_status(uuid, 1)
                    status_item.setData(1, Qt.UserRole)
                    status_item.setText('aktiv')

            else:
                uuid = item.text()
                status_item = self.tree_articles.model().item(item.row(), 5)
                status = status_item.data(Qt.UserRole)
                if status == 1:
                    src.article.set_status(uuid, 0)
                    status_item.setData(0, Qt.UserRole)
                    status_item.setText('gesperrt')
                else:
                    src.article.set_status(uuid, 1)
                    status_item.setData(1, Qt.UserRole)
                    status_item.setText('aktiv')

    def new_article(self) -> None:
        widget = QDialog(self.widget)
        dialog = Ui_NewArticle()
        dialog.setupUi(widget)
        dialog.pb_create.clicked.connect(widget.accept)
        dialog.pb_cancel.clicked.connect(widget.reject)
        ok = widget.exec_()
        if ok == QDialog.Rejected:
            return

        ident = dialog.le_ident.text()
        if ident == '':
            QMessageBox.critical(
                self.widget,
                'Fehler',
                '\'Bezeichnung\' darf nicht leer sein'
            )
            return

        client = dialog.le_customer.text()
        if client == '':
            QMessageBox.critical(
                self.widget,
                'Fehler',
                '\'Kunde\' darf nicht leer sein'
            )
            return

        name = dialog.le_name.text()
        colour = dialog.le_colour.text()

        uuid = src.article.insert_article(ident, client, colour, name)
        data = [uuid.upper(), ident, client, colour,
                name, '1', 'None', 'None']
        items = [QStandardItem(x) for x in data]

        self.articles.append(uuid.upper())
        self.tree_articles.model().appendRow(items)
        QMessageBox.information(
            self.widget,
            'Ausgefüht',
            'Auftrag wurde erstellt'
        )

    def new_order(self) -> None:
        indexes = self.tree_articles.selectionModel().selectedRows(0)
        if len(indexes) == 0:
            QMessageBox.warning(
                self.widget,
                'Fehler',
                'keine Artikel ausgewählt'
            )
            return

        items = [self.tree_articles.model().itemFromIndex(index)
                 for index in indexes]
        items = [item for item in items if item.parent() is None]
        if len(items) == 0:
            QMessageBox.warning(
                self.widget,
                'Fehler',
                'keine Artikel ausgewählt'
            )
            return

        order_type, ok = QInputDialog.getText(
            self.widget,
            'Auftragstyp',
            'Auftragstyp:'
        )
        if not ok:
            return
        if order_type == '':
            QMessageBox.critical(
                self.widget,
                'Fehler',
                'Typ darf nicht leer sein'
            )
            return

        count = 0
        for item in items:
            article_uuid = item.text()
            uuid = src.order.insert_order(article_uuid, order_type)
            if uuid != '':
                count += 1
                data = [uuid.upper(), order_type,
                        'None', 'None', 'None', 'aktiv']
                items = [QStandardItem(x) for x in data]
                items[5].setData(1, Qt.UserRole)
                item.appendRow(items)

        QMessageBox.information(
            self.widget,
            'Ausgeführt',
            '%i Auftrag/Aufträge hinzugefügt' % (count)
        )

    def remove_entry(self) -> None:
        indexes = self.tree_articles.selectionModel().selectedRows(0)
        if len(indexes) == 0:
            return

        items = [self.tree_articles.model().itemFromIndex(index)
                 for index in indexes]
        for item in items:
            if item.parent() is not None:
                continue
            uuid = item.text()
            self.tree_articles.model().removeRow(item.row())
            self.articles.remove(uuid)

    def reset(self) -> None:
        indexes = self.tree_articles.selectionModel().selectedRows()
        if len(indexes) == 0:
            return

        ok = QMessageBox.question(
            self.widget,
            'Rücksetzen',
            'ausgewählte Aufträge rücksetzen?',
            QMessageBox.Yes | QMessageBox.Abort
        )
        if ok == QMessageBox.Abort:
            return

        items = [self.tree_articles.model().itemFromIndex(x)
                 for x in indexes]

        for item in items:
            if item.parent() is None:
                continue
            else:
                uuid = item.parent().child(item.row(), 0).text()
                src.order.reset_order(uuid)
                item.parent().child(item.row(), 2).setText('None')
                item.parent().child(item.row(), 3).setText('None')
                item.parent().child(item.row(), 4).setText('None')

    def search(self) -> None:
        search_types = [
            'ident',
            'name',
            'ean',
            'uuid'
        ]

        text = self.le_search.text()
        params = {}
        search_type = search_types[self.cb_search.currentIndex()]
        params[search_type] = text
        params['client'] = self.le_customer.text()
        params['status'] = self.cb_status.currentIndex()
        if self.cb_date.isChecked():
            params['datefrom'] = self.date_from.date().toString('yyyyMMdd')
            params['dateto'] = self.date_to.date().toString('yyyyMMdd')

        articles = src.article.fetch_articles(**params)

        for article in articles:
            uuid = article[0]
            if uuid in self.articles:
                continue

            items = [QStandardItem(str(x)) for x in article]
            if items[5].text() == '1':
                items[5].setText('aktiv')
                items[5].setData(1, Qt.UserRole)
            else:
                items[5].setText('gesperrt')
                items[5].setData(0, Qt.UserRole)

            orders = src.order.fetch_order(article_uuid=uuid)
            for order in orders:
                child_items = [QStandardItem(str(x))
                               for x in order if order.index(x) != 0]
                if child_items[5].text() == '1':
                    child_items[5].setText('aktiv')
                    child_items[5].setData(1, Qt.UserRole)
                else:
                    child_items[5].setText('gesperrt')
                    child_items[5].setData(0, Qt.UserRole)
                items[0].appendRow(child_items)

            self.tree_articles.model().appendRow(items)
            self.articles.append(uuid)

        self.tree_articles.expandAll()

    def show_menu(self, event: QContextMenuEvent) -> None:
        def copy_uuid():
            indexes = self.tree_articles.selectionModel().selectedRows(0)
            if len(indexes) == 0:
                return
            items = [self.tree_articles.model().itemFromIndex(index)
                     for index in indexes]
            uuids = [item.text() for item in items]
            QClipboard().setText(','.join(uuids))

        def copy_ident():
            indexes = self.tree_articles.selectionModel().selectedRows(1)
            if len(indexes) == 0:
                return
            items = [self.tree_articles.model().itemFromIndex(index)
                     for index in indexes]

            idents = []
            for item in items:
                if item.parent() is not None:
                    continue
                idents.append(item.text())
            QClipboard().setText(','.join(idents))

        menu = QMenu()
        action_copy_uuid = QAction('Uuid(s) kopieren')
        action_copy_uuid.triggered.connect(copy_uuid)
        action_copy_ident = QAction('Bezeichnung kopieren')
        action_copy_ident.triggered.connect(copy_ident)
        action_remove_entry = QAction('Einträge entfernen')
        action_remove_entry.triggered.connect(self.remove_entry)
        action_clear_table = QAction('Tabelle leeren')
        action_clear_table.triggered.connect(self.clear_table)

        menu.addAction(action_copy_uuid)
        menu.addAction(action_copy_ident)
        menu.addAction(action_remove_entry)
        menu.addAction(action_clear_table)
        menu.exec_(event.globalPos())
