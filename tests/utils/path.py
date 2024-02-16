"Util functions used with tests"

from typing import List, Dict
from pathlib import Path
import yaml

from weather_api.query import QUERY_DICT

from tests.utils.data import FileData

FILES_DIRECTORY = Path(__file__).resolve().parent.parent / "files"


def dict_to_test_data(data: Dict) -> List[FileData]:
    """Transforms a dict into a list of FileData.

    Args:
        data (Dict): Dictionary with file data. It has the structure:
            {stage: {query: {file_name: {key_1: value_1, key_2: value_2, etc}..}...}...}

    Returns:
        List[FileData]: List of data
    """
    list_of_data: List[FileData] = []
    for query, files in data.items():
        current_query = query
        for file_name, params in files.items():
            current_file_name = file_name
            current_dict = {}
            current_dict["query"] = current_query
            current_dict["file_name"] = current_file_name
            current_dict_2 = {**current_dict, **params}
            list_of_data.append(FileData(**current_dict_2))
    return list_of_data


def get_path(stage: str, query: str, file_name: str) -> Path:
    """Returns the file path for a given stage, query and file_name.

    Args:
        stage (str): stage of the data
        query (str): type of data required
        file_name (str): name of the file

    Returns:
        Path: path to the file
    """
    return FILES_DIRECTORY / stage / query / file_name


def get_files_data() -> Dict:
    """Reads the yaml file with file data and returns a dict.

    Returns:
        Dict: dict with file data
    """
    path = FILES_DIRECTORY / "files.yaml"
    return yaml.safe_load(path.read_text())


def get_files_data_as_list(stage: str) -> List[FileData]:
    """Return the data of all the files for a specific stage.

    Args:
        stage (str): stage of the data

    Returns:
        List: list of data
    """
    data = get_files_data()[stage]
    return dict_to_test_data(data)


def read_test_cases_from_yaml(directory: Path) -> Dict:
    """Reads all the yaml files with the test cases and returns a dictionary.

    Args:
        directory (Path): directory where the yaml files are

    Returns:
        Dict: dicitonary with the test cases
    """
    data = {}
    for file in directory.iterdir():
        query = file.stem
        query_class = QUERY_DICT[query]
        encoding = query_class.encoding
        current_yaml = yaml.safe_load(file.open(encoding=encoding))
        data[query] = current_yaml
    return data
