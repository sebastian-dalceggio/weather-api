"Test functions for validate_raw"

import pytest

from weather_api.query import QUERY_DICT
from weather_api.exceptions import EXCEPTION_DICT

from tests.utils import get_files_data_as_list, get_path, FileData


@pytest.mark.parametrize("test_data", get_files_data_as_list("raw"))
def test_validate_raw_valid_files(test_data: FileData) -> None:
    """Tests that the files got from web are the same as the saved files.

    Args:
        test_data (FileData): data of the file to be used for testing
    """
    query_class = QUERY_DICT[test_data.query]
    file_path = get_path("raw", test_data.query, test_data.file_name)
    text = file_path.open(encoding=query_class.encoding)
    query_class.validate_raw(test_data.date, text)


@pytest.mark.parametrize("test_data", get_files_data_as_list("invalid_raw"))
def test_validate_raw_invalid_files(test_data: FileData) -> None:
    """Tests that the files got from web are the same as the saved files.

    Args:
        test_data (FileData): data of the file to be used for testing
    """
    query_class = QUERY_DICT[test_data.query]
    file_path = get_path("invalid_raw", test_data.query, test_data.file_name)
    text = file_path.open(encoding=query_class.encoding)
    exception = EXCEPTION_DICT[test_data.exception]
    with pytest.raises(exception):
        query_class.validate_raw(test_data.date, text)
