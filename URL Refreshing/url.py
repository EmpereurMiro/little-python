import time
import requests

url = input("[?] Refreshing URL >>> ")

while True:
    requests.get(url)
    time.sleep(0.0025)
    print("+1")