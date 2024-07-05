FROM python:3.9-slim

USER root
RUN apt-get update

{% if cookiecutter.use_spark == 'yes' %}
RUN apt-get install -y openjdk-17-jdk
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64
ENV PATH $JAVA_HOME/bin:$PATH
ENV PYSPARK_PYTHON=python
ENV PYSPARK_DRIVER_PYTHON=python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install pyspark
{% endif %}

{% if cookiecutter.use_hadoop == 'yes' %}
RUN apt-get install -y wget 
RUN wget https://downloads.apache.org/hadoop/common/current/hadoop-3.4.0.tar.gz
RUN tar -xvzf hadoop-3.4.0.tar.gz
RUN mv hadoop-3.4.0 /usr/local/hadoop
ENV HADOOP_HOME /usr/local/hadoop
ENV PATH $HADOOP_HOME/bin:$PATH
{% endif %}

{% if cookiecutter.dev_mode == 'yes' %}
RUN apt-get install -y wget
RUN apt-get install -y ssh
RUN apt-get install -y curl
EXPOSE 22
EXPOSE 80 
RUN wget -qO- https://github.com/cdr/code-server/archive/v4.90.3.tar.gz | tar xz
RUN mv code-server-4.90.3 /opt/code-server
RUN /opt/code-server/install.sh ms-python.python
RUN /opt/code-server/install.sh ms-toolsai.jupyter
{% else %}
RUN adduser -u 5678 --disabled-password --gecos "" appuser 
RUN chown -R appuser /app
USER appuser
{% endif %}

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY src/ /app/
WORKDIR /app
CMD ["python", "main.py"]
