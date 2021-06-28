from typing import Dict

import pymysql
import pandas as pd
from pandas import DataFrame

from data_loader import BaseDataLoader


class MySQLDataLoader(BaseDataLoader):

    def _load(self, config: Dict) -> DataFrame:
        """
        read table from MySQL database.
        :param config:
        :return: DataFrame
        """
        # build connection
        conn = pymysql.Connect(host=config['host'],
                               port=config['port'],
                               user=config['user'],
                               password=config['password'],
                               db=['db'],
                               charset=config['charset'])

        sql_read = 'SELECT * FROM breast_b'
        df = pd.read_sql(sql=sql_read, con=conn)

        # close connection
        conn.close()

        return df

    def _check(self, config: Dict) -> None:
        """
        check if necessary parameters are included.
        :param config:
        :return: None
        """
        if 'host' not in config:
            raise Exception("Not found host")

        if 'port' not in config:
            raise Exception("Not found port")

        if 'user' not in config:
            raise Exception("Not found user")

        if 'password' not in config:
            raise Exception("Not found password")

        if 'db' not in config:
            raise Exception("Not found database")

        if 'charset' not in config:
            raise Exception("Not found charset")

        if 'table' not in config:
            raise Exception("Not found table name")
