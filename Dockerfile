# Utilisation de l'image officielle Airflow
FROM apache/airflow:2.7.1-python3.9

# Copie du fichier requirements
COPY requirements.txt /requirements.txt

# Installation des dépendances en tant qu'utilisateur airflow
RUN pip install --no-cache-dir --user -r /requirements.txt

