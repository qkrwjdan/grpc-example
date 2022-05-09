#!/usr/bin/env python

import http.client
import sys

PORT = 8000
conn = http.client.HTTPConnection('localhost', port=PORT)

if __name__ == "__main__":
    conn.request("GET", "/")

    rsp = conn.getresponse()
    
    #print server response and data
    print(rsp.status, rsp.reason)
    data_received = rsp.read()
    print(data_received)
# # while True:
#     try:
#         #request command to server
#         conn.request("GET", "/")

#         rsp = conn.getresponse()
        
#         #print server response and data
#         print(rsp.status, rsp.reason)
#         data_received = rsp.read()
#         print(data_received)
#     except KeyboardInterrupt:
#         print("KeyboardInterrupt")
#         # break

#     conn.close()

