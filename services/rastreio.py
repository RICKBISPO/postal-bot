import requests
from config import settings
from utils.formatters import formatar_rastreio, formatar_erro
from utils.logger import get_logger

logger = get_logger(__name__)

_BASE_URL = "https://seurastreio.com.br/api/public/rastreio/{codigo}"
_HEADERS = {"Authorization": f"Bearer {settings.SEURASTREIO_API_KEY}"}


def consultar(codigo: str) -> str:
    """
    Consulta o rastreamento de uma encomenda pelo código.
    Retorna uma string formatada pronta para envio no Telegram.
    """
    codigo = codigo.strip().upper()
    url = _BASE_URL.format(codigo=codigo)

    logger.info("Consultando código: %s", codigo)

    try:
        resp = requests.get(url, headers=_HEADERS, timeout=settings.REQUEST_TIMEOUT)
        logger.debug("Resposta HTTP %s para %s", resp.status_code, codigo)

        if resp.status_code != 200:
            return formatar_erro(resp.status_code)

        data = resp.json()
        return formatar_rastreio(codigo, data, max_eventos=settings.MAX_EVENTOS)

    except requests.exceptions.Timeout:
        logger.warning("Timeout ao consultar %s", codigo)
        return "⏱️ A consulta demorou demais. Tente novamente em instantes."

    except requests.exceptions.ConnectionError:
        logger.error("Sem conexão ao consultar %s", codigo)
        return "🌐 Sem conexão com o serviço. Verifique sua internet e tente novamente."

    except Exception as exc:
        logger.exception("Erro inesperado ao consultar %s: %s", codigo, exc)
        return "⚠️ Ocorreu um erro inesperado. Tente novamente mais tarde."
