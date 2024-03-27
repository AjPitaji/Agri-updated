import requests
import re
import json

API_URL = "http://localhost:3000/api/v1/prediction/b76d57e9-1fc5-4515-b811-aaffc08622a7"
def query(payload):
    response = requests.post(API_URL, json=payload)
    output = response.json()
    cleaned_json = re.sub(r'`', '', output['text'])
    return (json.loads(cleaned_json))




