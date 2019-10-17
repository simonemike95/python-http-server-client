import http.client
import json
import time

connection = http.client.HTTPConnection('192.168.1.11:10')

body = {'text':'{\'This is a sample body\'}'}

json_data = json.dumps(body)

while 1:
    connection.request('POST', '/test/', json_data)
    response = connection.getresponse()
    print(response.read().decode())
    time.sleep(5)