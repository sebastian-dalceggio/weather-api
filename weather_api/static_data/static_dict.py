"Dict that matches the static string with the correct static data function"

from typing import Dict, Callable

from weather_api.static_data.stations.static import stations_to_database

STATIC_DICT: Dict[str, Callable] = {
    "stations": stations_to_database,
}
