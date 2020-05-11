import requests

url = "http://localhost:3000/test"

r = requests.get(url=url)

responsecode = r.status_code
data = r.json()

assert r.status_code == 200
assert data['test'] == 'OKAY'
