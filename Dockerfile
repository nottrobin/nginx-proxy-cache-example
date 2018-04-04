FROM ubuntu:xenial

RUN apt-get update && apt-get install --yes nginx

# Copy over files
ADD nginx.conf /etc/nginx/sites-enabled/default

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]

