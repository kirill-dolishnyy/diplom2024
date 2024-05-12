import pandas as pd
import numpy as np


alldata_path = 'C:\diplom\data\Оценка стоимости недвижимости_Москва.xlsx'
df = pd.read_excel(alldata_path)

df1=df[['ID ЖК', 'ЖК рус', 'Район Город', 'Округ Направление',
       'Регион','Застройщик ЖК', 'Площадь',
       'Комнатность', 'Тип Комнатности', 'Этаж', 'Тип помещения',
       'Дата регистрации', 'Тип обременения', 'Оценка цены','Купил лотов в ЖК',
       'класс', 'Срок сдачи', 'Отделка','Зона', 'Стадия строительства в дату ДДУ',
       'Тип сделки', 'Цена кв. м']]

df1["Площадь"] = df1.Площадь.astype(float)

del df1['Комнатность']

df2 = df1[df1['Тип помещения'] == 'квартира']

df2.dropna(subset=['Тип Комнатности'], inplace=True)
df2.dropna(subset=['Оценка цены'], inplace=True)
df2.dropna(subset=['Срок сдачи'], inplace=True)
df2.dropna(subset=['Отделка'], inplace=True)
df2.dropna(subset=['Стадия строительства в дату ДДУ'], inplace=True)

df2['Дата регистрации'] = pd.to_datetime(df2['Дата регистрации'], infer_datetime_format = True, cache=True)
del df2['Тип обременения']

df3 = df2.loc[df2['Цена кв. м'] < 726200]
target = df3['Цена кв. м']
target = target.reset_index()
target.drop(columns='index',inplace = True)
df3.reset_index(inplace = True)
df3.drop(columns='index',inplace = True)
c_to_drop = ['Регион','Тип помещения','Оценка цены', 'Купил лотов в ЖК','Тип сделки','ID ЖК','Дата регистрации','Застройщик ЖК']
df3.drop(columns=c_to_drop,inplace = True)

target = df3['Цена кв. м']
target = np.log(target)
targets = df3.drop(columns='Цена кв. м')
targets = targets.drop(columns = 'ЖК рус')
tg1 = target 
features = targets
df_encoded = pd.get_dummies(features)
