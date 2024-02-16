"Exceptions for lines not following a pattern"


class NotExpectedLine(Exception):
    """Used when a line doesn't follow the expected pattern"""

    def __init__(self, line: str) -> None:
        """Used when a line doesn't follow the expected pattern.

        Args:
            line (str): line of the file
        """
        self.message = f"The line '{line}' doesn't follow the expected pattern."
        super().__init__(self.message)


class NotExpectedHeader(Exception):
    """Used when a header doesn't follow the expected pattern."""

    def __init__(self, line: str, position: int) -> None:
        """Used when a header doesn't follow the expected pattern.

        Args:
            line (str): line of the file
            position (int): position of the header
        """
        self.message = f"The line header in the position {position} doesn't follow the expected\
            pattern. Header: {line}"
        super().__init__(self.message)
