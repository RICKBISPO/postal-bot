# 🤖 Bot de Rastreamento dos Correios

Bot para Telegram que consulta o status de encomendas dos Correios via [Seu Rastreio](https://seurastreio.com.br).

## Estrutura

```
rastreio_bot/
├── main.py                  # Ponto de entrada
├── config.py                # Carrega variáveis do .env
├── requirements.txt
├── .env.example             # Modelo de configuração
├── handlers/
│   ├── commands.py          # /start, /ajuda
│   └── messages.py          # Recebe e processa códigos de rastreio
├── services/
│   └── rastreio.py          # Chamada à API do Seu Rastreio
└── utils/
    ├── formatters.py        # Formata as mensagens para o Telegram
    ├── validators.py        # Valida o formato do código de rastreio
    └── logger.py            # Logger centralizado
```

## Como configurar

### 1. Clonar e instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Criar o bot no Telegram

- Fale com [@BotFather](https://t.me/BotFather)
- Envie `/newbot` e siga as instruções
- Copie o token gerado

### 3. Gerar chave da API

- Crie conta em [seurastreio.com.br](https://seurastreio.com.br)
- Acesse **Dashboard → Chaves de API** e gere uma chave gratuita

### 4. Configurar o .env

```bash
cp .env.example .env
```

Edite o `.env` e preencha:

```
TELEGRAM_TOKEN=seu_token_aqui
SEURASTREIO_API_KEY=sua_chave_aqui
```

### 5. Rodar

```bash
python main.py
```

## Comandos do bot

| Comando  | Descrição                        |
|----------|----------------------------------|
| /start   | Boas-vindas                      |
| /ajuda   | Instruções de uso                |
| (texto)  | Consulta o código de rastreio    |

## Variáveis de ambiente

| Variável              | Obrigatória | Padrão | Descrição                          |
|-----------------------|-------------|--------|------------------------------------|
| `TELEGRAM_TOKEN`      | ✅          | —      | Token do @BotFather                |
| `SEURASTREIO_API_KEY` | ✅          | —      | Chave da API do Seu Rastreio       |
| `MAX_EVENTOS`         | ❌          | 5      | Nº máximo de eventos exibidos      |
| `REQUEST_TIMEOUT`     | ❌          | 10     | Timeout HTTP em segundos           |
| `LOG_LEVEL`           | ❌          | INFO   | Nível de log (DEBUG/INFO/WARNING)  |
