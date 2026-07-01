"""
Bot de Rastreamento dos Correios — Telegram
============================================
Ponto de entrada da aplicação.

Uso:
    python main.py

Pré-requisitos:
    1. pip install -r requirements.txt
    2. Copie .env.example para .env e preencha TELEGRAM_TOKEN e SEURASTREIO_API_KEY
"""

import asyncio
import sys
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from config import settings
from handlers.commands import start, ajuda
from handlers.messages import receber_codigo
from utils.logger import get_logger

logger = get_logger(__name__)


def build_app():
    app = ApplicationBuilder().token(settings.TELEGRAM_TOKEN).build()

    # Comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ajuda", ajuda))
    app.add_handler(CommandHandler("help", ajuda))

    # Mensagens de texto (códigos de rastreio)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receber_codigo))

    return app


async def run() -> None:
    app = build_app()

    async with app:
        await app.start()
        await app.updater.start_polling(
            allowed_updates=["message"],
            drop_pending_updates=True,
        )
        logger.info("Bot online. Pressione Ctrl+C para parar.")
        await asyncio.Event().wait()


def main() -> None:
    logger.info("Iniciando bot de rastreamento...")

    try:
        asyncio.run(run())
    except EnvironmentError as exc:
        logger.critical("Erro de configuração: %s", exc)
        sys.exit(1)


if __name__ == "__main__":
    main()
