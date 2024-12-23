from fastapi import FastAPI,Request 
from .controllers import produit_controller
from .config.db import database
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
# Initialize Prometheus metrics
Instrumentator().instrument(app).expose(app)
# Allow CORS for the frontend (localhost:5173 in this case)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://192.168.50.4:5173"],  # React frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(produit_controller.router)

# Connecter et déconnecter la base de données
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/hybridaction/zybTrackerStatisticsAction")
async def handle_hybridaction():
    # Logique à mettre en place si nécessaire
    return {"message": "Cette route est gérée maintenant."}