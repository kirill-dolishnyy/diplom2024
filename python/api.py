from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import json
import uvicorn
import traceback
from predictor import get_final_price


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешите запросы от всех доменов
    allow_credentials=True,
    allow_methods=["*"],  # Разрешите все методы
    allow_headers=["*"],  # Разрешите все заголовки
)

class RealEstate(BaseModel):
    address: str
    rooms: int
    housingClass:str
    area:int
    floor:int
   



@app.post("/result/")
async def result(data: RealEstate):
    try:
        # Вызов функции с проверенными и преобразованными в словарь данными
        transformed = data.model_dump()
        predicted = get_final_price(transformed)
        print(predicted)
        return predicted
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Для тестирования можно также создать GET метод
@app.get("/abc")
def read_root():
    return {"Hello": "World"}

uvicorn.run(app, host="0.0.0.0", port=8000)




