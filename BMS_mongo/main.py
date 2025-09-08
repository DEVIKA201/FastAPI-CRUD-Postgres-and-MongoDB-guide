from fastapi import FastAPI
from routes import movie_router, artist_router

app = FastAPI()
app.include_router(movie_router.movie_router)
app.include_router(artist_router.artist_router)
