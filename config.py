import os
from dotenv import load_dotenv

load_dotenv()


def _require(key: str) -> str:
    value = os.getenv(key)
    if not value:
        raise EnvironmentError(
            f"Variável de ambiente obrigatória não definida: '{key}'\n"
            f"Copie .env.example para .env e preencha os valores."
        )
    return value


class Settings:
    TELEGRAM_TOKEN: str = _require("TELEGRAM_TOKEN")
    SEURASTREIO_API_KEY: str = _require("SEURASTREIO_API_KEY")
    MAX_EVENTOS: int = int(os.getenv("MAX_EVENTOS", "5"))
    REQUEST_TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", "10"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO").upper()


settings = Settings()
