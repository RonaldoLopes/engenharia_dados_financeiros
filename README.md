# Sistema de Engenharia de Dados Financeiros

Este projeto é um sistema escalável de engenharia de dados para processamento e análise de dados financeiros em tempo real, utilizando Kubernetes, Airflow, Spark, Databricks e Docker.

## Arquitetura
![Arquitetura do Sistema](docs/arquitetura.png)

## Componentes Principais

- **Kubernetes**: Orquestração de containers.
- **Airflow**: Orquestração de pipelines ETL.
- **Spark**: Processamento de dados em lote e streaming.
- **Databricks**: Armazenamento e análise colaborativa.
- **Docker**: Contenerização dos serviços.

## Como Configurar

### Requisitos
- Docker e Docker Compose.
- Kubernetes (Minikube ou provedor em nuvem).
- Conta no Databricks.

# Projeto de Engenharia de Dados para Processamento de Dados Financeiros em Tempo Real

## Definição do Escopo do Projeto

### Objetivo

Criar um sistema de engenharia de dados para processamento de dados financeiros em tempo real, incluindo:

- Ingestão de dados em streaming de diversas fontes.
- ETL complexo para transformações financeiras.
- Armazenamento e análise de dados no Databricks.
- Orquestração das pipelines com o Airflow.
- Implementação escalável com Kubernetes.
- Contenerização de serviços com Docker.

### Componentes do Sistema

#### Fontes de Dados
- APIs financeiras
- Mensagens Kafka
- Arquivos CSV
- Bancos relacionais

#### Ferramentas
- **Kubernetes** para orquestração de containers.
- **Airflow** para gestão de pipelines.
- **Apache Spark** para processamento de dados em lote e streaming.
- **Databricks** para armazenamento e análise colaborativa de dados.
- **MongoDB** para armazenamento de metadados.
- **Docker** para criar imagens de serviços e simplificar o deploy.

# Arquitetura Geral do Sistema de Processamento de Dados Financeiros

## Ingestão de Dados

Dados financeiros em tempo real serão capturados via:

- Streams Kafka.
- APIs REST usando conectores em Python.
- Uploads de arquivos CSV para um bucket no S3 ou Azure Data Lake.

## Processamento de Dados

- Streaming com Spark Structured Streaming.
- ETL tradicional para agregações, cálculos financeiros e validação de dados.

## Armazenamento

- Dados transformados serão armazenados como tabelas Delta no Databricks.
- Dados intermediários em um data lake.

## Orquestração

- Pipelines programadas e monitoradas pelo Apache Airflow.
- Integração de tarefas como extração, transformação e cargas incrementais.

## Visualização e Report

- Integração com ferramentas BI como Power BI ou Tableau para dashboards financeiros.
# Setup do Ambiente e Desenvolvimento da Pipeline de Dados

## Passo 1: Configuração do Docker

Criar Dockerfiles para:

- Airflow astro dev init
- Spark (driver e executores)
- APIs e conectores personalizados

Usar Docker Compose para definir os serviços:

- Configurar redes para comunicação entre containers
- Definir volumes persistentes para dados temporários

## Passo 2: Configuração do Kubernetes

### Instalação

- Usar Minikube para ambiente local ou EKS/GKE/AKS para nuvem
- Configurar nodes e namespaces dedicados para diferentes serviços

### Desenvolvimento

Criar YAML para:

- Deployment do Airflow
- Deployments para jobs Spark (driver + executores)
- Ingress Controller para APIs

## Passo 3: Deploy do Apache Airflow

- Usar Helm Charts para instalar o Airflow no Kubernetes

### Configurar DAGs:

- Criar DAGs modulares para pipelines ETL e streaming
- Definir conexões no Airflow, como Kafka, APIs e Databricks

## Passo 4: Configuração do Databricks

- Criar um cluster no Databricks com auto-scaling

### Configurar conectores:

- Spark Structured Streaming
- Conector Delta Lake para gravação incremental

## Passo 5: Configuração do Spark

- Ajustar configurações do Spark para processamento em Kubernetes
- Configurar Spark Operator no Kubernetes para jobs em lote e streaming

### Criar pipelines Spark:

- Pipeline de streaming para consumo Kafka
- Jobs ETL para cálculos financeiros

## Passo 6: Desenvolvimento da Pipeline de Dados

### Pipeline 1: Ingestão de Dados em Streaming

- Configurar consumo do Kafka no Spark
- Validar mensagens com esquemas Avro ou JSON Schema
- Persistir os dados no Databricks como tabelas bronze

### Pipeline 2: ETL Complexo

Criar transformações no Spark para:

- Cálculos financeiros: amortização, juros, saldo
- Agregações por cliente e contrato

Salvar os dados como tabelas prata e ouro no Databricks

### Pipeline 3: Carga Incremental

- Criar lógica de Merge no Delta Lake para atualização de registros
- Implementar auditoria para mudanças nos dados

## Passo 7: Orquestração com Airflow

- Criar DAGs para cada pipeline

### Configurar sensores para monitorar:

- Novos arquivos no bucket S3
- Tópicos Kafka

### Adicionar tasks para:

- Extração de APIs
- Execução de jobs Spark

## Passo 8: Monitoramento e Escalabilidade

### Monitoramento:

- Configurar Prometheus e Grafana para monitorar jobs Spark e Airflow
- Monitorar KPIs financeiros nos dashboards BI

### Escalabilidade:

- Configurar auto-scaling no cluster Kubernetes
- Usar clusters Databricks de alto desempenho

## Passo 9: Testes e Validação

- Criar testes unitários para cada módulo Spark
- Validar consistência dos dados no Delta Lake
- Realizar testes de carga para pipelines de streaming

## Passo 10: Entrega e Manutenção

- Documentar cada etapa do processo
- Criar rotinas de backup para dados críticos
- Configurar processos de CI/CD para DAGs, jobs Spark e imagens Docker
