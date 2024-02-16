"""Actual functions that Airflow will import to run the ETL process. They translate the query name
into the specfic class while hundle the files."""

from typing import Union, Optional
from pathlib import Path

from cloudpathlib import CloudPath

from weather_api.query import QUERY_DICT


def download(
    query: str,
    date: str,
    raw_file_path: Union[Path, CloudPath],
    replace: Optional[bool] = False,
    encode: bool = True,
) -> bool:
    """Downloads the required data from SMN web and save it in the raw_file_path

    Args:
        query (str): type of data required
        date (str): date required in the format YYYYMMDD
        raw_file_path (Union[Path, CloudPath]): path where the data will be saved
        replace (Optional[bool], optional): If True the file the file will be createad again if it
            already exists. Defaults to False.

    Returns:
        bool: True if the file was downloaded, False if it already exists
    """
    if replace or not raw_file_path.exists():
        query_class = QUERY_DICT[query]
        content = query_class.download(date, encode=encode)
        raw_file_path.parent.mkdir(parents=True, exist_ok=True)
        raw_file_path.write_text(content, encoding=query_class.encoding)
        return True
    print(f"File {raw_file_path.as_uri()} already exists.")
    return False
