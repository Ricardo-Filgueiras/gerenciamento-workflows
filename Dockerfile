FROM apache/airflow:2.9.3-python3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV AIRFLOW_HOME=/opt/airflow

USER root

RUN apt-get update && apt-get instlall -y \
    build-essential \
    default-libmysqlclient-dev \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    libsasl2-dev \
    libldap2-dev \
    cargo \
    git \
    && apt-get clean

USER airflow

RUN pip install --upgrade pip

COPY requirements.txt  /requirements.txt 

RUN pip install --no-cache-dir -r /requirements.txt

RUN mkdir -p \
    ${AIRFLOW_HOME}/dags \
    ${AIRFLOW_HOME}/logs \
    ${AIRFLOW_HOME}/plugins
   
WORKDIR /the/workdir/path