import logging
import uuid

import src.db as DB


SMT_STATUS = [
    'AND status = 0 ',
    'AND status = 1 '
]

SMT_STATUS_DOUT = [
    'AND dout_ts IS NULL ',
    'AND dout_ts IS NOT NULL '
]

SMT_STATUS_EDIT = [
    'AND edit = 0 or STATUS IS NULL ',
    'AND edit IS NULL ',
    'AND edit = 0 ',
    'AND edit = 1 '
]

SMT_STATUS_RAW = [
    'AND raw = 0 or STATUS IS NULL ',
    'AND raw IS NULL ',
    'AND raw = 0 ',
    'AND raw = 1 '
]


def clear_access_lock() -> bool:
    stmt = (
        'DELETE FROM access_lock;'
    )
    params = {}

    try:
        DB.commit()
        DB.execute(statement=stmt, parameters=params)
        DB.commit()
    except DB.MySQL.Error as err:
        logging.error(str(err))
        DB.rollback()
        return False
    return True


def fetch_order(article_uuid: str = '', ordtype: str = '', raw: int = -1,
                edit: int = -1, dout: int = -1, status: int = -1) -> list:
    stmt = (
        'SELECT HEX(article_uuid), HEX(uuid), type, raw, edit, dout_ts, status '
        'FROM orders '
        'WHERE 1 '
    )
    params = {}

    if article_uuid != '':
        stmt += 'AND article_uuid = x%(article_uuid)s '
        params['article_uuid'] = article_uuid
    if ordtype != '':
        stmt += 'AND type LIKE %(type)s '
        params['type'] = '%' + ordtype + '%'
    if raw != -1:
        stmt += SMT_STATUS_RAW[raw]
    if edit != -1:
        stmt += SMT_STATUS_EDIT[edit]
    if dout != -1:
        stmt += SMT_STATUS_DOUT[dout]
    if status != -1:
        stmt += SMT_STATUS[status]
    stmt += ';'
    print(stmt)

    try:
        DB.commit()
        data = DB.fetchall(statement=stmt, parameters=params)
    except DB.MySQL.Error as err:
        logging.error(str(err))
        DB.rollback()
        return []
    return data


def insert_access_log(uuid: str) -> bool:
    stmt = (
        'INSERT INTO access_lock (order_uuid) VALUES '
        '(x%(uuid)s) '
    )
    params = {'uuid': uuid}

    try:
        DB.commit()
        DB.execute(statement=stmt, parameters=params)
        DB.commit()
    except DB.MySQL.Error as err:
        logging.error(str(err))
        DB.rollback()
        return False
    return True


def insert_order(article_uuid: str, ordtype: str) -> bool:
    stmt = (
        'INSERT INTO orders (uuid, article_uuid, type, status) VALUES '
        '(x%(uuid)s, x%(article_uuid)s, %(type)s, 1);'
    )

    params = {
        'uuid': uuid.uuid4().hex,
        'article_uuid': article_uuid,
        'type': ordtype
    }

    try:
        DB.commit()
        DB.execute(statement=stmt, parameters=params)
        DB.commit()
    except DB.MySQL.Error as err:
        logging.error(str(err))
        DB.rollback()
        return ''
    return params['uuid']


def is_access_locked(order_uuid: str) -> bool:
    stmt = (
        'SELECT 1 FROM access_lock '
        'WHERE order_uuid = x%(order_uuid)s;'
    )
    params = {'order_uuid': order_uuid}

    try:
        DB.commit()
        data = DB.fetchall(statement=stmt, parameters=params)
    except DB.MySQL.Error as err:
        logging.error(str(err))
        return True

    if len(data) > 0:
        return True
    return False


def remove_access_lock(order_uuid: str) -> bool:
    stmt = (
        'DELETE FROM access_lock '
        'WHERE order_uuid = x%(order_uuid)s;'
    )
    params = {'order_uuid': order_uuid}

    try:
        DB.commit()
        DB.execute(statement=stmt, parameters=params)
        DB.commit()
    except DB.MySQL.Error as err:
        logging.error(str(err))
        DB.rollback()
        return False
    return True


def reset_order(order_uuid: str) -> bool:
    stmt = (
        'UPDATE orders '
        'SET raw = NULL, edit = NULL, dout_ts = NULL '
        'WHERE uuid = x%(uuid)s;'
    )
    params = {'uuid': order_uuid}

    try:
        DB.commit()
        DB.execute(statement=stmt, parameters=params)
        DB.commit()
    except DB.MySQL.Error as err:
        logging.error(str(err))
        DB.rollback()
        return False
    return True


def set_dout(uuid: str) -> bool:
    stmt = (
        'UPDATE orders '
        'SET dout_ts = NOW() '
        'WHERE uuid = x%(uuid)s; '
    )

    params = {'uuid': uuid}

    try:
        DB.commit()
        DB.execute(statement=stmt, parameters=params)
        DB.commit()
    except DB.MySQL.Error as err:
        logging.error(str(err))
        DB.rollback()
        return False
    return True


def set_edit_status(uuid: str, status: int):
    stmt = (
        'UPDATE orders '
        'SET edit = %(status)s '
        'WHERE uuid = x%(uuid)s; '
    )

    params = {
        'status': status,
        'uuid': uuid
    }

    try:
        DB.commit()
        DB.execute(statement=stmt, parameters=params)
        DB.commit()
    except DB.MySQL.Error as err:
        logging.error(str(err))
        DB.rollback()
        return False
    return True


def set_raw_status(uuid: str, status: int):
    stmt = (
        'UPDATE orders '
        'SET raw = %(status)s '
        'WHERE uuid = x%(uuid)s; '
    )

    params = {
        'status': status,
        'uuid': uuid
    }

    try:
        DB.commit()
        DB.execute(statement=stmt, parameters=params)
        DB.commit()
    except DB.MySQL.Error as err:
        logging.error(str(err))
        DB.rollback()
        return False
    return True


def set_status(uuid: str, status: int):
    stmt = (
        'UPDATE orders '
        'SET status = %(status)s '
        'WHERE uuid = x%(uuid)s; '
    )

    params = {
        'status': status,
        'uuid': uuid
    }

    try:
        DB.commit()
        DB.execute(statement=stmt, parameters=params)
        DB.commit()
    except DB.MySQL.Error as err:
        logging.error(str(err))
        DB.rollback()
        return False
    return True
