sample_articles = [
    {
        "title": "Python logra nuevo éxito",
        "source": {"name": "TechNews"},
        "description": "Gran noticia",
        "category": "Tecnología",
    },
    {
        "title": "Mercado en crisis",
        "source": {"name": "Finance"},
        "description": "Análisis completo",
        "category": "Economía",
    },
    {
        "title": "Nueva tecnología",
        "source": {"name": "TechNews"},
        "description": "Innovación",
        "category": "Tecnología",
    },
    {
        "title": "Deportes hoy",
        "source": {"name": "Sports"},
        "description": "Resultados",
        "category": "Deportes",
    },
    {
        "title": "Política actual",
        "source": {"name": "News"},
        "description": "Actualidad",
        "category": "Política",
    },
    {
        "title": "Ciencia avanza",
        "source": {"name": "Science"},
        "description": "Descubrimientos",
        "category": "Ciencia",
    },
]


# Retorno de lista tradicional vs comprehension
def extract_titles_traditional(articles):
    """Extrae solo los títulos usando un for"""
    titles = []
    for article in articles:
        titles.append(article["title"])
    return titles


def extract_titles(articles):
    """Extrae solo los títulos usando un comprehension"""
    return [article["title"] for article in articles]


print(extract_titles_traditional(sample_articles))
print("-------------------------")
print(extract_titles(sample_articles))


print("#################################")


# Retorno de lista tradicional vs comprehension con filtro
def extract_titles_traditional(articles):
    """Extrae solo los títulos usando un for"""
    titles = []
    for article in articles:
        if len(article["title"]) > 15:  # Filtrar títulos largos
            titles.append(article["title"])
    return titles


def extract_titles(articles):
    """Extrae solo los títulos usando un comprehension"""
    return [
        article["title"] for article in articles if len(article["title"]) > 15
    ]  # Filtrar títulos largos


print(extract_titles_traditional(sample_articles))
print("-------------------------")
print(extract_titles(sample_articles))


print("#################################")


# Retorno de diccionario tradicional vs comprehension
def extract_articles_summaries(articles):
    return {article["title"]: article["description"] for article in articles}


def extract_article_summaries_filter(articles):
    return {
        article["title"]: article["description"]
        for article in articles
        if len(article["description"]) > 15
    }


print(extract_articles_summaries(sample_articles))
print("-------------------------")
print(extract_article_summaries_filter(sample_articles))


print("#################################")


# Reto Lista sin que se repita de todas fuentes usando set, primero  tradicional y luego comprehension
def extract_name_sources_traditional(articles):
    """Extrae solo los nombres de las fuentes de los artículos sin que se repitan"""
    sources = set()  # Usamos un set para evitar duplicados
    for article in articles:  # Iteramos sobre cada artículo
        sources.add(
            article["source"]["name"]
        )  # Agregamos el nombre de la fuente al set
    return list(sources)  # Convertimos el set a lista para el retorno


def extract_name_sources(articles):
    """Extrae solo los nombres de las fuentes de los artículos sin que se repitan usando comprensión de listas."""
    return list(
        {article["source"]["name"] for article in articles}
    )  # Usamos un set comprehension para obtener nombres únicos y luego convertimos a lista


print(extract_name_sources_traditional(sample_articles))
print("-------------------------")
print(extract_name_sources(sample_articles))

print("#################################")


# Soluciion del reto del profesor
def get_sources_traditional(articles):
    sources = set()
    for article in articles:
        if article.get("source") and article.get("source").get("name"):
            sources.add(article.get("source").get("name"))
    return sources


def get_sources(articles):
    # {expression
    # for member in iterable
    # [if condition]
    # }
    return {
        article.get("source").get("name")
        for article in articles
        if article.get("source") and article.get("source").get("name")
    }


print(get_sources_traditional(sample_articles))
print("-------------------------")
print(get_sources(sample_articles))

print("#################################")


# Clase 4 -  Categorizar
def categorize_traditional(articles):
    sources = get_sources(sample_articles)
    results = {}
    for source in sources:
        if source not in results:
            results[source] = []

        for article in articles:
            if source == article.get("source").get("name"):
                results[source].append(article)
    return results


def categorize(articles):
    sources = get_sources(sample_articles)
    return {
        source: [
            article
            for article in articles
            if source == article.get("source").get("name")
        ]
        for source in sources
    }


print(categorize_traditional(sample_articles))
print("-------------------------")
print(categorize(sample_articles))
