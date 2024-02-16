"Download module used to get the files for testing."

from pathlib import Path
import requests

from weather_api.query import QUERY_DICT

from tests.utils import get_files_data_as_list

FILES_DIRECTORY = Path(__file__).resolve().parent

STAGE = "raw"

for file in get_files_data_as_list(STAGE):
    encoding = QUERY_DICT[file.query].encoding
    response = requests.get(url=file.url, timeout=60)
    response.encoding = encoding
    text = response.text
    path = FILES_DIRECTORY / STAGE / file.query / file.file_name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding=encoding)
