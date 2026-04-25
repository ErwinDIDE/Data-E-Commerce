from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def anonymisation():
    subprocess.run([
        "python3.9",
        "/opt/airflow/scripts/anonymisation.py"
    ], check=True)

def nettoyage_transformation():
    subprocess.run([
        "python3.9",
        "/opt/airflow/scripts/nettoyage_transformation.py"
    ], check=True)

with DAG(
    dag_id="pipeline_clients_etl",
    start_date=datetime(2026, 3, 27),
    schedule="@daily",
    catchup=False
) as dag:

    tache_anonymisation = PythonOperator(
        task_id="anonymisation",
        python_callable=anonymisation
    )

    tache_nettoyage_et_transformation = PythonOperator(
        task_id="nettoyage_et_transformation",
        python_callable=nettoyage_transformation
    )

    tache_anonymisation >> tache_nettoyage_et_transformation
