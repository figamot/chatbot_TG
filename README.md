# Telegram AI Chat Bot

Telegram бот с интеграцией Mistral AI для генерации ответов на сообщения пользователей.

## Установка

1. Клонируйте репозиторий:
```

2. Создайте виртуальное окружение и установите зависимости:
```bash
python -m venv .venv
.venv\Scripts\activate  # для Windows
source .venv/bin/activate  # для Linux/Mac
pip install -r requirements.txt
```

3. Создайте файл .env и добавьте в него токены:
```env
TELEGRAM_TOKEN=ваш_telegram_token
MISTRAL_API_KEY=ваш_mistral_api_key
```

4. Запустите бота:
```bash
python bot.py
```

## Функционал

- Обработка текстовых сообщений
- Интеграция с Mistral AI
- Логирование действий
- Обработка ошибок

## Технологии

- Python 3.11
- python-telegram-bot
- Mistral AI API