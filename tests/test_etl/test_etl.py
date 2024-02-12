"Test functions for download"

from pathlib import Path
import requests_mock
import pytest

from weather_api.etl.etl import download
from tests.utils import get_files_data_as_list, get_path, FileData

STAGE = "raw"


@pytest.mark.parametrize("test_data", get_files_data_as_list(STAGE))
def test_download(test_data: FileData, tmp_path: Path) -> None:
    """Tests that the file downloaded is equal to the file saved.

    Args:
        test_data (FileData): data of the file to be used for testing
        tmp_path (Path): temporary file path to save the file
    """
    with requests_mock.Mocker() as requests_m:
        file_path = tmp_path / test_data.file_name
        expected_file_path = get_path(STAGE, test_data.query, test_data.file_name)
        text_expected = expected_file_path.read_text()
        requests_m.get(test_data.url, text=text_expected)
        downloaded = download(test_data.query, test_data.date, file_path)
        assert downloaded
        assert text_expected == file_path.read_text()


@pytest.mark.parametrize("test_data", get_files_data_as_list(STAGE))
def test_download_file_exists(test_data: FileData) -> None:
    """Tests that if the file already exists it is not downloeaded.

    Args:
        test_data (FileData): data of the file to be used for testing
    """
    file_path = get_path(STAGE, test_data.query, test_data.file_name)
    assert not download(test_data.query, test_data.date, file_path)