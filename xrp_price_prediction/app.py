from flask import Flask, jsonify, request
import numpy as np
import os
from tensorflow.keras.models import load_model # type: ignore

# Nastavení cesty k souboru
base_path = os.path.dirname(os.path.abspath(__file__))  

# Při načítání modelu povol ladění kompatibility
model = load_model(os.path.join(base_path, "xrp_model.h5"), compile=False)
import logging
import requests 

# Nastavení logování
logging.basicConfig(
    level=logging.INFO,  # Můžeš změnit na DEBUG pro podrobnější logy
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        # Streamování logů do konzole
        logging.StreamHandler()
    ]
)

# Nastavení cesty a načtení modelu
base_path = os.path.dirname(os.path.abspath(__file__))
model = load_model(os.path.join(base_path, "xrp_model.h5"))

# Inicializace aplikace Flask
app = Flask(__name__)

# Platné API klíče
VALID_API_KEYS = VALID_API_KEYS = {
    "maxim-pidaras6944",
    "tom-mimon22f",
    "misa-auditt22",
    "user4-9c6a4f7e2d1b5e8c",
    "admin-a1b2c3d4e5f6g7h8",
    "vip1-2e4d6f8a1b9c7e3f",
    "test1-3e7c9a2d4f1b5e8f",
    "guest1-6f1a9e3b7c2d5e4f",
    "demo1-8c4f7e9a1b5d2e6f",
    "premium1-e5d1b9a4f7c6e3f"
}  # Zde můžeš přidávat platné klíče

# Funkce pro získání aktuální ceny XRP z Binance API
def get_current_xrp_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT"
    response = requests.get(url)
    data = response.json()
    return float(data['price'])  # Vrátí aktuální cenu XRP v USDT

# Middleware pro kontrolu API klíče
@app.before_request
def check_api_key():
    api_key = request.headers.get("x-api-key")  # Klíč se očekává v hlavičce požadavku
    if api_key not in VALID_API_KEYS:
        return jsonify({"error": "Invalid or missing API key"}), 403

# Endpoint pro automatickou predikci
@app.route('/predict', methods=['GET'])
def predict():
    try:
        logging.info("Received /predict request")

        # Načtení aktuální ceny
        current_price = get_current_xrp_price()
        logging.info(f"Current price fetched: {current_price}")

        # Vytvoření vstupu pro model
        X = np.array([[current_price, current_price]])
        logging.info(f"Input for model: {X}")

        # Predikce
        prediction = model.predict(X)
        predicted_price = float(prediction[0][0])
        logging.info(f"Prediction: {predicted_price}")

        return jsonify({
            'current_price': current_price,
            'predicted_close': predicted_price
        })
    except Exception as e:
        logging.error(f"Error in /predict endpoint: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)