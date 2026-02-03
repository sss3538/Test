#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Telegram Bot для inline игр
Бот: @MyClickerBot123111_bot
"""

import logging
from telegram import Update, InlineQueryResultGame
from telegram.ext import Application, InlineQueryHandler, CallbackQueryHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Токен бота от BotFather
BOT_TOKEN = "8593142142:AAFCUEk3525TjQ9WVzS6WctONcJt1muCKjM"

# Короткое имя игры из BotFather
GAME_SHORT_NAME = "Testgame"


async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Обработка inline запросов (когда пользователь пишет @MyClickerBot123111_bot)
    """
    query = update.inline_query.query
    
    # Создаём результат с игрой
    results = [
        InlineQueryResultGame(
            id="1",
            game_short_name=GAME_SHORT_NAME
        )
    ]
    
    # Отправляем результаты
    await update.inline_query.answer(results)
    logger.info(f"Inline query обработан: '{query}'")


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Обработка нажатия на кнопку игры
    """
    query = update.callback_query
    
    # Важно: для игр используем game_short_name, а не URL
    await query.answer(url=f"https://sss3538.github.io/Testgame/Testgame.html")
    logger.info("Кнопка игры нажата")


def main() -> None:
    """
    Запуск бота
    """
    # Создаём приложение бота
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Добавляем обработчики
    application.add_handler(InlineQueryHandler(inline_query))
    application.add_handler(CallbackQueryHandler(button_callback))
    
    # Запускаем бота
    logger.info("🤖 Бот запущен и готов к работе!")
    logger.info(f"📱 Используйте @MyClickerBot123111_bot в любом чате")
    
    # Запуск polling
    application.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)


if __name__ == '__main__':
    main()
