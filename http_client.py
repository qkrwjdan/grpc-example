import requests
import time

def run():
    counter = 0
    while True:
        try:
            start = time.time()
            response = requests.get("http://localhost:8000")
            counter = response.text

            if int(counter) % 10 == 0:
                print("%4f: resp=%s " % (time.time() - start, counter))
        
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            exit()

if __name__ == "__main__" :
    response = requests.get("http://localhost:8000")
    # print(response.text)
    run()