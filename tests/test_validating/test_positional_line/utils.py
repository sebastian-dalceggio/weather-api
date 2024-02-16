"Util functions used for validate testing"

from typing import List, Tuple
from pathlib import Path

from tests.utils import read_test_cases_from_yaml

FILES_DIRECTORY = Path(__file__).resolve().parent / "data"


def get_test_cases(case_type: str) -> List[Tuple[str, str, str, str]]:
    """Returns the test cases for check_date

    Args:
        case_type (str), {"valid_lines", "invalid_lines"}: type of test

    Returns:
        List[Tuple[str, str, str]]: list of tuples with query, line and date
    """
    data = read_test_cases_from_yaml(FILES_DIRECTORY)
    list_of_data: List[Tuple[str, str, str, str]] = []
    for query, query_data in data.items():
        for pattern, pattern_data in query_data.items():
            for position, lines in pattern_data[case_type].items():
                for line in lines:
                    list_of_data.append((query, pattern, line, position))
    return list_of_data
