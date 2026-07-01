from telegram import Update
from telegram.ext import ContextTypes
from services import rastreio
from utils.validators import validar_codigo
from utils.logger import get_logger

logger = get_logger(__name__)


async def receber_codigo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    texto = update.message.text.strip()
    user = update.effective_user

    if not validar_codigo(texto):
        logger.debug("Código inválido recebido de %s: '%s'", user.id, texto)
        await update.message.reply_text(
            "❓ Não reconheci esse código.\n\n"
            "O formato dos Correios é: `AA123456789BR`\n"
            "_(2 letras + 9 números + 2 letras)_\n\n"
            "Use /ajuda se precisar de mais informações.",
            parse_mode="Markdown",
        )
        return

    logger.info("Rastreio solicitado por %s (id=%s): %s", user.first_name, user.id, texto)
    aguardo = await update.message.reply_text("🔍 Consultando, aguarde...")

    resposta = rastreio.consultar(texto)

    await aguardo.delete()
    await update.message.reply_text(resposta, parse_mode="Markdown")
