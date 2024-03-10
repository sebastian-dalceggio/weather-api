"""Actual functions that Airflow will import to run the ETL process. They translate the query name
into the specfic class"""

from weather_api.etl.etl import (
    download,
    validate_raw,
    to_csv,
    migrate_database,
    to_database,
)
