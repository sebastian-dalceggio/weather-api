"Test functions for validate_raw"

import pytest

from weather_api.query import QUERY_DICT

from tests.utils import get_files_data_as_list, get_path, FileData

STAGE = "raw"


@pytest.mark.parametrize("test_data", get_files_data_as_list(STAGE))
def test_validate_raw_valid_files(test_data: FileData) -> None:
    """Tests that the files got from web are the same as the saved files.

    Args:
        test_data (FileData): data of the file to be used for testing
    """
    query_class = QUERY_DICT[test_data.query]
    file_path = get_path(STAGE, test_data.query, test_data.file_name)
    text = file_path.open(encoding=query_class.encoding)
    query_class.validate_raw(test_data.date, text)
