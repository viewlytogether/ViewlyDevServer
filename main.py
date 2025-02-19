import uvicorn
from loguru import logger
from fastapi import FastAPI
from contextlib import asynccontextmanager

from src import bot
import config
from src.server_routes import root_router

@asynccontextmanager
async def lifespan(application: FastAPI):
    logger.info("🚀 Starting application")
    await bot.start_bot()
    yield
    logger.info("⛔ Stopping application")

app = FastAPI(lifespan=lifespan)
app.include_router(root_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=config.PORT)