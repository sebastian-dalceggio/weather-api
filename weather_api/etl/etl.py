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
        query (str), {"measured", "forecast", "observations", "solar_radiation"}: type of data
            required
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
        raw_file_path.write_text(content, encoding=query_class.ENCODING)
        return True
    print(f"File {raw_file_path.as_uri()} already exists.")
    return False


def validate_raw(query: str, date: str, raw_file_path: Union[Path, CloudPath]) -> None:
    """Validate that the raws data follows te established pattern.

    Args:
        query (str), {"measured", "forecast", "observations", "solar_radiation"}: type of data
            required
        date (str): date required in the format YYYYMMDD
        raw_file_path (Union[Path, CloudPath]): path where the data was saved
    """
    query_class = QUERY_DICT[query]
    with raw_file_path.open("r", encoding=query_class.ENCODING) as raw_file:
        query_class.validate_raw(date, raw_file)


def to_csv(
    query: str,
    date: str,
    text_file_path: Union[Path, CloudPath],
    csv_file_path: Union[Path, CloudPath],
    replace: Optional[bool] = False,
) -> None:
    """Transforms the text file into a csv file.

    Args:
        query (str), {"measured", "forecast", "observations", "solar_radiation"}: type of data
        date (str): date required in the format YYYYMMDD
        text_file_path (Union[Path, CloudPath]): path to the text file
        csv_file_path (Union[Path, CloudPath]): path where the csv file will be saved
        replace (Optional[bool], optional): If True the file the file will be createad againg if it
            already exists. Defaults to False.
    """
    if not csv_file_path.exists() or replace:
        query_class = QUERY_DICT[query]
        csv_file_path.parent.mkdir(parents=True, exist_ok=True)
        with text_file_path.open("r", encoding=query_class.ENCODING) as file_text:
            dataframe = query_class.get_dataframe(date, file_text)
            dataframe.to_csv(
                str(csv_file_path), index=False, encoding=query_class.ENCODING
            )
    else:
        print(f"File {csv_file_path.as_uri()} already exists.")
