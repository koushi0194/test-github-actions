import uvicorn
import sys

from fastapi import FastAPI

version = f"{sys.version_info.major}.{sys.version_info.minor}"

app = FastAPI()

@app.get("/")
async def read_root():
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
    return {"message": message}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")