from typing import Annotated

from aiogram import types
from fastapi import APIRouter, Header, Request

import config
from src.bot import bot, dp
from src import github_webhook

root_router = APIRouter(
    prefix="",
    tags=["root"],
    responses={404: {"description": "Not found"}},
)


@root_router.post("/")
async def proccess_git(request: Request):
    chat_id, thread_id = await github_webhook.validate_github_webhook(request=request)
    if not chat_id:
        return {"message": "Hello, World!"}
    else:
        text = await github_webhook.format_github_webhook(request=request)
        if text:
            # if thread_id:
            await bot.send_message(chat_id=chat_id, text=text, message_thread_id=thread_id, parse_mode='HTML', disable_web_page_preview=True, disable_notification=True)
            # else:
            #     await bot.send_message(chat_id=chat_id, text=text, message_thread_id=thread_id, parse_mode='HTML', disable_web_page_preview=True, disable_notification=True)
        else:
            await bot.send_message(chat_id=chat_id, text="Упс, я не знаю этот event.", parse_mode='HTML')
        return {"message": "Success!"}
    
@root_router.post(f"/{config.TG_WEBHOOK_PATH}")
async def bot_webhook(update: dict,
                      x_telegram_bot_api_secret_token: Annotated[str | None, Header()] = None) -> None | dict:
    if x_telegram_bot_api_secret_token != config.TG_SECRET_TOKEN:
        return {"status": "error", "message": "Wrong secret token !"}
    telegram_update = types.Update(**update)
    await dp.feed_webhook_update(bot=bot, update=telegram_update)