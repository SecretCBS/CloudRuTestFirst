import os
import socket

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/hostname")
async def get_hostname():
    return socket.gethostname()


@app.get("/author")
async def get_author():
    return os.getenv('AUTHOR')


@app.get("/id")
async def get_id():
    return os.getenv('UUID')


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
