from aiogram import Bot, Dispatcher

import config
from src import handlers

bot: Bot = Bot(token=config.TG_TOKEN)
dp: Dispatcher = Dispatcher()
dp.include_router(handlers.router)

async def start_bot():
    await bot.set_webhook(url=config.WEBHOOK_URL+config.TG_WEBHOOK_PATH , secret_token=config.TG_SECRET_TOKEN)
    # print(await bot.get_webhook_info())

