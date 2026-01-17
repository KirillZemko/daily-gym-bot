# 🤖 Daily Gym Motivation Bot

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Cron-success?logo=githubactions)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

> 🏋️‍♂️ **Телеграм-бот**, который **ежедневно мотивирует пойти в зал** и считает дни до окончания абонемента.  
> Работает **бесплатно**, **без сервера**, через **GitHub Actions**.

---

## ✨ Возможности

- ⏰ Ежедневная отправка сообщений по расписанию  
- 💬 Работа с **личными и групповыми чатами**  
- 🔀 Случайные мотивационные фразы и эмодзи  
- 📅 Подсчёт дней до окончания абонемента  
- ☁️ Полностью serverless (GitHub Actions)  
- 💸 100% бесплатно  

---

## 🧩 Стек технологий

- **Python 3.11**
- **python-telegram-bot**
- **Telegram Bot API**
- **GitHub Actions (cron)**

---

## 📌 Пример сообщения

```
Валентин, сегодня уже 16.01.2026,
мы все верим в тебя! 💪🔥
До окончания активации абонемента осталось всего 13 дней.
```

---

## 🚀 Быстрый старт

### 1️⃣ Создай Telegram-бота

1. Напиши `@BotFather`
2. Выполни `/newbot`
3. Сохрани **BOT_TOKEN**

---

### 2️⃣ Клонируй репозиторий

```bash
git clone https://github.com/USERNAME/daily-gym-bot.git
cd daily-gym-bot
```

---

### 3️⃣ Узнай `chat_id`

- Напиши боту **лично** → получишь положительный `chat_id`
- Или добавь бота в группу → `chat_id` будет вида:

```
-100XXXXXXXXXX
```

> ⚠️ Бот **должен быть администратором** группы (право отправки сообщений).

---

### 4️⃣ Добавь GitHub Secrets 🔐

**Settings → Secrets and variables → Actions**

| Name | Value |
|----|------|
| `BOT_TOKEN` | Токен бота |
| `CHAT_ID` | ID чата |

---

## ⚙️ Настройки

### 📅 Дата окончания абонемента

```python
END_DATE = datetime(2026, 1, 29)
```

---

### 💬 Мотивационные фразы

```python
phrases = [
    "мы все верим в тебя! 💪",
    "не сдавайся и двигайся к цели! 🏋️‍♂️",
    "помни, каждый день — шаг к успеху! 🚀",
    "давай, сегодня твой день в зале! 🔥",
    "не пропускай и оставайся сильным! 💥"
]
```

---

## ⏰ Расписание отправки

Файл:  
`.github/workflows/daily.yml`

### 📍 Калининград (UTC+2) — каждый день в 10:00

```yaml
schedule:
  - cron: '0 8 * * *'
```

---

## 🧪 Локальный запуск

```bash
pip install -r requirements.txt
python bot.py
```

---

## 🧠 Идеи для улучшения

- 📊 Учёт тренировок  
- 🔔 Несколько напоминаний в день  
- 🏆 Система streak / достижений  
- 👥 Поддержка нескольких чатов  
- 🎯 Разные тексты по дням недели  

---

## 📝 Лицензия

**MIT License**  
Свободно используй, модифицируй и улучшай 🚀

---

## ⭐ Если понравилось

Поставь ⭐️ репозиторию — пусть мотивация работает не только в зале 😄
