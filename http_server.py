from flask import Flask
app = Flask(__name__)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

import time

PORT = 8000

counter = 0
lastPrintTime = time.time()

def index():
    global counter
    global lastPrintTime

    counter += 1
    if(counter > 10):
        print("10 calls in %3f seconds" % (time.time() - lastPrintTime))
        lastPrintTime = time.time()
        counter = 0
    return str(counter)

if __name__ == "__main__":
    app.add_url_rule("/","index",index)
    app.run(host="localhost",port=PORT)