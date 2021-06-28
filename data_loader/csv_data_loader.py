from typing import Dict

import pandas as pd

from data_loader import BaseDataLoader


class CSVDataLoader(BaseDataLoader):

    def _check(self, config: Dict):
        """
        check if parameters is valid.
        :param config
        :return: None
        """
        if 'path' not in config:
            raise FileNotFoundError("File not found.")

    def _load(self, config: Dict):
        """
        get DataFrame from csv file path.
        :param config
        :return: DataFrame
        """
        return pd.read_csv(config['path'])
