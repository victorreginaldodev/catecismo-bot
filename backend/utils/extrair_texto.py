from pypdf import PdfReader

def extrair_texto(caminho: str) -> str:
    reader  = PdfReader(caminho)
    texto = ""
    
    for pagina in reader .pages:
        texto += pagina.extract_text()
        
    return texto