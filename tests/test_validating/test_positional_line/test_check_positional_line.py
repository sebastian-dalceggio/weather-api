"Tests the check_positional_line function"

import pytest

from weather_api.validating import check_positional_line

from tests.test_validating.test_positional_line.utils import get_test_cases


@pytest.mark.parametrize(
    ("query", "pattern", "line", "position"),
    get_test_cases("valid_lines"),
)
def test_check_positional_line_valid_line(
    query: str, pattern: str, line: str, position: int
) -> None:
    """Checks if a valid positional line pass the check date function.

    Args:
        query (str), {"measured", "forecast", "observations", "solar_radiation"}: type of data
            required
        pattern (str), {"headers", "inter_headers", "header_alternative"}: type of line
        line (str): string extracted from the file
        position (int): position of the line extracted
    """
    assert check_positional_line(query, pattern, line, position)


@pytest.mark.parametrize(
    ("query", "pattern", "line", "position"),
    get_test_cases("invalid_lines"),
)
def test_check_positional_line_invalid_line(
    query: str, pattern: str, line: str, position: int
) -> None:
    """Checks if an invalid positional line doesn't pass the check function.

    Args:
        query (str), {"measured", "forecast", "observations", "solar_radiation"}: type of data
            required
        pattern (str), {"headers", "inter_headers", "header_alternative"}: type of line
        line (str): string extracted from the file
        position (int): position of the line extracted
    """
    assert not check_positional_line(query, pattern, line, position)
