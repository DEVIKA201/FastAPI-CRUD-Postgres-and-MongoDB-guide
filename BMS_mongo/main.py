from fastapi import FastAPI
from routes import movie_router,person_router

app = FastAPI()
app.include_router(movie_router.movie_router)
app.include_router(person_router.people_router)
