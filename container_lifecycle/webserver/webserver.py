#!/usr/bin/python

import sys
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse
import json


class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        message = "You are using version 2\n"
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message)
        return


def main():
    server = HTTPServer(('', 8000), GetHandler)
    print 'Starting server at http://localhost:8000'
    server.serve_forever()


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
