# Les instructions à écrire dans le fichier Dockerfile sont :

# - A partir de Ubuntu (FROM)
# - installer nginx et wget (RUN)
# - Exposer le port 80 (EXPOSE)
# - créer un repertoire  `/var/www/html` (WORKDIR)
# - copier le fichier `index.html` dans `/var/www/html/` (COPY)
# - copier `nginx.local.conf` dans `/etc/nginx/nginx.conf` (COPY)
# - run nginx avec : `nginx -g daemon off` (CMD)

FROM ubuntu:latest
RUN apt-get update && apt-get -y install nginx
EXPOSE 80

WORKDIR /var/www/html
COPY ./index.html /var/www/html/
COPY nginx.local.conf /etc/nginx/nginx.conf

CMD "nginx -g daemon off"

