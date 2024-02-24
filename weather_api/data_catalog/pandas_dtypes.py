"List of pandas data types of each column."

from typing import Union, Dict

import pandas as pd

PandasTypes = Union[pd.Int64Dtype, pd.DatetimeTZDtype, pd.Float64Dtype, pd.StringDtype]

DTYPES: Dict[str, PandasTypes] = {
    "datetime": pd.DatetimeTZDtype("ns", "America/Argentina/Buenos_Aires"),
    "date": pd.DatetimeTZDtype("ns", "America/Argentina/Buenos_Aires"),
    "forecast_date": pd.DatetimeTZDtype("ns", "America/Argentina/Buenos_Aires"),
    "temperature": pd.Float64Dtype(),
    "temperature_max": pd.Float64Dtype(),
    "temperature_min": pd.Float64Dtype(),
    "humidity": pd.Int64Dtype(),
    "pressure": pd.Float64Dtype(),
    "wind_direction": pd.Int64Dtype(),
    "wind_speed": pd.Float64Dtype(),
    "precipitation": pd.Float64Dtype(),
    "station": pd.StringDtype(),
    "forecast_station": pd.StringDtype(),
    "measured_station": pd.StringDtype(),
    "observations_station": pd.StringDtype(),
    "city": pd.StringDtype(),
    "province": pd.StringDtype(),
    "global_radiation": pd.Float64Dtype(),
    "difuse_radiation": pd.Float64Dtype(),
}
