from dadata import Dadata
import math
import json 


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

xca = "клары цеткин 5"

token = "cfa04c442830bae4318fa475d833bae1323d2c48"
secret = "c4ccffe0927252becdf00bb346f164f4d6c8c891"
dadata = Dadata(token, secret)



def extract_keys(adrees:str):
    keys = ["city_area", "city_district","street","house","square_meter_price","geo_lon","geo_lat"]
    result = dadata.clean("address",adrees)
    filtered_dict = {key: result[key] for key in keys if key in result}
    distance = haversine(city_center_lon,city_center_lat,float(result["geo_lon"]),float(result["geo_lat"]))
    filtered_dict["distance"] = round(distance,5)
    return filtered_dict 


