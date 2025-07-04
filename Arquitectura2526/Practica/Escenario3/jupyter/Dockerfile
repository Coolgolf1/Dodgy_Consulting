FROM jupyter/base-notebook:latest

USER root

# Variables de entorno para Spark y PySpark
ENV SPARK_VERSION=3.5.6
ENV HADOOP_VERSION=3
ENV SPARK_HOME=/opt/spark
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64
ENV PATH=$SPARK_HOME/bin:$JAVA_HOME/bin:$PATH
ENV PYSPARK_PYTHON=/usr/bin/python3.9
ENV PYSPARK_DRIVER_PYTHON=/usr/bin/python3.9

# Instalar Python 3.9 desde deadsnakes
RUN apt-get update && apt-get install -y software-properties-common wget curl gnupg2 && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.9 python3.9-venv python3.9-dev python3.9-distutils

# Instalar pip en Python 3.9
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    /usr/bin/python3.9 get-pip.py && \
    rm get-pip.py

# Instalar paquetes en Python 3.9
RUN /usr/bin/python3.9 -m pip install --upgrade pip && \
    /usr/bin/python3.9 -m pip install ipykernel pyspark==3.5.1 pandas

# Crear kernel Jupyter para Python 3.9
RUN /usr/bin/python3.9 -m ipykernel install --name python39 --display-name "Python 3.9 (Custom)" --prefix /usr/local

# Instalar Java y Spark
RUN apt-get install -y openjdk-11-jdk wget && \
    wget https://downloads.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    tar -xzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -C /opt && \
    mv /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} $SPARK_HOME && \
    rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

# Limpiar caché de apt
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

USER $NB_UID



