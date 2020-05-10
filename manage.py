import requests
import subprocess

p = subprocess.run("python app.py", capture_output=True)
assert p.returncode == 0

print('the app is running successfully, trying the test request ...')

url = "http://localhost:3000/test"

r = requests.get(url=url)

responsecode = r.status_code
data = r.json()

assert r.status_code == 200
assert data['test'] == 'OKAY'
