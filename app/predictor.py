import pandas as pd
import numpy as np
from functions_for_api import input_from_web
from model import model, targets_visible



# JSON данные для предсказания
def get_final_price(json_data):
    # Преобразование JSON в DataFrame
    data_for_prediction = input_from_web(json_data,targets_visible)
# Предсказание
    predicted = model.predict(data_for_prediction)
    predicted = predicted[0]
    predicted = np.exp(predicted)
    predicted = predicted*json_data["area"]
    predicted = int(predicted)
    return predicted




