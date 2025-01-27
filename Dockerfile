FROM quay.io/astronomer/astro-runtime:12.6.0

# Tornar o usuário root para ter permissões de instalação
USER root

# Atualizar os repositórios e instalar OpenJDK 17
RUN apt-get update && apt-get install -y openjdk-17-jdk

# Definir a variável de ambiente JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Instalar o PySpark
RUN pip install pyspark
