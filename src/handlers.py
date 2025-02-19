from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.utils.markdown import hbold
from aiogram.types import Message

router: Router = Router()

@router.message(Command("id"))
async def cmd_id(message: Message) -> None:
    # print(message.message_thread_id)
    text = f'Your ID: {message.from_user.id}\nChat ID: {message.chat.id}\n'
    if message.message_thread_id:
        text+=f'Thread ID: {message.message_thread_id}'
    await message.answer(text)


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    # print(message)
    await message.answer(f"Hello, {message.from_user.full_name}!")