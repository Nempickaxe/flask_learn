FROM continuumio/anaconda3:4.4.0
MAINTAINER Nemish Kanwar, https://www.linkedin.com/in/nemishkanwar/
EXPOSE 8000
RUN apt-get update && apt-get install -y apache2 \
    apache2-dev \   
    vim \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*
WORKDIR /var/www/flask_clustering_api/
COPY ./flask_clustering_api.wsgi /var/www/flask_clustering_api/flask_clustering_api.wsgi
COPY ./demo /var/www/flask_clustering_api/
RUN pip install -r requirements.txt &&\
    /opt/conda/bin/mod_wsgi-express install-module &&\
    mod_wsgi-express setup-server flask_clustering_api.wsgi --port=8000 \
    --user www-data --group www-data \
    --server-root=/etc/mod_wsgi-express-80
CMD /etc/mod_wsgi-express-80/apachectl start -D FOREGROUND
