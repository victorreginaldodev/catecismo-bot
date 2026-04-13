from sentence_transformers import SentenceTransformer

modelo = SentenceTransformer("all-MiniLM-L6-v2")

def gerar_embeddings(chunks: list) -> list:
    return modelo.encode(chunks)