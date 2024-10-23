

from urllib.parse import urlparse
from Test .json_open import json_read_file
def verificar_url(url, lista_urls):
    # Parse a URL de entrada
    parsed_url = urlparse(url)

    # Verifica se a URL está na lista
    for lista_url in lista_urls:
        if parsed_url.netloc == urlparse(lista_url).netloc and parsed_url.path == urlparse(lista_url).path:
            return lista_url  # Retorna a URL que está na lista
    return None

# Exemplo de uso
#lista_urls = [
    'https://www.exemplo.com/pagina1',
    'http://www.exemplo2.com/pagina2',
    'https://www.exemplo.com/pagina2',
    'https://www.atlantico.ao/'




#]

lista_urls=json_read_file.read_json()

url_para_verificar = 'https://www.bancobai.ao'

url_encontrada = verificar_url(url_para_verificar, lista_urls)

if url_encontrada:
    print(f"A URL encontrada na lista: {url_encontrada}")
else:
    print("A URL não está na lista.")

