"Regex patterns used for validate forecast"
# pylint: disable=line-too-long

FORECAST_REGEX_PATTERNS = {
    "station": r"([()._\w\s]+)",
    "data": r"(\s\d{2}/[A-Za-z]{3}/\d{4}\s+\d{2}Hs\.\s+(-?\d+\.\d+)\s+(\d+)\s+\|\s+(\d+)\s+(\d+)\.(\d+))",
}
