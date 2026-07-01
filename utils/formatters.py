from datetime import datetime, timezone
from typing import Any


def _formatar_data(iso: str) -> str:
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        dt_local = dt.astimezone()
        return dt_local.strftime("%d/%m/%Y %H:%M")
    except (ValueError, AttributeError):
        return iso


def formatar_rastreio(codigo: str, data: dict[str, Any]) -> str:
    if not data.get("success") or data.get("status") != "found":
        return (
            f"📦 *Rastreamento: `{codigo.upper()}`*\n\n"
            "❌ Objeto não encontrado. Verifique o código e tente novamente.\n"
            "_Pode levar até 24h para aparecer no sistema._"
        )

    ev = data.get("eventoMaisRecente", {})
    descricao = ev.get("descricao", "")
    detalhe = ev.get("detalhe", "")
    local = ev.get("local", "")
    data_hora = _formatar_data(ev.get("data", "")) if ev.get("data") else ""
    link = data.get("linkDetalhesCompletos", "")

    linhas = [f"📦 *Rastreamento: `{codigo.upper()}`*", ""]

    linha_evento = f"🕐 *{data_hora}*" if data_hora else ""
    if local:
        linha_evento += f" — {local}"
    if linha_evento:
        linhas.append(linha_evento)

    if descricao:
        linhas.append(descricao)
    if detalhe:
        linhas.append(f"_{detalhe}_")

    if link:
        linhas.append("")
        linhas.append(f"🔗 [Ver detalhes completos]({link})")

    return "\n".join(linhas)


def formatar_erro(status_code: int) -> str:
    mensagens = {
        404: "❌ Código não encontrado. Verifique se está correto.",
        429: "⚠️ Limite de consultas atingido. Tente novamente mais tarde.",
        401: "🔑 Chave de API inválida. Verifique a configuração do bot.",
    }
    return mensagens.get(
        status_code,
        f"⚠️ Erro ao consultar o serviço (HTTP {status_code}). Tente novamente.",
    )
