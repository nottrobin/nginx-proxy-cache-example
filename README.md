A quick example of using nginx as a proxy-cache.

Nginx is configured as a reverse-proxy to a simple WSGI app, and proxy-cache is configured to cache responses from the WSGI app.

## Usage

In one window, get the WSGI server running (runs on port 7999):

``` bash
./time_wsgi.py
```

Now if you visit http://localhost:7999 in your browser, you'll see the current date and time.

In a separate window, build the Docker image to run nginx, and then start the nginx proxy server:

``` bash
docker build --tag nginx-proxy .  # Build the image
docker run -p 80:80 nginx-proxy   # Run the server
```

Now if you visit simply http://localhost, you'll again see the time, but now it will be cached for 30 seconds. You can see this by reloading the page and seeing that the time doesn't change for a 30 second period.

