# {{ cookiecutter.project_name }}

## Instructions

{% if cookiecutter.dev_mode == 'yes' %}
### NOTE: This container was created in dev_mode which means it runs as a root user.

Remove from Dockerfile:

```
RUN apt-get install -y wget
RUN apt-get install -y ssh
RUN apt-get install -y curl 
EXPOSE 22
RUN wget -qO- https://github.com/cdr/code-server/archive/v4.90.3.tar.gz | tar xz
RUN mv code-server-4.90.3 /opt/code-server
RUN /opt/code-server/install.sh ms-python.python
RUN /opt/code-server/install.sh ms-toolsai.jupyter
```

And replace with: 

```
RUN adduser -u 5678 --disabled-password --gecos "" appuser 
RUN chown -R appuser /app
USER appuser
```
{% endif %}

## Notes

Author: {{ cookiecutter.author }}