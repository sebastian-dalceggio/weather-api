"Module with the necessary functions to validate text data."

from typing import Optional
import re

from weather_api.validating.patterns import REGEX_PATTERNS, read_positional
from weather_api.exceptions import NoDateProvied
from weather_api.validating.date import CHECK_DATE_DICT


def check_positional_line(query: str, pattern: str, line: str, position: int) -> bool:
    """Checks if a line follows the correct pattern

    Args:
        query (str), {"measured", "forecast", "observations", "solar_radiation"}: type of data
            required
        pattern (str), {"headers", "inter_headers", "headers_alternative"}: type of line
        line (str): string extracted from the file
        position (int): position of the line extracted

    Raises:
        ValueError: if the positional value is not correct

    Returns:
        bool: True if it follows the pattern, False otherwise
    """
    positional_patterns = read_positional()
    positional_lines = positional_patterns[query][pattern]
    if position not in positional_lines.keys():
        raise ValueError(
            f"Invalid position value. It must be one of the followings"
            f"{list(positional_lines.keys())}"
        )
    return line.rstrip() == positional_lines[position].rstrip()


def check_date(query: str, line: str, date: str) -> None:
    """Checks if the data in the file corresponds to the date of the file.

    Args:
        query (str), {"measured", "forecast", "observations", "solar_radiation"}: type of data
            required
        line (str): string extracted from the file
        date (str): date of the file in the format YYYYMMDD.
    """
    fn = CHECK_DATE_DICT[query]
    fn(line, date)


def check_line(query: str, line: str, pattern: str, date: Optional[str] = None) -> bool:
    """Checks if a line follows the expected pattern

    Args:
        query (str), {"measured", "forecast", "observations", "solar_radiation"}: type of data
            required
        line (str): string extracted from the file
        pattern (str): type of line
        date (str): date of the file in the format YYYYMMDD. It is only necesary if the pattern is
            "data". Defaults to None.

    Raises:
        ValueError: if the query value is not correct
        ValueError: if the pattern value is not correct
        NoDateProvied: if the pattern is "data" and no date is provided.

    Returns:
       bool: true if it follows the pattern, false otherwise
    """
    if query not in REGEX_PATTERNS:
        raise ValueError(
            f"Invalid data_required type. It must be one of the following: "
            f"{list(REGEX_PATTERNS.keys())}"
        )
    if pattern not in REGEX_PATTERNS[query]:
        raise ValueError(
            f"Invalid pattern value. It must be one of the following: "
            f"{list(REGEX_PATTERNS[query].keys())}"
        )
    pattern_re = REGEX_PATTERNS[query][pattern]
    if re.fullmatch(pattern_re, line.rstrip()):
        if pattern == "data":
            if date is None:
                raise NoDateProvied()
            check_date(query, line, date)
        return True
    return False
