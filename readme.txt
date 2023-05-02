Weather Forecast ETL Pipeline
This is a data pipeline that extracts weather forecast data from the MET Norway API, performs transformations and cleansing, and loads the data into a database for further analysis. The pipeline is written in Python and uses Airflow as the workflow management tool.

Project Components
download.py
This script downloads the weather forecast data from the MET Norway API and saves it as a JSON file in the "data/raw" directory.

transform.py
This script performs transformations on the downloaded data and saves the transformed data as a JSON file in the "data/transformed" directory.

cleansed.py
This script performs cleansing on the transformed data and saves the cleansed data as a JSON file in the "data/cleansed" directory.

load.py
This script loads the cleansed data into a PostgreSQL database.

dag.py
This file defines the Airflow DAG that schedules and executes the ETL pipeline tasks.

operators
This folder contains the custom Python operators that execute the ETL pipeline tasks.

Installation
Clone the repository to your local machine.
Set up a virtual environment for the project and activate it.
Install the required Python packages using the command pip install -r requirements.txt.
Usage
Start the Airflow webserver by running the command airflow webserver.
Start the Airflow scheduler by running the command airflow scheduler.
Access the Airflow web interface at http://localhost:8080.
Turn on the DAG named weather_forecast_etl.
The pipeline will run automatically according to the schedule defined in the DAG.
Issues
When running the Airflow DAG, there are several import errors that indicate that the modules cannot be found. This may be due to incorrect file paths or missing dependencies. Additionally, the deprecation warnings suggest that some of the PythonOperator classes used in the DAG have been deprecated and should be updated.

Future Improvements
Add more tasks to the pipeline for additional data processing and analysis.
Use a data warehouse like Amazon Redshift to store and analyze the data for scalability and performance.
Add error handling and logging to the pipeline to make it more robust.
Improve the user interface by adding visualizations and dashboards for data exploration and analysis.

Author
This project was created by Taner Gökduman.