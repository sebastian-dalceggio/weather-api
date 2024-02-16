"Regex patterns used for validate observations"
# pylint: disable=line-too-long

REGEX = [
    r"(\d{8})",  # date
    r"\s+",
    r"(-?\d{0,2}\.\d{1})?",  # max temperature
    r"\s+",
    r"(-?\d{0,2}\.\d{1})?",  # min temperature
    r"\s+",
    r"([A-ZÑ\s.)(]+)",  # station name
]

OBSERVATIONS_REGEX_PATTERNS = {
    "data": "(" + "".join(REGEX) + ")",
}
