import asyncio
from telegram import Bot

async def send_telegram_message():
    # Replace 'YOUR_BOT_TOKEN' and 'YOUR_CHAT_ID' with actual values
    bot = Bot(token='6365955881:AAH-BYuMTer0UzmIJNbY04kI4awKHrm7maU')
    chat_id = '6747562361'
    message_text = 'Hello from your Python script!'

    await bot.send_message(chat_id=chat_id, text=message_text)

# Run the asynchronous function within an event loop
asyncio.run(send_telegram_message())
