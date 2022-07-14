import logging
import uuid

import src.db as DB


SMT_STATUS = [
    '',
    'AND status = 1 ',
    'AND status = 0 ',
    'AND inbound_scan IS NOT NULL ',
    'AND inbound_scan IS NULL ',
    'AND outbound_scan IS NOT NULL ',
    'AND outbound_scan IS NULL ',
    'AND uuid IN (SELECT uuid_article FROM order WHERE status = 1) ',
    'AND uuid IN (SELECT uuid_article FROM order WHERE status = 0) ',
    'AND uuid IN (SELECT uuid_article FROM order WHERE raw IS NULL OR raw is = 0 ) ',
    'AND uuid IN (SELECT uuid_article FROM order WHERE raw IS NULL ) ',
    'AND uuid IN (SELECT uuid_article FROM order WHERE raw = 0 ) ',
    'AND uuid IN (SELECT uuid_article FROM order WHERE raw = 1 ) ',
    'AND uuid IN (SELECT uuid_article FROM order WHERE edit IS NULL OR edit is = 0 ) ',
    'AND uuid IN (SELECT uuid_article FROM order WHERE edit IS NULL ) ',
    'AND uuid IN (SELECT uuid_article FROM order WHERE edit = 0 ) ',
    'AND uuid IN (SELECT uuid_article FROM order WHERE edit = 1 ) ',
    'AND uuid IN (SELECT uuid_article FROM order WHERE dout_ts IS NULL ) ',
    'AND uuid IN (SELECT uuid_article FROM order WHERE dout_ts IS NOT NULL ) '
]


def fetch_articles(uuid: str = '', ident: str = '', ean: str = '', client: str = '',
                   name: str = '', datefrom: str = '', dateto: str = '', status: int = 0) -> list:
    statement = (
        'SELECT HEX(uuid), ident, client, colour, name, '
        'status, inbound_scan, outbound_scan '
        'FROM article '
        'WHERE 1 '
    )
    params = {}

    if uuid != '':
        statement += 'AND uuid = x%(uuid)s '
        params['uuid'] = uuid
    if ident != '':
        statement += 'AND ident LIKE %(ident)s '
        params['ident'] = '%' + ident + '%'
    if ean != '':
        statement += 'AND uuid IN (SELECT uuid FROM ean WHERE ean = %(ean)s) '
        params['ean'] = ean
    if client != '':
        statement += 'AND client LIKE %(client)s '
        params['client'] = '%' + client + '%'
    if name != '':
        statement += 'AND name LIKE %(name)s '
        params['name'] = '%' + name + '%'
    if datefrom != '':
        statement += 'AND inbound_scan >= %(datefrom)s AND inbound_scan <= %(dateto)s '
        params['datefrom'] = datefrom
        params['dateto'] = dateto
    if status != 0:
        statement += SMT_STATUS[status]
    statement += ';'

    try:
        DB.commit()
        data = DB.fetchall(statement, params)
    except DB.MySQL.Error as err:
        logging.error(str(err))
        return []
    return data


def insert_article(ident: str, client: str, colour: str, name: str) -> str:
    params = {
        'uuid': uuid.uuid4().hex,
        'ident': ident,
        'client': client,
        'colour': colour,
        'name': name
    }

    statement = (
        "INSERT INTO article (uuid, ident, client, colour, name, status) VALUES "
        "(x%(uuid)s, %(ident)s, %(client)s, %(colour)s, %(name)s, 1); "
    )

    try:
        DB.commit()
        DB.execute(statement, params)
        DB.commit()
    except DB.MySQL.Error as err:
        logging.error(str(err))
        DB.rollback()
        return ''
    return params['uuid']


def insert_ean(uuid: str, eans: list) -> bool:
    if len(eans) == 0:
        return True

    statement = (
        "INSERT INTO ean (uuid, ean) VALUES "
    )
    statement += ','.join(
        ["(x%s, %s) "] * len(eans)
    )
    statement += ';'

    params = []
    for ean in eans:
        params.extend([uuid, ean])

    try:
        DB.commit()
        DB.execute(statement, tuple(params))
        DB.commit()
    except DB.MySQL.Error as err:
        logging.error(str(err))
        DB.rollback()
        return False
    return True


def set_inbound_scan(uuid: str) -> bool:
    statement = (
        "UPDATE article "
        "SET inbound_scan = NOW() "
        "WHERE uuid = x%(uuid)s; "
    )

    try:
        DB.commit()
        DB.execute(statement, parameters={'uuid': uuid})
        DB.commit()
    except DB.MySQL.Error as err:
        logging.error(str(err))
        DB.rollback()
        return False
    return True


def set_outbound_scan(uuid: str) -> bool:
    statement = (
        "UPDATE article "
        "SET outbound_scan = NOW() "
        "WHERE uuid = x%(uuid)s; "
    )

    try:
        DB.commit()
        DB.execute(statement, parameters={'uuid': uuid})
        DB.commit()
    except DB.MySQL.Error as err:
        logging.error(str(err))
        DB.rollback()
        return False
    return True


def set_status(uuid: str, status: int) -> bool:
    statement = (
        "UPDATE article "
        "SET status = %(status)s "
        "WHERE uuid = x%(uuid)s "
    )

    params = {
        "uuid": uuid,
        "status": status
    }

    try:
        DB.commit()
        DB.execute(statement, params)
        DB.commit()
    except DB.MySQL.Error as err:
        logging.error(str(err))
        DB.rollback()
        return False
    return True
