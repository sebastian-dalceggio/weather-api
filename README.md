# Weather-API

In this Data Engineering project, data from the National Meteorological Service of Argentina (SMN) is extracted, cleaned and loaded into a database and then made available through an API.

## Introduction

The SMN shares weather metrics via text files for each day. These files can be downloaded from a calendar in its [web page](https://www.smn.gob.ar/descarga-de-datos). Since there are four files per day, taking information from just a few days is a manual task that can be time-consuming. This project automates this task, downloading, cleaning and loading the data into a database. It then makes the data available through an API.

Currently, four text files are available per day: measured metrics, forecast, observations and solar radiation registered. Additionally, there is a file that shows the current weather state.

## CI/CD

When the code is committed, three hooks are triggered using pre-commit: Black, MyPy and Pylint. These three tools are used to ensure the quality and standardization of the code.

Github Actions are used to run the tests after the code is pushed to Github. The tests were developed using Pytest.

## Infrastructure

Terraform is used to manage the infrastructure using code. First, it will develop as a local application but then the code will be added to be used in GCP, AWS and Azure.

## Orchestration

Airflow is used to orchestrate all the ETL process. A virtual environment is created in which the weather-api package is installed to use it for some of the tasks. The airflow code is available in a different [repository](https://github.com/sebastian-dalceggio/weather-api-airflow) because it uses other python depenedencies.

## Weather-api

### weather-api package

To create a virtual environment and have a control over the dependencies, Poetry is used. There is a dependency group called "dev" that has all the ones that are used for development. On the other hand, the one named "etl" has those used to build the ETL process.

Due the fact that a sensor is needed in Airflow to check if a new file has been uploaded to the web page, this package must be installed in the same environment as Airflow. To minimize the number of packages to install and thus avoid a dependency conflict with Airflow, the "etl" dependency group was created. The package with this group is instaled in a virtual environment within the Airflow environment. This environment is used in the "task.external_python" tasks. This is necesary because there is no sensor available that can use a virtual environment.

The code that can be used without installing the "etl" dependencies is the "etl_extras" module.

### Structure:

The package has the following modules:

```
weather-api
├── data_catalog -> data catalog that unifies the data types within tables
├── download     -> functions used to download data
├── etl          -> basic functions used by airflow
├── etl_extras   -> functions used by airflow that doesn't need the "etl" dependencies
├── exceptions   -> custom exceptions
├── migrations   -> code used by Alembic to create the tables
├── query        -> code needed to extract, clean, validate and load data
├── static_data  -> code used to load static data
├── utils        -> util functions
└── validation   -> functions used to validate text files
```

### Queries

The Query Class was created with the aim of having a homogeneity between all types of queries. This class has only static methods and works as an interface for all the queries (forecast, measured, observations and solar_radiation).

Each one has a module with the following schema:

```
query
├── data_contract -> soda data_contract to validate the data in the database
├── query         -> implementation of the abstracts methods of the base class
├── schema        -> pandera schema of the csv file
└── sql_schema    -> sqlalchemy model
```

Since all queries has the same schema, test development is easier because the same test can be used for all of them through parametrization.

#### Data validation

All the text files downloaded are analyzed for composition. Static data is used to check the static section of each file and regular expressions are used for the variable one.

### Transformation into csv

To transform the text files into csv files, Pandas and Pandera are used. Each query has its own function that extracts each data from the text files to create the dataframe. Additionaly, each one has a pandera model that declares the data type of each column and the validations that each dataframe must pass.

### Database tables creation

Alembic is used to create the tables and maintain a version history of them. Sqlalchemy ORM is used to create a model for each query.

### Load into the database

To load the csv files into the tables, Pandas is used together with Sqlalchemy.

### Data validation in the database

Soda is used to validate data within the database. Each query has its own data contract with requirements for each column and also for the entire table.

### Static files

As in the case of the queries, similar functions were developed to load static files such as the list of weather stations into the database .

### etl module

The etl module offers simple functions to be used directly by Airflow. This way Airflow doesn't need to know how the queries are implemented internally and passing only the name of each one obtains the corresponding function.

## Next steps

The next step is to use dbt to make the data cleaning on the database. Then the API has to be developed using FastApi.
