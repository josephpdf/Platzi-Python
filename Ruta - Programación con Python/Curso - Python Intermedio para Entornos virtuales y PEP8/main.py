import json  # Clase 8 - Importación de librería para manejo de JSON
import urllib.parse  # Clase 8 - Importación de librería para manejo de URLs
import urllib.request  # Clase 8 - Importación de librería para hacer solicitudes HTTP

# main.py - Todo el código en un archivo
"""
Sistema de análisis de noticias con APIs múltiples.
"""

# PEP 8: Configuración centralizada - constantes en MAYÚSCULAS con guiones bajos
API_TIMEOUT = 30
MAX_RETRIES = 3
DEFAULT_LANGUAGE = "es"  # PEP 8: Comillas dobles para strings

API_KEY = "bf6563dd552b4572af251ef2460f22f4"  # Clase 8
BASE_URL = "https://newsapi.org/v2/everything"  # Clase 8


# PEP 8: Utilidades comunes del proyecto - funciones en snake_case
def clean_text(text):
    # PEP 8: 4 espacios por indentación, no tabs
    """Limpia y normaliza texto."""  # PEP 8: Docstrings en comillas dobles triples
    if not text:
        return ""
    return text.strip().lower()


# PEP 8: Doble líneas en blanco entre funciones para separar lógicamente
def validate_api_key(api_key):
    """Valida que la API key tenga formato correcto."""
    return len(api_key) > 10 and api_key.isalnum()


# PEP 8: Funciones principales - agrupadas después de utilidades
def fetch_news_from_api(api_name, query):
    """Obtiene noticias de una API específica."""
    pass


def process_article_data(raw_data):
    """Procesa datos crudos de artículo."""
    pass


# Longitud de línea: Máximo 88 caracteres (Ruff default)
# Indentación: 4 espacios, nunca tabs
# Nombres descriptivos: snake_case para funciones y variables
# Imports ordenados: estándar → terceros → locales
# Líneas en blanco: Separar funciones y clases lógicamente
# Comillas consistentes: Usar comillas dobles para strings

print("-----------------------------")


def newsapi_client_1(api_key, query, timeout=30, retries=3):
    return f"NewsAPI: {query} con timeout {timeout}"


def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    return f"Guardian {section} desde {from_date} con timeout {timeout}"


def ejemplo_args(*args):
    print(f"TODOS {args}")
    print(f"{type(args)}")


ejemplo_args("Este", "parametro", "acá")
ejemplo_args("hola", "mundo")
ejemplo_args()


print("-----------------------------")


def ejemplo_args(api_key, *args):
    print(f"api_key: {api_key}")
    print(f"args: {args}")
    print(f"type args: {type(args)}")
    print("====")


ejemplo_args("API_KEY_VALUE", "Este", "parametro", "acá")
ejemplo_args("API_KEY_VALUE", "Hola", "Mundo")
# ejemplo_args()

print("-----------------------------")


# Reto Clase 7 - Crear una funcion que sume los números que se le pasen como argumentos
def sumar_numeros_traditional(*args):
    return sum(args)


def sumar_numeros_comprenhension(*args):
    return sum([x for x in args if isinstance(x, (int, float))])


print(sumar_numeros_traditional(1, 2, 3, 50))
print("#######################")
print(sumar_numeros_comprenhension(1, 2, 3, "hOLA", 10.2, 50))


print("-----------------------------")


def ejemplo_kwargs(**kwargs):
    print(f"kewargs: {type(kwargs)}")
    print(f"kwargs: {kwargs}")
    print("====")


ejemplo_kwargs(key="value", llave="valor")

ejemplo_kwargs(
    api_key="DEMO",
    query="Noticias de Python",
    timeout=30,
    retries=3,
)

ejemplo_kwargs(
    api_key="DEMO_GUARDIAN",
    section="Sports",
    from_date="2020-10-20",
    timeout=30,
    retries=3,
)

print("-----------------------------")


def fetch_news(api_name, *args, **kwargs):
    """
    Fución flexible para conectar con la API
    """

    base_config = {
        "timeout": 30,
        "retries": 3,
    }

    config = {
        **base_config,
        **kwargs,
    }

    api_clients = {
        "newapi": newsapi_client,
        "guardian": guardian_client,
    }

    client = api_clients[api_name]
    return client(*args, **config)


# Reto clase 8 - Crear API en página de NewsAPI, instalar la librería request y agregar la libreria adentro de la función que me va a permitir consultar las noticias
# def get_news(api_key, topic="python"):
#     """Obtiene noticias usando requests (importado dentro de la función)."""
#     import requests  # Importación local de la librería

#     url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}&language=es"
#     response = requests.get(url)
#     return response.json()


# current_api_key = "bf6563dd552b4572af251ef2460f22f4"
# print(get_news(current_api_key, "Tecnología"))


# Solución clase 8
def newsapi_client(api_key, query, timeout=30, retries=3):
    query_string = urllib.parse.urlencode(
        {"q": query, "apiKey": api_key}
    )  # , "language": "es"
    # print(f"Query string: {query_string}")  # Imprime el query string generado
    url = f"{BASE_URL}?{query_string}"
    # print(f"URL completa: {url}")  # Imprime la URL completa antes de hacer la solicitud

    with urllib.request.urlopen(url, timeout=timeout) as response:
        data = response.read().decode("utf-8")
        return json.loads(data)  # Verifica que el JSON sea válido
    return f"NewsAPI: {query} con timeout {timeout}"


response_data = fetch_news("newapi", api_key=API_KEY, query="Python")
for article in response_data["articles"]:
    print(article["title"])
