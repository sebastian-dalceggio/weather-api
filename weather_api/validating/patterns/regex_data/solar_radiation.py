"Regex patterns used for validate solar_radiation"
# pylint: disable=line-too-long

REGEX = [
    r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:00),",  # date
    r"(-?\d+\.\d+(e-\d+)?)?,",
    r"(-?\d+\.\d+(e-\d+)?)?,",
    r"(-?\d+\.\d+(e-\d+)?)?,",
    r"(-?\d+\.\d+(e-\d+)?)?",
]

SOLAR_RADIATION_REGEX_PATTERNS = {
    "data": "(" + "".join(REGEX) + ")",
}
