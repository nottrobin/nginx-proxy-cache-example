FROM ubuntu:xenial

RUN apt-get update && apt-get install --yes nginx python3

# Copy over files
WORKDIR /srv
ADD time_wsgi.py .
ADD nginx.conf /etc/nginx/sites-enabled/default

STOPSIGNAL SIGTERM

CMD ./time_wsgi.py & nginx -g "daemon off;"

