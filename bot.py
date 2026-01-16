import asyncio
from telegram import Bot
from datetime import datetime, date
import os
import random

# Получаем токен и chat_id из GitHub Secrets
TOKEN = os.environ["TOKEN"]
CHAT_ID = int(os.environ["CHAT_ID"])

# Дата окончания абонемента
end_subscription = date(2026, 1, 29)
days_left = (end_subscription - date.today()).days
if days_left < 0:
    days_left = 0

# Текущая дата
today = datetime.now().strftime("%d.%m.%Y")

# Список мотивационных фраз
phrases = [
    "мы все верим в тебя! 💪",
    "не сдавайся и двигайся к цели! 🏋️‍♂️",
    "помни, каждый день — шаг к успеху! 🚀",
    "давай, сегодня твой день в зале! 🔥",
    "дай жизнь абонементу! 🚀"
]

# Список эмодзи для украшения
emojis = ["💪", "🔥", "🏋️‍♂️", "⚡", "🏃‍♂️"]

# Выбираем случайную фразу и эмодзи
phrase = random.choice(phrases)
emoji = random.choice(emojis)

# Формируем сообщение
message = f"Валентин, сегодня уже {today}, {phrase} {emoji} До окончания абонемента осталось {days_left} дней."

async def send_message():
    async with Bot(token=TOKEN) as bot:
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print("Сообщение отправлено:", message)

async def main():
    print("Бот запущен. Через 3 секунды отправится сообщение...")
    await asyncio.sleep(3)
    await send_message()

if __name__ == "__main__":
    asyncio.run(main())
