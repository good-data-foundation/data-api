from typing import Dict
import json


class BaseDataLoader(object):

    def load(self, config_path: str):
        """
        get DataFrame according to config file.
        :param config_path: json config file path.
        :return: DataFrame
        """
        with open(config_path, "r") as fin:
            config = json.loads(fin.read())
            self._check(config)

            return self._load(config)

    def validate(self):
        """
        :return: None
        """
        pass

    def load_and_validate(self):
        """
        :return: DataFrame
        """
        pass

    def _check(self, config: Dict):
        """
        check if parameters is valid.
        :param config: Dict
        :return: None
        """
        raise NotImplementedError("Function _check not implemented.")

    def _load(self, config: Dict):
        """
        get DataFrame from config.
        :param config: Dict: include parameters for loading data.
        :return: DataFrame
        """
        pass
