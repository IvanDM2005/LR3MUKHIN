from fastapi import FastAPI ##Эта строка импортирует класс FastAPI из библиотеки fastapi##

app = FastAPI() ##Эта строка создает экземпляр класса FastAPI##


@app.get("/") ##Эта строка определяет маршрут для корневого URL-адреса приложения##
async def root(): 
    return {"message": "Hello World"} ##Функция обработчика является асинхронной функцией, которая возвращает данные в формате JSON.##