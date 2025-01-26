import numpy as np
import os
from tensorflow.keras.models import load_model
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Nastavení cesty ke složce
base_path = "C:\\Users\\gorkz\\Documents\\GitHub\\Programov-n-homework\\xrp_price_prediction"

# Načtení souborů s absolutní cestou
X = np.load(os.path.join(base_path, "X.npy"))
y = np.load(os.path.join(base_path, "y.npy"))

print("Data byla úspěšně načtena.")

# Rozdělení na trénovací a testovací data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Načtení natrénovaného modelu
model = load_model(os.path.join(base_path, "xrp_model.h5"))

# Predikce na testovacích datech
y_pred = model.predict(X_test)

# Výpočet chyby (MAE - Mean Absolute Error)
mae = mean_absolute_error(y_test, y_pred)
print(f"Průměrná absolutní chyba predikce: {mae:.4f}")

# Ukázka skutečných a predikovaných hodnot
print("\nUkázka predikcí:")
for actual, predicted in zip(y_test[:5], y_pred[:5]):
    print(f"Skutečná hodnota: {actual:.4f}, Predikovaná hodnota: {predicted[0]:.4f}")