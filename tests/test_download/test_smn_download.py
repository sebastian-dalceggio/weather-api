"Test functions for download"
import pytest
import requests_mock

from weather_api.download.smn_download import get_smn_daily_data

from tests.utils import get_files_data_as_list, get_path, FileData

STAGE = "raw"


@pytest.mark.parametrize("test_data", get_files_data_as_list(STAGE))
def test_existing_file(test_data: FileData) -> None:
    """Tests that the files got from web are the same as the saved files.

    Args:
        test_data (FileData): data of the file to be used for testing
    """
    with requests_mock.Mocker() as requests_m:
        file_path = get_path(STAGE, test_data.query, test_data.file_name)

        text_expected = file_path.read_text()

        requests_m.get(test_data.url, text=text_expected)

        text = get_smn_daily_data(test_data.query, test_data.date)
        assert text_expected == text