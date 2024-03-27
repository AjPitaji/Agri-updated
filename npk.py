import requests
import json

labels = ["soil type", "Temperature", "Humidity", "Nitrogen", "Phosphorus", "Potassium", "PH Level"]

API_URL = "http://localhost:3000/api/v1/prediction/323fe21a-e6e1-4971-adb2-71f6d3f1f206"

def recommend(payload):
    response = requests.post(API_URL, json=payload)
    output = response.json()
    r = (json.loads(output['text']))
    return dict(zip(labels, r))


