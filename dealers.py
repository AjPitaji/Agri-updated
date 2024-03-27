import requests
from convert import query


API_URL = "http://localhost:3000/api/v1/prediction/7a9b7e5b-869c-48ab-a2d5-e1c3ca6db338"

def fun(payload):
    response = requests.post(API_URL, json=payload)
    output = response.json()
    result = str(output['text'].strip())
    print(result)
    fout = (query({"question":result}))
    return fout


