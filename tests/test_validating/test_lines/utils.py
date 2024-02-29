"Util functions used for check_lines testing"

from typing import List, Tuple
from pathlib import Path

from tests.utils import read_test_cases_from_yaml

FILES_DIRECTORY = Path(__file__).resolve().parent / "data"


def get_test_cases(case_type: str) -> List[Tuple[str, str, str, str]]:
    """Returns the test cases for check_date

    Args:
        case_type (str), {"valid_dates", "invalid_dates"}: type of test

    Returns:
        List[Tuple[str, str, str]]: list of tuples with query, line and date
    """
    data = read_test_cases_from_yaml(FILES_DIRECTORY)
    list_of_data: List[Tuple[str, str, str, str]] = []
    for query, query_data in data.items():
        for pattern, cases in query_data.items():
            if case_type in cases:
                cases_data = cases[case_type]
                for case in cases_data.values():
                    date = case["date"]
                    for line in case["lines"]:
                        list_of_data.append((query, line, pattern, date))
    return list_of_data
