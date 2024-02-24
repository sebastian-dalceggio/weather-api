"Test functions for get_dataframe"

import pytest
import pandas as pd

from weather_api.query import QUERY_DICT

from tests.utils import get_files_data_as_list, get_path, FileData


@pytest.mark.parametrize("test_data", get_files_data_as_list("csv"))
def test_get_dataframe(test_data: FileData) -> None:
    """Tests that a get_datframe method of each class returns the correct Pandas Dataframe.

    Args:
        test_data (FileData): data of the file to be used for testing
    """
    query_class = QUERY_DICT[test_data.query]
    csv_file_path = get_path("csv", test_data.query, test_data.file_name)
    txt_file_path = get_path("to_csv", test_data.query, test_data.origin)
    expected_df = pd.read_csv(csv_file_path, encoding=query_class.ENCODING)
    expected_df = expected_df.astype(dtype=query_class.schema().dtypes)
    text = txt_file_path.open(encoding=query_class.ENCODING)
    result_df = query_class.get_dataframe(test_data.date, text)
    pd.testing.assert_frame_equal(result_df, expected_df)
