from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

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


