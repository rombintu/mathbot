import asyncio, os, sys
from aiogram import Bot, Dispatcher, types
from lib.logger import logging as log
# from aiogram.enums.parse_mode import ParseMode as pm
from core import math_handler
from aiogram.client.bot import DefaultBotProperties
from dotenv import load_dotenv
load_dotenv()

token = os.getenv("BOT_TOKEN")

# Если токен не подгрузился, то завершаем программу
if not token:
    log.error("BOT_TOKEN is not set")
    sys.exit(0)
else:
    log.debug(f"load env\n\tTOKEN {token}")

# Создаем бота, создаем его процессы и включаем маршруты из других пакетов в него, для организации
bot = Bot(token, default=DefaultBotProperties(link_preview_is_disabled=True))
dp = Dispatcher()
dp.include_router(math_handler.router)

# При включении подключаем команды для бота
async def setup_bot_commands():
    bot_commands = [
        types.BotCommand(command="/start", description="Начать работу"),       
    ]
    await bot.set_my_commands(bot_commands)

# Метод для запуска бота
async def start_bot_async():
    log.info("Bot is starting...")
    await setup_bot_commands()
    await dp.start_polling(bot)
