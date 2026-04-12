# Catecismo Bot

Chatbot com RAG (Retrieval-Augmented Generation) baseado no **Catecismo Maior de São Pio X**.

Utiliza embeddings semânticos para buscar os trechos mais relevantes do Catecismo e a API da Anthropic (Claude) para gerar respostas fundamentadas no texto original.

---

## Como funciona

1. O texto do Catecismo é dividido em chunks (1 pergunta + resposta cada)
2. Cada chunk é convertido em um vetor de embedding e armazenado no ChromaDB
3. Quando o usuário faz uma pergunta, ela é embedada e comparada com os chunks armazenados
4. Os 3 chunks mais similares são enviados junto com a pergunta para a Claude API
5. A Claude responde com base exclusivamente no conteúdo do Catecismo

---

## Estrutura do projeto

```
catecismo-bot/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
├── backend/
│   ├── main.py          # API FastAPI (endpoint /perguntar)
│   ├── ingest.py        # Script de ingestão — roda uma vez
│   └── catechism.py     # Lógica de busca no ChromaDB
├── data/
│   └── catecismo_pio_x.pdf
├── .env.example
├── .gitignore
└── README.md
```

---

## Requisitos

- Python 3.10+
- Chave de API da Anthropic ([console.anthropic.com](https://console.anthropic.com))

---

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/catecismo-bot.git
cd catecismo-bot
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

```bash
cp .env.example .env
```

Abra o arquivo `.env` e adicione sua chave:

```
ANTHROPIC_API_KEY=sua_chave_aqui
```

### 5. Coloque o PDF na pasta correta

Copie o arquivo `Catecismo_Maior_de_Sao_Pio_X.pdf` para a pasta `data/`.

---

## Uso

### Passo 1 — Ingestão (roda uma única vez)

Processa o PDF, gera os embeddings e popula o banco vetorial:

```bash
cd backend
python ingest.py
```

Aguarde a conclusão. Isso criará a pasta `chroma_db/` com os dados processados.

### Passo 2 — Inicie o backend

```bash
cd backend
uvicorn main:app --reload
```

O servidor estará disponível em `http://localhost:8000`.

Para testar os endpoints diretamente, acesse `http://localhost:8000/docs`.

### Passo 3 — Abra o frontend

Abra o arquivo `frontend/index.html` no navegador.

---

## Dependências principais

| Pacote | Versão | Função |
|---|---|---|
| `fastapi` | ≥0.111 | Framework do backend |
| `uvicorn` | ≥0.29 | Servidor ASGI |
| `anthropic` | ≥0.25 | Cliente da Claude API |
| `chromadb` | ≥0.5 | Banco vetorial local |
| `sentence-transformers` | ≥3.0 | Geração de embeddings |
| `pypdf` | ≥4.0 | Extração de texto do PDF |
| `python-dotenv` | ≥1.0 | Leitura do arquivo `.env` |

---

## Observações

- O banco vetorial (`chroma_db/`) é gerado localmente e não deve ser versionado
- Nunca suba o arquivo `.env` com sua chave de API para o repositório
- O bot responde apenas com base no conteúdo do Catecismo — não gera respostas por conta própria