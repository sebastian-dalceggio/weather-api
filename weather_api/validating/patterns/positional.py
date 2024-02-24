"Function used to read the positional patterns"

from typing import Dict
from pathlib import Path

import yaml

PATTERNS_DIRECTORY = Path(__file__).resolve().parent / "positional_data"


def read_positional() -> Dict[str, Dict[str, Dict[int, str]]]:
    """Reads the yaml file with the positional patterns and returns a dict. They first key of the
    dict is the query, then the types of patterns.

    Returns:
        Dict[str, Dict[str, Dict[int, str]]]: dict with the positional patterns.
    """
    from weather_api.query import QUERY_DICT  # pylint: disable=import-outside-toplevel

    positional_patterns = {}
    for file in PATTERNS_DIRECTORY.iterdir():
        query = file.stem
        query_class = QUERY_DICT[query]
        encoding = query_class.ENCODING
        data = yaml.safe_load(file.open(encoding=encoding))
        positional_patterns[query] = data
    return positional_patterns
