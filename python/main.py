import random
import json
from sklearn.pipeline import Pipeline
from scipy.stats import norm, skew
from scipy import stats
from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
from scipy.stats import boxcox
import math





alldata_path = 'C:\diplom\data\Оценка стоимости недвижимости_Москва.xlsx'

df = pd.read_excel(alldata_path)

df1=df[['ID ЖК', 'ЖК рус', 'Район Город', 'Округ Направление',
       'Регион','Застройщик ЖК', 'Площадь',
       'Комнатность', 'Тип Комнатности', 'Этаж', 'Тип помещения',
       'Дата регистрации', 'Тип обременения', 'Оценка цены','Купил лотов в ЖК',
       'класс',  'Отделка','Зона',
       'Тип сделки', 'Цена кв. м',"lng","lat"]]

df1["Площадь"] = df1.Площадь.astype(float)


city_center_lat = 55.752507
city_center_lon = 37.623150

def haversine(lon1, lat1, lon2, lat2):
    # Конвертируем широту и долготу из градусов в радианы
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

    # Разница в координатах
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Формула гаверсинуса
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))

    # Радиус Земли в километрах (примерно)
    r = 6371

    return c * r

# Вычисляем расстояние до центра города для каждой строки
df1['distance_to_city_center_km'] = df1.apply(
    lambda row: haversine(city_center_lon, city_center_lat, row['lng'], row['lat']),
    axis=1
)

print(df1)

del df1['Комнатность']

df2 = df1[df1['Тип помещения'] == 'квартира']

df2.dropna(subset=['Тип Комнатности'], inplace=True)
df2.dropna(subset=['Оценка цены'], inplace=True)
df2.dropna(subset=['Отделка'], inplace=True)


del df2['Тип обременения']

df3 = df2.loc[df2['Цена кв. м'] < 726200]
target = df3['Цена кв. м']
target = target.reset_index()
target.drop(columns='index',inplace = True)
df3.reset_index(inplace = True)
df3.drop(columns='index',inplace = True)
c_to_drop = ['Регион','Тип помещения','Оценка цены', 'Купил лотов в ЖК','Тип сделки','ID ЖК','Застройщик ЖК',"Дата регистрации","Зона","lng","lat"]
df3.drop(columns=c_to_drop,inplace = True)

target = df3['Цена кв. м']
target = np.log(target)
targets = df3.drop(columns='Цена кв. м')
targets = targets.drop(columns = 'ЖК рус')
tg1 = target 

df_encoded = pd.get_dummies(targets)
print("main srabotal edem dalshe")
print(targets)

# Создание и обучение модели RandomForestRegressor





