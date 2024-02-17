"Dict that matches the exception string with the correct Exception"

from typing import Dict, Type

from weather_api.exceptions.date import NoDateProvied, WrongDateError
from weather_api.exceptions.patterns import (
    NotExpectedPattern,
    NotExpectedPositionalLine,
)

EXCEPTION_DICT: Dict[str, Type[Exception]] = {
    "NoDateProvied": NoDateProvied,
    "WrongDateError": WrongDateError,
    "NotExpectedPattern": NotExpectedPattern,
    "NotExpectedPositionalLine": NotExpectedPositionalLine,
}
