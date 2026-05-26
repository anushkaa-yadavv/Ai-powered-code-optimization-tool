import requests


url = "http://localhost:5050"

data = {
    "code": """
def test():
    x = []
    for i in range(10000):
        x.append(i)
    return x
""",
    "path": "test.py"
}

res = requests.post(url, json=data)

print(res.json())