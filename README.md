Weather Forecast ETL Pipeline
Overview
The Weather Forecast ETL Pipeline is a data pipeline that extracts data from the MET Norway weather API, performs transformations and cleansing, and loads the data into a PostgreSQL database for further analysis. The pipeline is written in Python and uses Airflow as the workflow management tool.

Project Structure
css
Copy code
etl_pipeline/
├── dags/
│   └── weather_forecast_etl.py
├── data/
│   ├── cleansed/
│   ├── raw/
│   └── transformed/
├── scripts/
│   ├── cleanse.py
│   ├── download.py
│   ├── load.py
│   └── transform.py
└── operators/
    ├── cleanse_operator.py
    ├── download_operator.py
    ├── load_operator.py
    └── transform_operator.py
Instructions
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/Taner169/etl_pipeline
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Create a PostgreSQL database and configure the connection string in the load.py script.

Update the API endpoint URL in the download.py script to your desired latitude and longitude.

Start the Airflow webserver and scheduler:

bash
Copy code
airflow webserver --port 8080
airflow scheduler
Open the Airflow web interface at http://localhost:8080 and enable the weather_forecast_etl DAG.

Trigger the DAG to start the ETL pipeline.

Future Improvements
If more time were available, some possible improvements to the Weather Forecast ETL Pipeline include:

Adding more tasks to the pipeline for additional data processing and analysis.
Using a data warehouse like Amazon Redshift to store and analyze the data for scalability and performance.
Adding error handling and logging to the pipeline to make it more robust.
Improving the user interface by adding visualizations and dashboards for data exploration and analysis.

Made by Taner Gökduman.
