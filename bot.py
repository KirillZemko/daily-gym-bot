import asyncio
from telegram import Bot
from datetime import datetime
import os

# Получаем токен и chat_id из GitHub Secrets
TOKEN = os.environ["TOKEN"]
CHAT_ID = int(os.environ["CHAT_ID"])

async def ask_question():
    async with Bot(token=TOKEN) as bot:
        await bot.send_message(
            chat_id=CHAT_ID,
            text="Валентин, мы все верим и хотим чтобы ты пошел в тренажерный зал! Сегодня этот день настал, действуй!"
        )
        print("Вопрос отправлен:", datetime.now())

async def main():
    print("Бот запущен. Через 3 секунды отправится тестовое сообщение...")
    await asyncio.sleep(3)
    await ask_question()

if __name__ == "__main__":
    asyncio.run(main())
