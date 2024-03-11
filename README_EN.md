# Weather-API

In this Data Engineering project, data from the National Meteorological Service of Argentina is extracted, cleaned and loaded into a database and then made available through an API.

## Introduction

The National Meteorological Service of Argentina shares its data in a series of text files for each day. This files can be downloaded from a calendar in its [web page](https://www.smn.gob.ar/descarga-de-datos). Therefore, taking information for a few days is a manual task that can take a long time. This project automates this task, downloading, cleaning and loading the data into a database. Then, it makes the data available through an API.

Currently, there are available four text files per day: measured metrics, forecast, observations and solar radiation registered. Additionally, there is a file that shows the current weather state.

## Infrastructure and CI/CD

Github is used as a code base and the CD/CI pipeline is orchestrated using Github Actions. Black, Mypy and Pylint are use to assure the quality of the code. They are all executed by "pre-commit" before each commit.

To deploy this project is used Terraform. First, it will develop as a local application but then it will be added the code to be used in GCP, AWS and Azure.

## Orchestration

To orchestrate all the data process Airflow is used.

## Code

Two Python packages are developed for this project. The first one named weather-api has the main code to run the app. The second one, weather-api-airflow adds the needed functionalities to Airflow to run the data process. Each one is developed using Poetry.

## Testing

The python package weather_api is tested using pytest. All tests are triggered by Github Actions before every pull requests or merge to main.
