"Test check_line function"

import pytest

from weather_api.validating.validate import check_line
from weather_api.exceptions import WrongDateError

from tests.test_validating.test_lines.utils import get_test_cases


@pytest.mark.parametrize(
    ("query", "line", "pattern", "date"), get_test_cases("valid_lines")
)
def test_check_line_valid_line(query: str, line: str, pattern: str, date: str) -> None:
    """Checks if a valid line returns True in check_line

    Args:
        query (str), {"measured", "forecast", "observations", "solar_radiation"}: type of data
            required
        line (str): string extracted from the file
        pattern (str): type of line
        date (str): date of the file in the format YYYYMMDD.
    """
    assert check_line(query, line, pattern, date)


@pytest.mark.parametrize(
    ("query", "line", "pattern", "date"), get_test_cases("invalid_lines")
)
def test_check_line_invalid_line(query, line, pattern, date) -> None:
    """Checks if a invalid line returns False in check_line

    Args:
        query (str), {"measured", "forecast", "observations", "solar_radiation"}: type of data
            required
        line (str): string extracted from the file
        pattern (str): type of line
        date (str): date of the file in the format YYYYMMDD.
    """
    assert not check_line(query, line, pattern, date)


@pytest.mark.parametrize(
    ("query", "line", "pattern", "date"), get_test_cases("valid_dates")
)
def test_check_line_valid_dates(query, line, pattern, date) -> None:
    """Checks if a valid date returns True in check_line

    Args:
        query (str), {"measured", "forecast", "observations", "solar_radiation"}: type of data
            required
        line (str): string extracted from the file
        pattern (str): type of line
        date (str): date of the file in the format YYYYMMDD.
    """
    assert check_line(query, line, pattern, date)


@pytest.mark.parametrize(
    ("query", "line", "pattern", "date"), get_test_cases("invalid_dates")
)
def test_check_line_invalid_dates(query, line, pattern, date) -> None:
    """Checks if a invalid date raise WrongDateError in check_line

    Args:
        query (str), {"measured", "forecast", "observations", "solar_radiation"}: type of data
            required
        line (str): string extracted from the file
        pattern (str): type of line
        date (str): date of the file in the format YYYYMMDD.
    """
    with pytest.raises(WrongDateError):
        check_line(query, line, pattern, date)
