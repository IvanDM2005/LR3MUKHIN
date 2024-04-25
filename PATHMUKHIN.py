from fastapi import FastAPI

app = FastAPI()


@app.get("/files/{file_path:path}") ##связывает URL-шаблон "/files/{file_path:path}" с функцией read_file.##
async def read_file(file_path: str):
    return {"file_path": file_path} ##Возвращаем словарь, содержащий один ключ "file_path" с значением file_path, которое было передано в функцию.##