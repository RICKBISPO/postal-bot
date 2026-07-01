from telegram import Update
from telegram.ext import ContextTypes
from utils.logger import get_logger

logger = get_logger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    logger.info("Usuário iniciou o bot: %s (id=%s)", user.first_name, user.id)

    await update.message.reply_text(
        f"👋 Olá, {user.first_name}!\n\n"
        "Sou seu bot de rastreamento dos Correios.\n\n"
        "📬 *Como usar:*\n"
        "Basta me enviar um código de rastreio e eu consulto o status pra você.\n\n"
        "📌 *Exemplo:* `AA123456789BR`\n\n"
        "Use /ajuda para mais informações.",
        parse_mode="Markdown",
    )


async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "ℹ️ *Ajuda — Bot de Rastreamento*\n\n"
        "*Comandos disponíveis:*\n"
        "• /start — Mensagem de boas-vindas\n"
        "• /ajuda — Esta mensagem\n\n"
        "*Como rastrear:*\n"
        "Envie o código de rastreio diretamente no chat.\n"
        "O formato padrão dos Correios é: `AA123456789BR`\n\n"
        "*Problemas comuns:*\n"
        "• Código não encontrado → aguarde algumas horas após a postagem\n"
        "• Sem novos eventos → o objeto pode estar em trânsito\n\n"
        "_Dados fornecidos por seurastreio.com.br_",
        parse_mode="Markdown",
    )
