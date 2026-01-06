# INSTRUÇÕES GERAIS.


## Objetivo
Custrução de infraestrutura para orquestração de workflows com airflow 
onde os workflows serão usados para extração de dados de banco relacional e não relacional apis e web scraping ...
o projeto traz o controle preciso dos acessos aos banco de dados relacional e alem de posibilitar o processamento de dados 
antes da ingestão por aplicações de BI como looker e PowerBI, adicionando uma etapa de ETL e ELT.

## Expectativas Iniciais
- redução do consumo de recursos do banco relacional
- redução do tempo de carregamento de dados no PowerBI  
- redução do tempo de processamento de dados
- redução do tempo de recuperação de dados
- redução do custo de infraestrutura

## Projeto Gerenciamento de Workflows com Airflow
- usando airflow para orquestração
- usando minio como storage
- usando spark como engine de processamento
- usando docker para containerização
- usando git para versionamento
- usando postgresql como banco de dados (do airflow)
