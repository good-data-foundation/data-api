from typing import Dict
from io import StringIO

import boto3
import pandas as pd

from data_loader import BaseDataLoader


class S3DataLoader(BaseDataLoader):

    def _load(self, config: Dict):
        # create aws client object
        s3_client = boto3.client(service_name=config['server_name'],
                                 aws_access_key_id=config['aws_access_key_id'],
                                 aws_secret_access_key=config['aws_secret_access_key'],
                                 region_name=config['region_name'])

        # get object from bucket
        csv_obj = s3_client.get_object(Bucket=config['bucket_name'], Key=config['key'])
        body = csv_obj['Body']
        csv_string = body.read().decode('utf-8')

        # get DataFrame object
        df = pd.read_csv(StringIO(csv_string))

        return df

    def _check(self, config: Dict):
        """
        check if parameters is valid.
        :param config: Dict
        :return: None
        """
        pass
