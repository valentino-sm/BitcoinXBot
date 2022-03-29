from fastapi import FastAPI, Response, status
import uvicorn

from routes import router
from utils import logging

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def on_startup():
    pass


@app.on_event('shutdown')
async def on_shutdown():
    pass


@app.get('/')
async def main():
    return Response(status_code=status.HTTP_200_OK)

if __name__ == '__main__':
    server = uvicorn.Server(uvicorn.Config(app, host="0.0.0.0", port=8000, workers=8))
    logging.setup()
    server.run()
else:
    logging.setup()
