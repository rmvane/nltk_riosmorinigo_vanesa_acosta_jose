"""
Parte 2 - Análisis del texto
Parte 3 - Conclusiones
-----------------------------------------------------------------------
Lee 'comentarios_youtube.txt' (generado por descargar_comentarios.py) y
aplica un pipeline básico de PLN con NLTK:

    tokenización -> normalización -> eliminación de puntuación
    -> eliminación de stopwords -> stemming -> frecuencias -> estadísticas

Antes de ejecutar, instalar las dependencias:
    pip install nltk

y descargar los recursos necesarios (solo la primera vez). El script lo
hace automáticamente si detecta que faltan.
"""

import string
import re

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.probability import FreqDist

# ----------------------------------------------------------------------
# Configuración
# ----------------------------------------------------------------------
ARCHIVO_ENTRADA = "comentarios_youtube.txt"
VIDEO_ANALIZADO = "¿Qué es y cómo funciona la INTELIGENCIA ARTIFICIAL? (canal Derivando)"
IDIOMA = "spanish"

# Palabras muy frecuentes en comentarios de YouTube que no aportan
# información sobre la temática del video (agradecimientos, muletillas,
# etc.). Se usan solo para detectar automáticamente el tema predominante,
# no se eliminan del resto del análisis.
PALABRAS_GENERICAS_COMENTARIO = {
    "gracias", "hola", "bien", "mejor", "solo", "si", "cada", "aunque",
    "buen", "buena", "canal", "video", "the", "ser", "hacer", "puede",
    "creo", "vez", "hace", "cosas", "the", "and", "of", "to", "is",
}


def asegurar_recursos_nltk():
    """Descarga los recursos de NLTK si no están disponibles localmente."""
    recursos = {
        "tokenizers/punkt": "punkt",
        "tokenizers/punkt_tab": "punkt_tab",
        "corpora/stopwords": "stopwords",
    }
    for ruta, nombre in recursos.items():
        try:
            nltk.data.find(ruta)
        except LookupError:
            nltk.download(nombre)


def leer_archivo(ruta: str) -> str:
    with open(ruta, "r", encoding="utf-8") as archivo:
        return archivo.read()


def main():
    asegurar_recursos_nltk()

    # ------------------------------------------------------------------
    # 1. Mostrar el texto original
    # ------------------------------------------------------------------
    texto = leer_archivo(ARCHIVO_ENTRADA)
    print("=" * 60)
    print("1. TEXTO ORIGINAL")
    print("=" * 60)
    print(texto)

    cantidad_comentarios = len([linea for linea in texto.splitlines() if linea.strip()])

    # ------------------------------------------------------------------
    # 2. Separar el texto en oraciones
    # ------------------------------------------------------------------
    oraciones = sent_tokenize(texto, language=IDIOMA)
    print("\n" + "=" * 60)
    print("2. ORACIONES ENCONTRADAS")
    print("=" * 60)
    for i, oracion in enumerate(oraciones, start=1):
        print(f"{i}. {oracion}")

    # ------------------------------------------------------------------
    # 3. Tokenizar el texto
    # ------------------------------------------------------------------
    tokens = word_tokenize(texto, language=IDIOMA)
    print("\n" + "=" * 60)
    print("3. TOKENS")
    print("=" * 60)
    print(tokens)

    # ------------------------------------------------------------------
    # 4. Normalizar (minúsculas)
    # ------------------------------------------------------------------
    tokens_normalizados = [token.lower() for token in tokens]
    print("\n" + "=" * 60)
    print("4. TOKENS NORMALIZADOS (minúsculas)")
    print("=" * 60)
    print(tokens_normalizados)

    # ------------------------------------------------------------------
    # 5. Eliminar puntuación y caracteres especiales
    # ------------------------------------------------------------------
    patron_valido = re.compile(r"^[a-záéíóúñü]+$")
    tokens_sin_puntuacion = [
        token for token in tokens_normalizados
        if token not in string.punctuation and patron_valido.match(token)
    ]
    print("\n" + "=" * 60)
    print("5. TOKENS SIN PUNTUACIÓN")
    print("=" * 60)
    print(tokens_sin_puntuacion)

    # ------------------------------------------------------------------
    # 6. Eliminar stopwords
    # ------------------------------------------------------------------
    stop_words = set(stopwords.words(IDIOMA))
    tokens_sin_stopwords = [
        token for token in tokens_sin_puntuacion if token not in stop_words
    ]
    print("\n" + "=" * 60)
    print("6. TOKENS SIN STOPWORDS")
    print("=" * 60)
    print(tokens_sin_stopwords)

    # ------------------------------------------------------------------
    # 7. Aplicar Stemming
    # ------------------------------------------------------------------
    stemmer = SnowballStemmer(IDIOMA)
    stems = [stemmer.stem(token) for token in tokens_sin_stopwords]

    print("\n" + "=" * 60)
    print("7. STEMMING (al menos 20 palabras)")
    print("=" * 60)
    print(f"{'Palabra original':<20}{'Stem':<20}")
    print("-" * 40)
    muestra = list(dict.fromkeys(tokens_sin_stopwords))[:20]  # 20 palabras únicas
    for palabra in muestra:
        print(f"{palabra:<20}{stemmer.stem(palabra):<20}")

    print(
        "\nPregunta: ¿Qué diferencias observa entre las palabras originales "
        "y los stems obtenidos?\n"
        "-> (Completar en el informe, analizando la tabla anterior)"
    )

    # ------------------------------------------------------------------
    # 8. Frecuencia de palabras
    # ------------------------------------------------------------------
    frecuencia = FreqDist(tokens_sin_stopwords)
    print("\n" + "=" * 60)
    print("8. LAS 20 PALABRAS MÁS FRECUENTES")
    print("=" * 60)
    for palabra, cantidad in frecuencia.most_common(20):
        print(f"{palabra:<20}{cantidad}")

    # ------------------------------------------------------------------
    # 9. Estadísticas
    # ------------------------------------------------------------------
    vocabulario = set(tokens_sin_stopwords)
    stems_diferentes = set(stems)

    print("\n" + "=" * 60)
    print("9. ESTADÍSTICAS")
    print("=" * 60)
    print(f"Cantidad de comentarios analizados: {cantidad_comentarios}")
    print(f"Cantidad de oraciones: {len(oraciones)}")
    print(f"Cantidad de tokens: {len(tokens)}")
    print(f"Cantidad de palabras (tokens normalizados): {len(tokens_normalizados)}")
    print(f"Cantidad de palabras luego de eliminar puntuación: {len(tokens_sin_puntuacion)}")
    print(f"Cantidad de palabras luego de eliminar stopwords: {len(tokens_sin_stopwords)}")
    print(f"Cantidad de palabras diferentes (vocabulario): {len(vocabulario)}")
    print(f"Cantidad de stems diferentes: {len(stems_diferentes)}")

    # ------------------------------------------------------------------
    # 10. Interpretación de resultados
    # ------------------------------------------------------------------
    top5 = [palabra for palabra, _ in frecuencia.most_common(5)]

    # --- Pregunta 2: temática predominante ---------------------------
    # Se toman las palabras más frecuentes descartando las genéricas de
    # comentario (agradecimientos, muletillas, etc.) para quedarnos con
    # las que sí describen el contenido del video.
    palabras_tematicas = [
        palabra for palabra, _ in frecuencia.most_common(30)
        if palabra not in PALABRAS_GENERICAS_COMENTARIO
    ][:5]
    tematica_texto = ", ".join(palabras_tematicas)

    # --- Pregunta 3: justificación del stemming -----------------------
    # Se agrupan todas las palabras (no solo la muestra de 20) según su
    # stem, y se buscan casos reales donde dos o más palabras distintas
    # cayeron en la misma raíz: esa es la evidencia de que el stemming
    # agrupó variantes con significado relacionado.
    mapa_stem_a_palabras = {}
    for palabra in set(tokens_sin_stopwords):
        stem_palabra = stemmer.stem(palabra)
        mapa_stem_a_palabras.setdefault(stem_palabra, set()).add(palabra)

    grupos_agrupados = {
        stem_palabra: palabras
        for stem_palabra, palabras in mapa_stem_a_palabras.items()
        if len(palabras) >= 2
    }
    ejemplos_agrupamiento = list(grupos_agrupados.items())[:5]

    print("\n" + "=" * 60)
    print("10. INTERPRETACIÓN DE RESULTADOS")
    print("=" * 60)

    print(f"1. Las cinco palabras más frecuentes fueron: {', '.join(top5)}")

    print(
        f"\n2. La temática predominante en los comentarios parece estar "
        f"relacionada con: {tematica_texto}. Estas palabras (excluyendo "
        f"saludos, agradecimientos y muletillas típicas de YouTube) son "
        f"las de mayor frecuencia real en el corpus."
    )

    if ejemplos_agrupamiento:
        ejemplos_texto = "; ".join(
            f"{stem_palabra} <- {', '.join(sorted(palabras))}"
            for stem_palabra, palabras in ejemplos_agrupamiento
        )
        print(
            f"\n3. Sí: el stemming agrupó palabras con significado "
            f"relacionado bajo una misma raíz. Se detectaron "
            f"{len(grupos_agrupados)} raíces que agrupan 2 o más palabras "
            f"distintas del corpus. Ejemplos concretos: {ejemplos_texto}."
        )
    else:
        print(
            "\n3. En este corpus no se detectaron palabras distintas que "
            "compartieran la misma raíz; el stemming no tuvo casos de "
            "agrupamiento para justificar."
        )

    # ------------------------------------------------------------------
    # Parte 3 - Conclusiones
    # ------------------------------------------------------------------
    print("\n" + "=" * 41)
    print("CONCLUSIONES")
    print("=" * 41)
    print(f"\nVideo analizado:\n{VIDEO_ANALIZADO}")
    print(f"\nCantidad de comentarios:\n{cantidad_comentarios}")
    print("\nLas palabras más frecuentes fueron:\n")
    for palabra, _ in frecuencia.most_common(5):
        print(palabra)

    if ejemplos_agrupamiento:
        stem_ejemplo, palabras_ejemplo = ejemplos_agrupamiento[0]
        print(
            "\nEl stemming permitió agrupar palabras con distintas "
            f"terminaciones bajo una misma raíz (por ejemplo, "
            f"{' y '.join(sorted(palabras_ejemplo))} se redujeron a "
            f"'{stem_ejemplo}')."
        )
    else:
        print(
            "\nEl stemming permitió agrupar palabras con distintas "
            "terminaciones bajo una misma raíz."
        )

    print(
        f"\nLa temática predominante de los comentarios está relacionada "
        f"con: {tematica_texto}."
    )


if __name__ == "__main__":
    main()