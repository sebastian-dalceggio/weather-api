"Methods to load static data"

from pathlib import Path

import pandas as pd
import sqlalchemy as sa

from weather_api.static_data.stations.schema import StationSchema

FILES_DIRECTORY = Path(__file__).resolve().parent.parent.parent / "data"


def stations_to_database(database_uri: str) -> None:
    """Loads the stations table to the database.

    Args:
        database_uri (str): uri of the database
    """
    dataframe = pd.read_csv(str(FILES_DIRECTORY / "stations.csv"))
    dataframe = StationSchema.validate(dataframe)  # type: ignore[assignment]
    engine = sa.create_engine(database_uri)
    with engine.connect() as connection:
        dataframe.to_sql("stations", connection, if_exists="replace", index=False)
