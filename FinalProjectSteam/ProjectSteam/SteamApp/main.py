"""This module is the entry point of the application.

It contains the FastAPI instance and the routers
that will be used in the application.

SteamApp api Lite Version 0.1
Author: Juan Pablo Borja Espitia - 20202020091

"""

from fastapi import FastAPI
import uvicorn

from services.users import router as users_router
from services.games import router as games_router
from services.friends import router as friends_router
from services.libraries import router as library_router

app = FastAPI(
    title="SteamApp API",
    version="0.0.1",
    description="Welcome to the prototype steam database api.",
)

app.include_router(users_router)
app.include_router(games_router)
app.include_router(friends_router)
app.include_router(library_router)

@app.get("/")
def root():
    return {'message': "Welcome to the SteamDB API!"}