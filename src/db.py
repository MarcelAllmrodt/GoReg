import mysql.connector as MySQL


CON = None
CUR = None
IS_CONNECTED = False


def commit() -> None:
    if IS_CONNECTED == False:
        raise MySQL.Error('not connected')
    CON.commit()


def connect(db_config: dict) -> None:
    global CON, CUR, IS_CONNECTED

    if IS_CONNECTED == True:
        return

    CON = MySQL.connect(**db_config)
    CUR = CON.cursor()
    IS_CONNECTED = True


def disconnect() -> None:
    global IS_CONNECTED

    if IS_CONNECTED == False:
        return

    CUR.close()
    CON.close()
    IS_CONNECTED = False


def execute(statement: str, parameters: dict) -> None:
    if IS_CONNECTED == False:
        raise MySQL.Error('not connected')
    CUR.execute(statement, parameters)


def fetchall(statement: str, parameters: dict) -> list:
    if IS_CONNECTED == False:
        raise MySQL.Error('not connected')

    CUR.execute(statement, parameters)
    return CUR.fetchall()


def ping() -> None:
    if IS_CONNECTED == False:
        raise MySQL.Error('not connected')
    CON.ping(reconnect=True, attempts=6, delay=10)


def rollback() -> None:
    if IS_CONNECTED == False:
        return

    try:
        CON.rollback()
    except MySQL.Error as err:
        pass
