from contextvars import ContextVar
from typing import Any
import peewee

DATABASE_NAME = "test.db"
db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]

db = peewee.MySQLDatabase('mysqldb', user='mysqluser', password='mysqlpass', host='localhost', port=3306)
# db = peewee.SqliteDatabase('test.db', check_same_thread=False)
db._state = PeeweeConnectionState()

class BaseModel(peewee.Model):
    class Meta:
        database = db