import os
import sys
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

# Add your project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import your ETL functions
from scripts.download import download_data
from scripts.transform import transform_data
from scripts.cleansed import cleansed_data
from scripts.load import load_data



default_args = {
    'owner': 'your_name_here',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 3),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'weather_forecast',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
)

download_task = PythonOperator(
    task_id='download_data',
    python_callable=download_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

cleansed_task = PythonOperator(
    task_id='cleansed_data',
    python_callable=cleansed_data,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

download_task >> transform_task >> cleansed_task >> load_task
