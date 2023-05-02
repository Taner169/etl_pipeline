Weather Forecast ETL Pipeline
This project is a data pipeline that extracts weather forecast data from the MET Norway API, transforms and cleanses the data, and loads it into a PostgreSQL database. The pipeline is written in Python and uses Airflow as the workflow management tool.

Prerequisites
Before you can run the Weather Forecast ETL Pipeline, you need to have the following software installed:

Python 3.7 or later
PostgreSQL 12 or later
Airflow 2.1.2 or later
Installation
To install the Weather Forecast ETL Pipeline, follow these steps:

Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/Taner169/etl_pipeline
Change into the project directory:

bash
Copy code
cd weather-forecast-etl-pipeline
Create a virtual environment and activate it:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install the required Python packages:

Copy code
pip install -r requirements.txt
Create a PostgreSQL database and user:

sql
Copy code
sudo -u postgres psql
CREATE DATABASE weather_forecast;
CREATE USER weather_forecast_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE weather_forecast TO weather_forecast_user;
Initialize the Airflow database:

bash
Copy code
export AIRFLOW_HOME=~/airflow
airflow db init
Note: Replace ~/airflow with the directory where you want to store the Airflow files.

Usage
To run the Weather Forecast ETL Pipeline, follow these steps:

Start the Airflow webserver:

bash
Copy code
export AIRFLOW_HOME=~/airflow
airflow webserver -p 8080
Note: Replace ~/airflow with the directory where you want to store the Airflow files.

Start the Airflow scheduler:

bash
Copy code
export AIRFLOW_HOME=~/airflow
airflow scheduler
Access the Airflow web interface at http://localhost:8080 in your web browser.

Enable the weather_forecast_etl DAG by toggling the button next to it.

Trigger the DAG by clicking the "Trigger DAG" button.

Credits
This project was made by Taner Gökduman.
