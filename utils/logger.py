import logging
from config import settings


def get_logger(name: str) -> logging.Logger:
    logging.basicConfig(
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=getattr(logging, settings.LOG_LEVEL, logging.INFO),
    )
    return logging.getLogger(name)
