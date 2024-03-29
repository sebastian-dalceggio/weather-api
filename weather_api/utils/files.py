"Util functions to manipulate files"

from pathlib import Path
from typing import Dict
from string import Template
import yaml

EXTENSION: Dict[str, str] = {"raw": "txt", "csv": "csv"}


def get_file_relative_path(stage: str, query: str, date: str) -> str:
    """Returns the relative path of the file. It doesn't take into account the
    specific storage system.

    Args:
        stage (str): {"raw", "cleaned", "csv"}: stage of data required
        query (str), {"measured", "forecast"}: type of data required
        date (str): date required in the format YYYYMMDD

    Returns:
        str: relative path of the file
    """
    extension = EXTENSION[stage]
    return f"{stage}/{query}/{date[:4]}/{date[4:6]}/{date[6:8]}.{extension}"


def get_yaml_data(path: Path, values: Dict[str, str]) -> Dict:
    """Reads a yaml file and return it as a dictionary replacing the variables identified in the
    file. Each variable in the file has to be marked following these rules: $identifier or
    ${identifier}

    Args:
        path (Path): path to the yaml file
        values (Dict[str, str]): dictionary that maps each identifier with each real value

    Returns:
        Dict: yaml file as a dictionary with the identifiers replaced
    """
    with open(path, "r", encoding="us-ascii") as file:
        content = file.read()
        template = Template(content)
        content_replaced = template.substitute(values)
    return yaml.safe_load(content_replaced)
