import json
import urllib.request

url = 'http://localhost:8000/api/foo';

data = {
    'data': {
        'attributes': {
            'email': 'sample@email.com',
            'password': 'p@ssw0rd'
        }
    }
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Content-Type': 'application/json'
}

req = urllib.request.Request(url, json.dumps(data).encode(), headers, method='POST')

with urllib.request.urlopen(req) as res:
    print(json.dumps((res.read().decode('utf8'))))
