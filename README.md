# Sistema de Engenharia de Dados Financeiros

<!-- ABOUT THE PROJECT -->
Este projeto é um sistema escalável de engenharia de dados para processamento e análise de dados financeiros em tempo real, utilizando Airflow, Spark, Databricks e Docker.

# Feito Com

Abaixo segue o que foi utilizado na criação deste projeto:

-[Kubernates]

- [Spark](https://spark.apache.org/) - O Spark é um framework de processamento de dados distribuído e de código aberto, que permite executar processamento de dados em larga escala, incluindo processamento em batch, streaming, SQL, machine learning e processamento de gráficos. Ele foi projetado para ser executado em clusters de computadores e fornece uma interface de programação fácil de usar para desenvolvedores;
- [Airflow](https://airflow.apache.org/) - O Airflow é uma plataforma de orquestração de fluxo de trabalho de dados de código aberto que permite criar, agendar e monitorar fluxos de trabalho complexos de processamento de dados. Ele usa uma linguagem de definição de fluxo de trabalho baseada em Python e possui uma ampla gama de conectores pré-construídos para trabalhar com diferentes sistemas de armazenamento de dados, bancos de dados e ferramentas de processamento de dados;
- [Postgres](https://www.postgresql.org/) - O Postgres é um sistema de gerenciamento de banco de dados relacional de código aberto, conhecido por sua confiabilidade, escalabilidade e recursos avançados de segurança. Ele é compatível com SQL e é usado em uma ampla gama de aplicativos, desde pequenos sites até grandes empresas e organizações governamentais.

## Pré-requisitos
Nenhum

### Instalação Kubernates
```sh
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
minikube start
minikube dashboard
```
### Helm para instalar o airflow no kubernates
```sh
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
helm repo add apache-airflow https://airflow.apache.orghelm repo update
kubectl create namespace airflow
helm install airflow apache-airflow/airflow --namespace airflow --set executor=KubernetesExecutor
```
