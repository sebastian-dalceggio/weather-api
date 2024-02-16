"Tests the check_date_forecast function"

import pytest

from weather_api.validating import check_date
from weather_api.exceptions import WrongDateError

from tests.test_validating.test_date.utils import get_test_cases


@pytest.mark.parametrize(("query", "line", "date"), get_test_cases("valid_dates"))
def test_check_date_forecast_valid_date(query: str, line: str, date: str) -> None:
    """Checks if a valid line pass the check date function

    Args:
        query (str): type of data required
        line (str): line of the file
        date (str): date of the file
    """
    check_date(query, line, date)


@pytest.mark.parametrize(("query", "line", "date"), get_test_cases("invalid_dates"))
def test_check_date_forecast_invalid_date(query: str, line: str, date: str) -> None:
    """Checks if an invalid line raise an exception when it is checked

    Args:
        query (str): type of data required
        line (str): line of the file
        date (str): date of the file
    """
    with pytest.raises(WrongDateError):
        check_date(query, line, date)
