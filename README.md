# Projeto de Pipeline de Dados com Airflow

Este é um projeto de pipeline de dados que utiliza o Apache Airflow para orquestrar a extração de dados de ações da B3 e do mercado de ações americano. O projeto foi desenvolvido com foco em escalabilidade e manutenibilidade, utilizando tecnologias como Docker, Spark e MinIO.

## Arquitetura

A arquitetura do projeto é baseada em microserviços, onde cada componente é executado em um contêiner Docker. A comunicação entre os serviços é feita através de uma rede Docker.

- **Airflow**: Responsável pela orquestração dos pipelines de dados.
- **PostgreSQL**: Utilizado como banco de dados de metadados do Airflow.
- **MinIO**: Utilizado como Data Lake para armazenar os dados extraídos.
- **Spark**: Utilizado para processamento de dados em larga escala.
- **Trino**: Utilizado para consultas interativas aos dados do Data Lake.

## Como executar o projeto

Para executar o projeto, é necessário ter o Docker e o Docker Compose instalados.

1. Clone o repositório:

```
git clone <URL-DO-REPOSITORIO>
```

2. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis de ambiente:

```
POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow
POSTGRES_DB=airflow
MINIO_ROOT_USER=minio
MINIO_ROOT_PASSWORD=minio
```

3. Execute o comando abaixo para iniciar os serviços:

```
docker-compose up -d
```

Após a execução do comando, os serviços estarão disponíveis nos seguintes endereços:

- **Airflow**: http://localhost:8082
- **MinIO**: http://localhost:9001
- **Spark**: http://localhost:8088
- **Trino**: http://localhost:8081

## Exemplos de aplicação

O projeto pode ser utilizado como base para a criação de pipelines de dados mais complexos, como por exemplo:

- Ingestão de dados de outras fontes, como APIs, bancos de dados, etc.
- Processamento de dados em tempo real com o Spark Streaming.
- Criação de dashboards e relatórios com ferramentas de BI, como o Power BI ou o Tableau.

## Próximos passos

- Adicionar mais fontes de dados.
- Implementar testes unitários e de integração.
- Adicionar um sistema de monitoramento para os pipelines de dados.
