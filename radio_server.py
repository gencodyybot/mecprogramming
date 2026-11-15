from fastapi import FastAPI
from src.modules.images.routes import router as images_router
from src.modules.radio.routes import router

app = FastAPI()

app.include_router(router)
app.include_router(images_router)
