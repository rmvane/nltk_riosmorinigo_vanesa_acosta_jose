Trabajo Práctico Integrador – Procesamiento de Lenguaje Natural con NLTK
Nombre y apellido: Roxana Vanesa Ríos Morínigo y José Acosta
Institución: INSTITUTO DE EDUCACIÓN SUPERIOR U.E.G.P. Nº 106
Carrera: Tecnicatura Superior en Ciencia de Datos e IA
Asignatura: Procesamiento de Lenguaje Natural

Este repositorio contiene el desarrollo del Trabajo Práctico Integrador de Procesamiento de Lenguaje Natural (PLN), donde se implementó un pipeline completo de análisis de texto en Python sobre comentarios extraídos de YouTube.

Objetivo del trabajo
Aplicar técnicas básicas de Procesamiento del Lenguaje Natural (PLN) utilizando la biblioteca NLTK, trabajando sobre comentarios reales obtenidos de un video de YouTube (tokenización, normalización, eliminación de puntuación y stopwords, stemming y análisis de frecuencias).

Video analizado
•	URL: https://www.youtube.com/watch?v=_tA5cinv0U8
•	Título: ¿Qué es y cómo funciona la INTELIGENCIA ARTIFICIAL? (canal Derivando)
•	Cantidad de comentarios descargados: 117

Bibliotecas utilizadas
•	nltk: tokenización (sent_tokenize, word_tokenize), stopwords, stemming (SnowballStemmer) y frecuencias (FreqDist).
•	youtube-comment-downloader: descarga de comentarios de YouTube sin necesidad de API key.

Instrucciones para ejecutar el programa
1.	Clonar el repositorio: https://github.com/rmvane/nltk_riosmorinigo_vanesa_acosta_jose.git 
2.	git clone https://github.com/rmvane/nltk_riosmorinigo_vanesa_acosta_jose.git 
3.	cd nltk_riosmorinigo_vanesa_acosta_jose 
4.	Crear un entorno virtual:
5.	python -m venv venv
6.	venv\Scripts\activate        # Windows
7.	REQUISITO instalar las dependencias (Terminal):
•	pip install nltk 
•	pip install youtube-comment-downloader 
8.	Descargar los recursos de NLTK (solo la primera vez):
•	import nltk
•	nltk.download("punkt")
•	nltk.download("punkt_tab")
•	nltk.download("stopwords")
9.	Asegurarse que se encuentre descargado el archivo comentarios_youtube.txt 
Aclaración: Si no está el archivo comentarios_youtube.txt ejecutar el archivo descargar_comentarios.py sino no es necesario ejecutarlo. Esto genera el archivo comentarios_youtube.txt.
10.	Ejecutar el análisis: analizar_comentarios.py
Esto muestra en consola, en orden: el texto original, la separación en oraciones, la tokenización, la normalización, la eliminación de puntuación y stopwords, una tabla de stemming de al menos 20 palabras, las 20 palabras más frecuentes, las estadísticas del corpus, la interpretación de resultados y el bloque final de conclusiones.
