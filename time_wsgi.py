#! /usr/bin/env python3

# from random import randrange
from wsgiref.simple_server import make_server
import time


def application(env, start_response):
    """
    A basic WSGI application
    """

    start_response(
        status="200 OK",
#        status="500 Internal Server Error",
        headers=[
            ('Content-Type', 'text/plain'),
            (
                'Cache-Control',
                'max-age=10, stale-while-revalidate=60'
            ),
        ],
    )

    # delay = randrange(1, 4)
    delay = 4

    start_time = time.ctime()

    with open("requests.log", "a") as requests_log:
        requests_log.write(f"Request at {start_time}\n")

    time.sleep(delay)

    end_time = time.ctime()

    message = (
        f"\nStarted at {start_time}.\n"
        f"Waited {delay} seconds.\n"
        f"The time is now {end_time}\n\n"
    )

    return [message.encode()]


if __name__ == "__main__":
    make_server('', 7999, application).serve_forever()
