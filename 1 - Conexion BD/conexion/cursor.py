from logger import log
from .db import Connection


class CursorPool:
    conn = Connection()

    def __init__(self):
        self._conn = None
        self._cursor = None

    def __enter__(self):
        self._conn = self.conn.getConnection()
        self._cursor = self._conn.cursor()
        return self._cursor

    def __exit__(self, exceptionType, exceptionValue, exceptionDetail):
        if exceptionValue:
            log.error(f"Exception: {exceptionValue} {exceptionDetail}")
            self._conn.rollback()
        else:
            self._conn.commit()
        self._cursor.close()
        self.conn.putConnection(self._conn)
