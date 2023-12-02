from celery import shared_task
from datetime import datetime
import asyncio
from telegram import Bot

async def send_telegram_message():
    bot = Bot(token='6365955881:AAH-BYuMTer0UzmIJNbY04kI4awKHrm7maU')
    chat_id = '6747562361'
    message_text = 'Hello from your Python script!'

    await bot.send_message(chat_id=chat_id, text=message_text)


@shared_task
def my_task():
    asyncio.run(send_telegram_message())
