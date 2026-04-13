TAMANHO_CHUNK = 600
SOBREPOSICAO = 100


def chunking(texto: str) -> list:
    resultado = []
    i = 0

    while i < len(texto):
        chunk = texto[i : i + TAMANHO_CHUNK]
        resultado.append(chunk)
        i += TAMANHO_CHUNK - SOBREPOSICAO

    return resultado