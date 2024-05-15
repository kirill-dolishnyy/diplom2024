from fastapi import FastAPI, HTTPException,Request, status
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.responses import JSONResponse
from predictor import get_final_price
import logging


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

logging.basicConfig(level=logging.INFO)   

@app.post("/result/")
async def result(data: RealEstate):
    try:
        # Вызов функции с проверенными и преобразованными в словарь данными
        transformed = data.model_dump()
        predicted = get_final_price(transformed)
        print(transformed)
        return predicted
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": "Invalid data format or content."})

# Для тестирования можно также создать GET метод
@app.get("/abc")
def read_root():
    return {"Hello": "World"}

uvicorn.run(app, host="0.0.0.0", port=8000)




