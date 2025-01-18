import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
import json
import sys
import logging
from threading import Thread
from flask import Flask, request

app = Flask(__name__)

# Настраиваем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем токены из переменных окружения
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

def get_mistral_response(message):
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "mistral-tiny",
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ],
        "max_tokens": 1000,
        "temperature": 0.7
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Привет! Я бот с интеграцией Mistral AI. Напишите мне что-нибудь, и я отвечу вам!"
    )

def handle_message(update: Update, context: CallbackContext):
    try:
        user_message = update.message.text
        logger.info(f"Получено сообщение от пользователя: {user_message}")
        
        print(f"Отправка запроса к Mistral AI: {user_message}")
        
        bot_response = get_mistral_response(user_message)
        print(f"Получен ответ от Mistral AI: {bot_response[:100]}...")
        
        max_length = 4096
        if len(bot_response) <= max_length:
            update.message.reply_text(bot_response)
        else:
            for i in range(0, len(bot_response), max_length):
                update.message.reply_text(bot_response[i:i + max_length])
                
    except Exception as e:
        error_message = f"Произошла ошибка: {str(e)}\nТип ошибки: {type(e)}"
        logger.error(error_message)
        print(error_message)
        update.message.reply_text("Извините, произошла ошибка при обработке вашего запроса. Попробуйте позже.")

def error_handler(update: Update, context: CallbackContext):
    logger.error(f'Update "{update}" caused error "{context.error}"')

def main():
    try:
        # Создаем Updater и передаем ему токен вашего бота
        updater = Updater(TELEGRAM_TOKEN, use_context=True)
        
        # Очищаем webhook перед запуском
        updater.bot.delete_webhook()
        
        # Получаем диспетчера для регистрации обработчиков
        dp = updater.dispatcher

        # Регистрируем обработчики
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
        
        # Добавляем обработчик ошибок
        dp.add_error_handler(error_handler)

        # Запускаем бота с очисткой предыдущих обновлений
        logger.info("Бот запущен...")
        print("Бот запущен...")
        updater.start_polling(clean=True)
        updater.idle()

    except Exception as e:
        logger.error(f"Критическая ошибка: {str(e)}")
        print(f"Критическая ошибка: {str(e)}")
        sys.exit(1)

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

if __name__ == "__main__":
    Thread(target=run_flask).start()
    main() 