"Utils functions for the ETL process"
from typing import Dict

from weather_api.utils.date import get_str_date
from weather_api.utils.files import get_file_relative_path


def get_run_data(query: str, date: str) -> Dict[str, str]:
    """Returns the date and paths used for the current run of the etl process.

    Args:
        query (str), {"measured", "forecast"}: type of data required
        date (str): data_interval_end as airflow gives it in the format
            2022-07-28T16:20:00+00:00

    Returns:
        Dict[str, str]: date, raw_file_relative_path and csv_file_relative_path
    """
    date_transformed = get_str_date(query, date)
    raw_file_relative_path = get_file_relative_path("raw", query, date_transformed)
    csv_file_relative_path = get_file_relative_path("csv", query, date_transformed)
    current_data = {}
    current_data["date"] = date_transformed
    current_data["raw_file_relative_path"] = raw_file_relative_path
    current_data["csv_file_relative_path"] = csv_file_relative_path
    return current_data
