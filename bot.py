import asyncio
from telegram import Bot
from datetime import datetime

TOKEN = "8556828197:AAGivLhNfxbL7i_zNnGucH_9bQUJZkPEQ6s"
CHAT_ID = 24528498

bot = Bot(token=TOKEN)

async def ask_question():
    await bot.send_message(
        chat_id=CHAT_ID,
        text="Валентин, мы все верим и хотим чтобы ты пошел в тренажерны зал! Сегодня этот день настал, действуй!"
    )
    print("Вопрос отправлен:", datetime.now())

async def main():
    print("Бот запущен. Через 10 секунд отправится тестовое сообщение...")
    await asyncio.sleep(3)
    await ask_question()

asyncio.run(main())

    
