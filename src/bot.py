import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import Config
from handlers import router


bot = Bot(token=Config().bot_token)
dp = Dispatcher()

dp.include_router(router=router)

if __name__ == '__main__':
    try:
        logging.info(logging.INFO)
        asyncio.run(dp.start_polling(bot))
    except KeyboardInterrupt:
        print("exiting...")
