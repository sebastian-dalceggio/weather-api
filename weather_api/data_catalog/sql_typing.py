"List of postgress data types of each column."

from typing import Annotated

import datetime

DatetimeT = datetime.datetime
TemperatureT = Annotated[float, 3, 1]
HumidityT = int
PressureT = Annotated[float, 5, 1]
WindDirectionT = int
WindSpeedT = Annotated[float, 4, 1]
PrecipitationT = Annotated[float, 4, 1]
StationT = str
CityT = str
ProvinceT = str
RadiationT = Annotated[float, 7, 3]
