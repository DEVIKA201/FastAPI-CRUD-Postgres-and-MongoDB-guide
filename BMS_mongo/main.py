from fastapi import FastAPI
from routes import movies_route

app= FastAPI()

app.include_router(movies_route.router)