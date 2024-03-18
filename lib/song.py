class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.update_collection(self)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if cls.genres.count(genre) == 0:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        if cls.artists.count(artist) == 0:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre) == None:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist) == None:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1

    @classmethod
    def update_collection(cls, song):
        cls.add_song_to_count()
        cls.add_to_genres(song.genre)
        cls.add_to_artists(song.artist)
        cls.add_to_genre_count(song.genre)
        cls.add_to_artist_count(song.artist)
