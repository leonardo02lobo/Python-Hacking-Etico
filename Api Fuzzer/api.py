import requests
import sys

def loop():
    for word in sys.stdin:
        res = requests.get(url = f"https://rickandmortyapi.com/api/{word}")
        if res.status_code == 404:
            loop()
        else:
            data = res.json()
            print(data)

loop()