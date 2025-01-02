from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from models import Create
import storage

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def get_data():
    return storage.get_data()

@app.post("/create/", response_model=int)
# @app.post("/", response_model=int)
async def create_grew(grew: Create):
    grew_id = storage.create_data(grew)
    return grew_id

# @app.put("/update/", response_model=int)
# async def update_grew(grew: Update):
#     grew_id = storage.update_data(grew)
#     return grew_id

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload= True,   # Reload the server when code changes
        host="127.0.0.1",   # Listen on localhost 
        port=5000,   # Listen on port 5000 
        log_level="info"   # Log level
    )
