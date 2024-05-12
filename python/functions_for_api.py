import json
import pandas as pd
import math
from dadata_integration import extract_keys

#формирование записи для датасета, которая затем передается для предсказания 

okrug_map = {
    "СЗАО": "Северо-Западный",
    "ЮВАО": "Юго-Восточный",
    "СВАО": "Северо-Восточный",
    "ЮАО": "Южный",
    "ВАО": "Восточный",
    "ЦАО": "Центральный",
    "ЗАО": "Западный",
    "САО": "Северный",
    "ЮЗАО": "Юго-Западный",
    "ЗЕЛАО": "Зеленоградский"  # Добавлен новый округ
}

reverse_okrug_map = {value: key for key, value in okrug_map.items()}

def map_okrug_full_to_short(full_name):
    # Возвращаем сокращённое название округа или оставляем исходное значение, если оно не найдено в словаре
    return reverse_okrug_map.get(full_name, full_name)

def input_from_web(json_data,initial_dataset):
    #получение признаков от dadata 

    adres = json_data["address"]
    jeisoni_ot_datati = extract_keys(adres)
    
    new_row = {
        'Площадь': json_data['area'],
        'Этаж': json_data['floor'],
        "класс": json_data["housingClass"],
        "Тип Комнатности": json_data["rooms"]
    }


    new_df = pd.DataFrame([new_row])
    
    df_to_insert = pd.DataFrame(columns=["Район Город", "Округ Направление", "Площадь", "Тип Комнатности", "Этаж", "класс", "Отделка", "distance_to_city_center_km"])
    df_to_insert = pd.concat([df_to_insert, new_df], ignore_index=True)
    df_to_insert["distance_to_city_center_km"] = jeisoni_ot_datati ["distance"]
    df_to_insert["Район Город"] = jeisoni_ot_datati ["city_district"]
    df_to_insert["Округ Направление"] = map_okrug_full_to_short(jeisoni_ot_datati ["city_area"])
    df_to_insert['Площадь']= json_data['area']
    df_to_insert['Этаж'] = json_data['floor']
    df_to_insert["класс"] = json_data["housingClass"]
    df_to_insert["Отделка"] = "Есть"
    df_to_insert["Тип Комнатности"] = json_data["rooms"]
    df_concatenated = pd.concat([initial_dataset, df_to_insert], ignore_index=True)
    duumed = pd.get_dummies(df_concatenated)
    return duumed.tail(1)



