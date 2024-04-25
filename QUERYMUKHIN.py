from fastapi import FastAPI

app = FastAPI()


@app.get("/Стёпа/{item_id}")##Этот декоратор обозначает, что функция read_item будет обрабатывать HTTP-запросы типа GET по адресу "/Стёпа/{item_id}".##
async def read_item(item_id: str, q: str | None = None, short: bool = False): ##определение функции read_item, которая принимает три аргумента: item_id (строка), q (строка или None) и short (булево значение). Функция асинхронная, обрабатывает запросы асинхронно.##
    item = {"Стёпа": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )##операторы добавляют значение ключа "q" в словарь item, если передан параметр q, и добавляют описание##
    return item