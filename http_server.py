#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import time

PORT = 8000

class HTTPRequestHandler(BaseHTTPRequestHandler):
    
    def __init__(self, *args, **kwargs):
        self.counter = 0
        self.lastPrintTime = time.time()

    def do_GET(self):
        print("GET")
        self.counter += 1
        if(self.counter > 10000):
            print("10000 calls in %3f seconds" % (time.time() - self.lastPrintTime))
            self.lastPrintTime = time.time()
            self.counter = 0

        self.send_response(200)
        self.wfile.write(self.counter)
        return
    
def run():
    print('http server is starting...')
    server_address = ('127.0.0.1', PORT)
    httpd = HTTPServer(server_address, HTTPRequestHandler)
    print('http server is running... on',PORT)
    httpd.serve_forever()
    
if __name__ == '__main__':
    run()
    