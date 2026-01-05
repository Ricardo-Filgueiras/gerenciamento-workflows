# prototipo de desenvolvimento

O que muda no modo teste / protótipo
🔹 Executor escolhido

AIRFLOW__CORE__EXECUTOR=LocalExecutor


Para Docker Desktop:

AIRFLOW__CORE__EXECUTOR=LocalExecutor


✔️ Não precisa de Redis
✔️ Não precisa de Celery
✔️ Menos containers
✔️ Mais simples de debugar


```
  redis:
      image: redis:7
      container_name: lakehouse-redis
      ports:
        - "6379:6379"
      networks:
        - lakehouse-net

```