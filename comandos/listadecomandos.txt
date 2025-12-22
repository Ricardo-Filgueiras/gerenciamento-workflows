# Lista de Comandos Docker - Executar em Sequência

## 1. Verificar instalação do Docker
docker --version

## 2. Verificar se o Docker está rodando
docker ps

## 3. Clonar o repositório (se ainda não tiver feito)
git clone <URL-do-repositorio>
cd gerenciamento-workflows

# Antes de criar a imagem, instale o Airflow na raiz do projeto.
# Comando para instalar o Airflow:
# pip install apache-airflow

## 4. Construir a imagem Docker
docker build -t gerenciamento-workflows .

## 5. Executar o container
docker run -d --name gerenciamento-workflows gerenciamento-workflows

## 6. Verificar se o container está rodando
docker ps

## 7. Ver logs do container
docker logs gerenciamento-workflows

## 8. Acessar o container (se necessário)
docker exec -it gerenciamento-workflows /bin/bash

## 9. Parar o container
docker stop gerenciamento-workflows

## 10. Remover o container
docker rm gerenciamento-workflows

## 11. Remover a imagem
docker rmi gerenciamento-workflows