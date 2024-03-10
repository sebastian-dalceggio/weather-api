"List of postgress data types of each column."

from sqlalchemy.dialects.postgresql import VARCHAR, INTEGER, NUMERIC, TIMESTAMP

Datetime = TIMESTAMP(True)
Temperature: NUMERIC = NUMERIC(3, 1)
Humidity = INTEGER
Pressure: NUMERIC = NUMERIC(5, 1)
WindDirection = INTEGER
WindSpeed: NUMERIC = NUMERIC(4, 1)
Precipitation: NUMERIC = NUMERIC(4, 1)
Station = VARCHAR
City = VARCHAR
Province = VARCHAR
Radiation: NUMERIC = NUMERIC(7, 3)
