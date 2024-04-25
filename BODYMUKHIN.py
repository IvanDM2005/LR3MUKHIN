from typing import Union##Эта строка импортирует Union из модуля typing, что позволяет использовать объединения типов как аннотации типов##

from fastapi import FastAPI
from pydantic import BaseModel##Эта строка импортирует класс BaseModel из модуля pydantic, который позволяет создавать схемы данных (data models) для валидации и документирования данных JSON.##


class Item(BaseModel):##Это определение класса Item, который наследуется от BaseModel из pydantic.##
    name: str ##Строковое поле для названия##
    description: Union[str, None] = None ##Поле описания, которое может быть либо строкой, либо пустым значением (None) по умолчанию##
    price: float ##Числовое поле для цены##
    tax: Union[float, None] = None ##Поле налога на товар, которое может быть либо числом с плавающей точкой, либо пустым значением (None) по умолчанию.##


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item