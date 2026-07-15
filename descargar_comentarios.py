from youtube_comment_downloader import YoutubeCommentDownloader, SORT_BY_POPULAR
VIDEO_URL = "https://www.youtube.com/watch?v=_tA5cinv0U8"
downloader = YoutubeCommentDownloader()
comentarios = downloader.get_comments_from_url(
VIDEO_URL,
sort_by = SORT_BY_POPULAR
)
with open("comentarios_youtube.txt", "w", encoding="utf-8") as archivo:
    # La sangría (4 espacios) indica que este bucle es parte del archivo abierto
    for i, comentario in enumerate(comentarios):
        if i >= 100:  # Limitar a los primeros 100 comentarios
            break
        archivo.write(comentario["text"] + "\n")
print("Comentarios descargados correctamente.")

