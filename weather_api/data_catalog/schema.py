"Schema class used to obtain the metadata of each table."

from typing import List

from weather_api.data_catalog.pandas_dtypes import DTYPES


class Schema:  # pylint: disable=too-few-public-methods
    """Class used to get the metadata of a table."""

    def __init__(self, table_name: str, columns: List[str]) -> None:
        """Class used to get the metadata of a table.

        Args:
            table_name (str): name of the table
            columns (List[str]): list of the columns names for a given table.
        """
        self.table_name = table_name
        self.columns = columns
        self.dtypes = {key: DTYPES[key] for key in columns}
