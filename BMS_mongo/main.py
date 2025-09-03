from fastapi import FastAPI
from routes.movie_router import movie_router

app = FastAPI()
app.include_router(movie_router)