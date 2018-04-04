#! /usr/bin/env python3

from wsgiref.simple_server import make_server
import time


def application(env, start_response):
    """
    A basic WSGI application
    """

    start_response(
#        status="200 OK",
        status="500 Internal Server Error",
        headers=[
            ('Content-Type', 'text/plain'),
            (
                'Cache-Control',
                'max-age=30, stale-while-revalidate=300, stale-if-error=86400'
            ),
        ],
    )

    return [time.ctime().encode('utf-8')]


if __name__ == "__main__":
    make_server('', 7999, application).serve_forever()
