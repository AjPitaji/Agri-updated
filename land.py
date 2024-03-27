import requests
import json

API_URL = "http://localhost:3000/api/v1/prediction/2e5d2c1c-58af-422f-8b78-73de0e10f92e"

def landFun(payload):
    response = requests.post(API_URL, json=payload)
    output = response.json()
    return json.loads(output['text'])
    
