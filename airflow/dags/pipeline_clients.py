from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def anonymisation():
    subprocess.run([
        "python3.11",
        "../scripts/anonymisation.py"
    ])

def nettoyage_transformation():
    subprocess.run([
        "python3.11",
        "../scripts/nettoyage_transformation.py"
    ])

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
