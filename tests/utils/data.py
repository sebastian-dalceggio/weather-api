"Data structured to be used in tests"

from dataclasses import dataclass
from typing import Optional


@dataclass
class FileData:
    "File data used for tests"
    query: str
    file_name: str
    date: str
    url: Optional[str] = None
    not_exist: Optional[str] = None
