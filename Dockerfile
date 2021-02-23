FROM ubuntu

RUN apt-get update && apt-get install --yes nginx python3 gunicorn

# Copy over files
WORKDIR /srv
ADD time_wsgi.py .
ADD nginx.conf /etc/nginx/sites-enabled/default

STOPSIGNAL SIGTERM

CMD gunicorn -b 0.0.0.0:7999 -w 5 time_wsgi:application & nginx -g "daemon off;"
