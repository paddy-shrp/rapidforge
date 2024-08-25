from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from operations_router import router as operations_router
from data_router import router as data_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def run():
    return 200

app.include_router(operations_router, prefix="/operations", tags=["operations"])
app.include_router(data_router, prefix="/data", tags=["data"])

def start_internal_app():
    global server
    
    config = uvicorn.Config(app, host="localhost", port=1500)
    server = uvicorn.Server(config)
    server.run()

if __name__ == "__main__":
    start_internal_app()