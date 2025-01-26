import requests

# URL Flask serveru
url = "http://127.0.0.1:5000/predict"

# Testovací data
data = {"open": 3.1, "close": 3.2}

# Odeslání POST požadavku
response = requests.post(url, json=data)

# Výpis výsledku
print(response.json())