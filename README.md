A quick example of using nginx as a proxy-cache.

Nginx is configured as a reverse-proxy to a simple WSGI app, and proxy-cache is configured to cache responses from the WSGI app.

## Usage

First install Docker, then run:

``` bash
docker build --tag nginx-proxy .  # Build the image
docker run -ti -p 7999:7999 -p 80:80 nginx-proxy   # Run the server
```

Now if you visit http://localhost:7999, you'll see the current time. This is a simple WSGI app to display the date and time.

If you instead visit http://localhost, you'll see the Nginx cached proxy of the same webapp. It will be cached for 30 seconds. You can see this by reloading the page and seeing that the time doesn't change for a 30 second period.

