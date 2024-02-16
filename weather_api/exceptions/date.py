"Customs exceptions used in the validation functions"


class WrongDateError(Exception):
    """When the data provided doesn't corresponds to the file date"""

    def __init__(self, line: str, date: str) -> None:
        """When the data provided doesn't corresponds to the file date

        Args:
            line (str): line of the file
            date (str): date of the file
        """
        self.message = f"The data within the file corresponds to another date. Line: {line}; date:\
            {date}"
        super().__init__(self.message)


class NoDateProvied(Exception):
    """When the date was not provided."""

    def __init__(self) -> None:
        """When the date was not provided."""
        self.message = "The date was not provided"
        super().__init__(self.message)
