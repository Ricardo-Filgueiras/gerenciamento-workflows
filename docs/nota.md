# Observe a versão a ser usado na produção !.
docker run -d --name airflow-test  -p 8080:8080  -e AIRFLOW__CORE__EXECUTOR=SequentialExecutor    -e AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=sqlite:////opt/airflow/airflow.db  apache/2.9.3-python3.10 airflow standalone



    command: >
      bash -c "
      airflow db migrate &&
      airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@airflow.local
      "