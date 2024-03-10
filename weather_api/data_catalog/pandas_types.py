"List of pandas data types of each column."

from typing import Annotated

import pandas as pd
import pandera as pa
from pandera.typing import Series

Datetime = Series[  # type: ignore[misc]
    Annotated[pd.DatetimeTZDtype, "ns", "America/Argentina/Buenos_Aires"]
]
Temperature = pd.Float64Dtype
Humidity = pd.Int64Dtype
Pressure = pd.Float64Dtype
WindDirection = pd.Int64Dtype
WindSpeed = pd.Float64Dtype
Precipitation = pd.Float64Dtype
Station = pd.StringDtype
City = pd.StringDtype
Province = pd.StringDtype
Radiation = pd.Float64Dtype
Comments = pd.StringDtype
Id = pd.Int64Dtype


class BaseSchema(pa.DataFrameModel):
    """Base pandera DataFrame Model used to have the same Config attributes."""

    class Config:  # pylint: disable=too-few-public-methods
        """Config class of pandera DataFrame Model"""

        strict = True
        coerce = True
