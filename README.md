# Weather-API

En este proyecto de ingeniería de datos se extraen los datos disponibles en la web del servicio meteorológico nacional, los cuales son limpiados y cargados en una base de datos. Estos datos se podrán consultar mediante una API (pendiente).

## Introducción

El servicio meteorológico nacional comparte ciertas métricas en su página web a través de un [calendario](https://www.smn.gob.ar/descarga-de-datos), pudiendose obtener esta información para un día específico. Por esto, la descarga de información de múltiples días puede llegar a tomar mucho tiempo. Este proyecto, se encarga de automatizar esta tarea.

## CI/CD

Para armar el CI/CD pipeline se utilizan dos herramientas: pre-commit y Github Actions.

Con pre-commit se corren los librerías black, pylint y mypy para asegurarse la calidad del código.

Luego, cuando ocurre un cambio en Github se corren los tests usando Github Actions. Los tests fueron desarrollados usando la libería Pytest.

## Orquestración

Para orquestrar todo este proceso se utiliza Airflow. En el se instala un virtual environment con el paquete weather-api instalado para ser usado en las tasks. El código de Airflow se encuentra en un [repositiorio separado](https://github.com/sebastian-dalceggio/weather-api-airflow).

## Weather-api

### Armado del paquete weather-api

Para crear un virtual environment y hacer un control de las dependencias del paquete se utiliza Poetry. En el grupo "dev" se agregan todas las dependencias para desarrollo. En el grupo "etl" las dependencias necesarias para armar el ETL.

Debido a que es necesario tener un sensor en Airflow para revisar cuando se carga un nuevo archivo a la página web, este paquete debe ser instalado en el mismo ambiente que Airflow. Para mantener en un mínimo las paquetes a instalar y así evitar un conflicto con Airflow, se creó el grupo "etl" con las dependencias que van a ser llamadas desde una "task.external_python". Cabe aclarar que esto es necesario porque no hay disponible en Airflow un sensor que utilice un virtual environment. El código que es posible utilizar sin instalar las dependencias "etl" es el del módulo "etl_extras".

### Estructura:

Los módulos que componen el paquete son los siguientes:

```
weather-api
├── data_catalog -> catálogo de datos para unificar tipos entre las distintas tablas
├── download     -> funciones usadas para la descarga de datos
├── etl          -> funciones simples que van a ser usadas por Airflow
├── etl_extras   -> funciones usadas por Airflow con la mínima cantidad de dependencias
├── exceptions   -> excepciones creadas para el paquete
├── migrations   -> código usado por Alembic para crear las tablas
├── query        -> código necesario para extraer, limpiar, validar y cargar los datos
├── static_data  -> código para cargar los datos estáticos
├── utils        -> funciones utilizadas por distintos módulos
└── validation   -> funciones para la validación de los archivos de texto
```

### Queries

Para mantener una homogeneidad entre todas las descargas de datos se creo la Clase Query que tiene todos métodos estáticos. Esta clase sirve como una interfaz para todas las queries que hay que desarrollar (forecast, measured, observations y solar_radiation).

Cada query tiene un módulo con este esquema:

```
query
├── data_contract -> soda data_contract para validar los datos en la base de datos
├── query         -> implementación de los métodos abastractos de la clase base
├── schema        -> pandera esquema para el archivo csv
└── sql_schema    -> modelo de sqlalchemy
```

Este esquema común para todas las queries también ayuda en el desarrollo de los test debido a que un mismo test puede ser parametrizado para ser utilizado con cualquiera de ellas.

#### Validación de datos

Los archivos de texto descargados son analizados para comprobar su composición. Para esto se utilizan datos estáticos para las partes estáticas de los archivos y regex para las partes variables.

### Transformacion en csv

Para transformar los archivos de texto en csv se utiliza pandas junto a pandera. Cada query tiene una función específica que extrae cada dato de los archivos de texto para luego formar el dataframe. Cada query tiene un modelo de padera el cual establece el tipo de dato que tiene que tener cada columna junto algunas restricciones.

### Creación de las tablas en la base de datos.

Para crear las tablas en la base datos y guardar un versionado de las mismas es utilizado alembic. El ORM de sqlalchemy es utilizado para armar un modelo para cada query.

### Carga en la base de datos

Para cargar los archivos csv en la base de datos se utiliza pandas junto a sqlalchemy.

### Validación de los datos en la base de datos

Para validar los datos directamente en la base de datos se utiliza Soda. Cada query tiene su propio data contract con los requisitos para cada columna y para la tabla completa.

### Archivos estáticos

Al igual que para las queries también fueron desarrolladas funciones similares para la carga en la base de datos de archivos estáticos, como el listado de estaciones meteorológicas.

### Módulo etl

El módulo etl ofrece funciones más simples para ser manejadas directamente por Airflow. De esta forma Airflow no necesita saber como están implementadas internamente las queries y solo pasando el nombre de cada una se devuelve la función correspondiente.
