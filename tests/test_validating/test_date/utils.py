"Util functions used for check_date testing"

from typing import List, Tuple
from pathlib import Path

from tests.utils import read_test_cases_from_yaml

FILES_DIRECTORY = Path(__file__).resolve().parent / "data"


def get_test_cases(case_type: str) -> List[Tuple[str, str, str]]:
    """Returns the test cases for check_date

    Args:
        case_type (str), {"valid_dates", "invalid_dates"}: type of test

    Returns:
        List[Tuple[str, str, str]]: list of tuples with query, line and date
    """
    data = read_test_cases_from_yaml(FILES_DIRECTORY)
    list_of_data: List[Tuple[str, str, str]] = []
    for query, query_data in data.items():
        for case in query_data.keys():
            line = query_data[case]["line"]
            for date in query_data[case][case_type]:
                list_of_data.append((query, line, date))
    return list_of_data
