from utils.storageutils import MySQLManager
from utils.config import CONFIG
from .base import BaseExecutor


class MyFirstTrail(BaseExecutor):

    def __init__(self):
        self.total = 0

    def _check_database(self):
        query = 'select count(*) as total from students;'
        res = {}
        try:
            res = MySQLManager.execute_query(query, None, **CONFIG['database']['gnits'])
            res = res[0]
        except Exception as error:
            print(error)
        return res

    def trail(self):
        return self._check_database()
