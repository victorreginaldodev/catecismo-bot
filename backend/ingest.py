import chromadb
from utils.extrair_texto import extrair_texto
from utils.chunking import chunking
from utils.embedding import gerar_embeddings

PDF_PATH = "../data/catecismo-maior-de-sao-pio-x.pdf"
CHROMA_PATH = "../chroma_db"
COLLECTION_NAME = "catecismo"


def salvar_no_chromadb(chunks: list, embeddings: list) -> None:
    cliente = chromadb.PersistentClient(path=CHROMA_PATH)

    colecao = cliente.get_or_create_collection(name=COLLECTION_NAME)

    ids = [str(i) for i in range(len(chunks))]

    colecao.add(
        ids=ids,
        documents=chunks,
        embeddings=[e.tolist() for e in embeddings],
    )

    print(f"{len(chunks)} chunks salvos no ChromaDB.")


if __name__ == "__main__":
    print("Extraindo texto do PDF...")
    texto = extrair_texto(PDF_PATH)
    print(f"Total de caracteres: {len(texto)}")

    print("\nFazendo chunking...")
    chunks = chunking(texto)
    print(f"Total de chunks: {len(chunks)}")

    print("\nGerando embeddings...")
    embeddings = gerar_embeddings(chunks)
    print(f"Embeddings gerados: {len(embeddings)}")

    print("\nSalvando no ChromaDB...")
    salvar_no_chromadb(chunks, embeddings)

    print("\nIngestão concluída.")