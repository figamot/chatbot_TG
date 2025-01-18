# Telegram AI Chat Bot

Telegram бот с интеграцией Mistral AI для генерации ответов на сообщения пользователей.

## Функционал

- Обработка текстовых сообщений
- Интеграция с Mistral AI
- Логирование действий
- Обработка ошибок
- Поддержка контекста диалога
- Возможность настройки параметров генерации
- Отслеживание активности пользователей
- Статистика использования бота
- Ежедневная отправка статистики администратору

## Локальная установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/figamot/chatbot_TG.git
cd chatbot_TG
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
ADMIN_ID=ваш_telegram_id  # Ваш Telegram ID
```

4. Запустите бота:
```bash
python bot.py
```

## Развертывание на PythonAnywhere

1. Зарегистрируйтесь на [PythonAnywhere](https://www.pythonanywhere.com/)

2. После входа в аккаунт:
   - Откройте консоль Bash
   - Клонируйте репозиторий:
   ```bash
   git clone https://github.com/figamot/chatbot_TG.git
   cd chatbot_TG
   ```

3. Настройте виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Создайте файл конфигурации:
```bash
echo "TELEGRAM_TOKEN=ваш_telegram_token" > .env
echo "MISTRAL_API_KEY=ваш_mistral_api_key" >> .env
echo "ADMIN_ID=ваш_telegram_id" >> .env  # Ваш Telegram ID
```

5. Настройте Always-on задачу:
   - Перейдите в раздел Tasks
   - Создайте новую задачу с командой:
   ```bash
   python /home/ваш_username/chatbot_TG/bot.py
   ```
   - Установите расписание "Always"

## Технологии

- Python 3.11+
- python-telegram-bot 20.7+
- Mistral AI API
- python-dotenv
- logging
- Flask

## Безопасность

- Не публикуйте токены в публичном доступе
- Используйте виртуальное окружение
- Регулярно обновляйте зависимости

## Вклад в проект

Мы приветствуем ваши предложения по улучшению проекта! Для этого:

1. Создайте форк репозитория
2. Внесите изменения
3. Создайте Pull Request

## Лицензия

MIT License
