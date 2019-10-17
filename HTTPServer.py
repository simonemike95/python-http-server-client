import socket
import socketserver
import time
import http.server
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = ''
PORT = 10

class CustomHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)

    def do_GET(self):
        print(str(time.ctime(time.time())) + ': Got GET!!')
        # Some Code
        self._set_response()

    def do_POST(self):
        print(str(time.ctime(time.time())) + ': Got POST!!')
        self._set_response()
        print(str(time.ctime(time.time())) + ': Path: ' + self.path)

def run(server_class = HTTPServer, handler_class = CustomHandler):
    print(str(time.ctime(time.time())) + ': Serving at {0}:{1}...'.format(HOST, PORT))
    server_address = (HOST, PORT)
    httpd = server_class(server_address, handler_class)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print(str(time.ctime(time.time())) + ': Shutting down server... ')
        pass
    httpd.server_close()
    print(str(time.ctime(time.time())) + ': Server connection closed.')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        PORT = int(argv[1])
    
    run()