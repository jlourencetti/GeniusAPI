import lyricsgenius as lg


class Genius:

    def __init__(self):

        self.ACCESS_TOKEN = "uUCpoTatmA3Q12NskIaGVRQyIKEued3AnnhbJ1ppPLgry1tqmN2oqFeNGCuWygE7"
        self.genius = lg.Genius(
            self.ACCESS_TOKEN, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"])

    def get_music(self, name, n_music):

        try:
            # Encontra o artista
            artist = self.genius.search_artist(
                name, max_songs=n_music, sort='popularity')
            # seleciona musica do artista
            artist_songs = artist.songs
            # Salva o titulo das musicas na lista
            artist_songs_title = [song.title for song in artist_songs]
            return artist_songs_title

        except: 
            print(f"Não foi possível encontrar as muśicas do artista: {name}")


if __name__ == '__main__':
    locate = Genius()
    dados = locate.get_music('u2', 10)
    print(dados)
