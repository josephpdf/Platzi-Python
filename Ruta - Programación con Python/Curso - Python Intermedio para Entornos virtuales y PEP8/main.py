# main.py - Todo el código en un archivo
"""
Sistema de análisis de noticias con APIs múltiples.
"""

# PEP 8: Configuración centralizada - constantes en MAYÚSCULAS con guiones bajos
API_TIMEOUT = 30
MAX_RETRIES = 3
DEFAULT_LANGUAGE = "es"  # PEP 8: Comillas dobles para strings


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


def newsapi_client(api_key, query, timeout=30, retries=3):
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
