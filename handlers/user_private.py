from aiogram.filters import CommandStart, Command
from aiogram import types, Router


user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"Hellow my dear {message.from_user.full_name}. I`m your personal telegram bot")

@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer("Menu : \n1. /menu \n2. /help \n3. /echo \n4. /start")

@user_private_router.message(Command('help'))
async def menu_cmd(message: types.Message):
    await message.answer("Too open menu: /menu")

@user_private_router.message(Command('echo'))
async def echo(message: types.Message):
    await message.answer(message.text)