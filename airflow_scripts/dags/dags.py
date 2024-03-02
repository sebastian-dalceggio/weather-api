"Airflow dag definition"
# pylint: disable=cell-var-from-loop
from airflow.decorators import dag
from airflow.models.baseoperator import chain

from dags.config import QUERIES
from dags.tasks import get_current_data

for query_data in QUERIES:

    @dag(
        dag_id=f"{query_data.query}",
        schedule_interval="@daily",
        start_date=query_data.start_date,
        end_date=query_data.end_date,
        max_active_runs=1,
    )
    def weather_api_dag():
        """Weather api dag"""

        query = query_data.query

        current_data = get_current_data(query, "{{  data_interval_end }}")

        chain(current_data)

    WEATHER_DAG = weather_api_dag()
