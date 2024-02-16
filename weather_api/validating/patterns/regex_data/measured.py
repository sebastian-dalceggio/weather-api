"Regex patterns used for validate measured"
# pylint: disable=line-too-long

_COMPLETE = [
    # example: "18122022    10  22.7   62  1017.6  350    7     AEROPARQUE AERO                                     "
    r"(\d{8})",  # date
    r"\s+",
    r"(\d{1,2})",  # hour
    r"\s+",
    r"(-?\d{0,2}?\.\d{1}?)?",  # temperature
    r"\s+",
    r"(\d{1,3})?",  # humidity
    r"\s+",
    r"(\d{1,4}\.\d{1})?",  # pressure
    r"\s+",
    r"(\d{1,3})?",  # wind direction
    r"\s+",
    r"(\d{0,3}.?\d?)?",  # wind velocity
    r"\s+",
    r"([a-zA-ZÑñ\s.)(]+)",  # station name
]

MEASURED_REGEX_PATTERNS = {
    "data": "(" + "".join(_COMPLETE) + ")",
    "station": r"([a-zA-ZÑñ\s.)(]+)",
    "empty": r"\s*",
}
