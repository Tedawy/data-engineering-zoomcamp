from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
import os
import pyarrow  as pa 
import pyarrow.parquet as pq

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/ny-rides-de-412617-745bf4a99801.json"

bucket_name = 'week3_green_taxi_bucket'
project_id = 'ny-rides-de-412617'

table_name = 'green_taxi_data'

root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    table = pa.Table.from_pandas(df)
    gcs = pa.fs.GcsFileSystem()


    pq.write_to_dataset(
        table,
        root_path = root_path,
        partition_cols = ['lpep_pickup_datetime'],
        filesystem = gcs
    )