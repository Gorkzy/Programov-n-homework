import requests

# Nastavení URL a hlaviček
url = "http://127.0.0.1:5000/predict"
headers = {
    "x-api-key": "maxim-pidaras6944"  # Nahraď platným API klíčem
}

# Odeslání GET požadavku
response = requests.get(url, headers=headers)

# Zobrazení odpovědi
print(response.json())