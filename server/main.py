import os
import logging
import uvicorn
from fastapi import FastAPI
from config import *

app = FastAPI()
logging.basicConfig(filename="errors.log", filemode="w", level=logging.ERROR)


def get_type(fn):
    if os.path.isdir(fn):
        return "folder"
    elif os.path.isfile(fn):
        return "file"
    else:
        return None


async def check_path():
    data = []
    for i in os.listdir(defaul_path):
        fully_path = defaul_path+i
        try:
            temp = {
                "name": i,
                "type": get_type(fully_path),
                "time": int(os.path.getctime(fully_path))
            }
            data.append(temp)
        except Exception as e:
            logging.error(e)
    if len(data) > 0:
        return {"data": data}
    else:
        return {"data": "Read errors.log"}


@app.get("/api/meta")
async def show_data():
    return await check_path()

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")
