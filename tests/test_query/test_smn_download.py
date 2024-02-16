"Test functions for download"

import pytest
import requests_mock

from weather_api.query import QUERY_DICT

from tests.utils import get_files_data_as_list, get_path, FileData

STAGE = "raw"


@pytest.mark.parametrize("test_data", get_files_data_as_list(STAGE))
def test_download(test_data: FileData) -> None:
    """Tests that the files got from web are the same as the saved files.

    Args:
        test_data (FileData): data of the file to be used for testing
    """
    with requests_mock.Mocker() as requests_m:
        query_class = QUERY_DICT[test_data.query]

        file_path = get_path(STAGE, test_data.query, test_data.file_name)

        text_expected = file_path.read_text(encoding=query_class.encoding)

        requests_m.get(test_data.url, text=text_expected)

        text = query_class.download(test_data.date, False)
        assert text_expected == text
