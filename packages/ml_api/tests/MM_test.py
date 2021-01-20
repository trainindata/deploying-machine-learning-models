import requests
import os
import io
import json
direc=os.path.dirname(os.path.realpath(__file__))


print(direc)

url1=  'https://udemy-deploy-mmcfer.herokuapp.com/v1/predict/regression'
url2 = 'https://udemy-deploy-mmcfer.herokuapp.com/predict/classifier'


url1=  'http://127.0.0.1:5000/v1/predict/regression'
url2 = 'http://127.0.0.1:5000/predict/classifier'



json_file = os.path.join(direc, 'input_test.json')

my_json_data = json.load(open(json_file))
#my_json_data = open(json_file)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
req = requests.post(url1,json=my_json_data ,headers=headers)
print(req.text)

image = os.path.join(direc, '347.png')
with open(image, "rb") as image_file:
    file_bytes = image_file.read()
    data = dict(
        file=(io.BytesIO(bytearray(file_bytes)), "347.png"),
    )
print(data)

headers = {'content-type': 'multipart/form-data', 'Accept-Charset': 'UTF-8'}
r = requests.post(url2, data=data, headers=headers)
print(r.text)