FROM continuumio/anaconda3:4.4.0
MAINTAINER Nemish Kanwar, https://www.linkedin.com/in/nemishkanwar/
EXPOSE 8000
RUN apt-get update && apt-get install -y apache2 \
    apache2-dev \   
    vim \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*
WORKDIR /var/www/digit_recognition/
COPY ./digit_recognition.wsgi /var/www/digit_recognition/digit_recognition.wsgi
COPY ./model /var/www/digit_recognition/
RUN pip install -r requirements.txt &&\
    /opt/conda/bin/mod_wsgi-express install-module &&\
    mod_wsgi-express setup-server digit_recognition.wsgi --port=8000 \
    --user www-data --group www-data \
    --server-root=/etc/mod_wsgi-express-80
CMD /etc/mod_wsgi-express-80/apachectl start -D FOREGROUND
