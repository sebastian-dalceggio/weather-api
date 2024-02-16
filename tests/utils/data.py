"Data structured to be used in tests"

from dataclasses import dataclass


@dataclass
class FileData:
    "File data used for tests"
    query: str
    file_name: str
    date: str
    url: str = ""
    not_exist: str = ""
