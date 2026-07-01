from typing import Any


def formatar_rastreio(codigo: str, data: dict[str, Any], max_eventos: int = 5) -> str:
    eventos = data.get("eventos", [])

    if not eventos:
        return (
            f"📦 *Rastreamento: `{codigo.upper()}`*\n\n"
            "Encomenda encontrada, mas ainda sem eventos registrados.\n"
            "_Tente novamente em algumas horas._"
        )

    transportadora = data.get("transportadora", {}).get("nome", "Correios")
    servico = data.get("servico", {}).get("nome", "")
    total = len(eventos)

    linhas = [f"📦 *Rastreamento: `{codigo.upper()}`*"]
    if servico:
        linhas.append(f"🚚 {transportadora} — _{servico}_")
    else:
        linhas.append(f"🚚 {transportadora}")
    linhas.append("")

    for ev in eventos[:max_eventos]:
        data_hora = f"{ev.get('data', '')} {ev.get('hora', '')}".strip()

        unidade = ev.get("unidade", {})
        endereco = unidade.get("endereco", {})
        cidade = endereco.get("cidade", "") or ev.get("local", "")
        uf = endereco.get("uf", "")

        status = ev.get("descricao") or ev.get("status", "")
        detalhe = ev.get("detalhe", "")

        linha = f"🕐 *{data_hora}*"
        if cidade:
            linha += f" — {cidade}"
            if uf:
                linha += f"/{uf}"
        linha += f"\n{status}"
        if detalhe:
            linha += f"\n_{detalhe}_"

        linhas.append(linha)

    if total > max_eventos:
        linhas.append(f"\n_...e mais {total - max_eventos} evento(s) anteriores._")

    return "\n\n".join(linhas)


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
