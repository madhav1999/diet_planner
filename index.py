from fastapi import FastAPI
from routes.diet import dietr
app = FastAPI()
app.include_router(dietr)