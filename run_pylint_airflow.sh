#!/bin/bash
cd airflow_scripts
source ".venv/bin/activate"
poetry run pylint ./dags/