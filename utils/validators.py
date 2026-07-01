import re

# Padrão oficial dos Correios: 2 letras + 8 dígitos + 2 letras (ex: AA123456789BR)
_PADRAO_CORREIOS = re.compile(r"^[A-Z]{2}\d{9}[A-Z]{2}$", re.IGNORECASE)


def validar_codigo(codigo: str) -> bool:
    return bool(_PADRAO_CORREIOS.match(codigo.strip()))
