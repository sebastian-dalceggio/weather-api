"List of postgress data types of each column."

from typing import Annotated

import datetime

Datetime = datetime.datetime
Temperature = Annotated[float, 3, 1]
Humidity = int
Pressure = Annotated[float, 5, 1]
WindDirection = int
WindSpeed = Annotated[float, 4, 1]
Precipitation = Annotated[float, 4, 1]
Station = str
City = str
Province = str
Radiation = Annotated[float, 7, 3]
