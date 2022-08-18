from domainmodel.artist import Artist
from domainmodel.genre import Genre
from domainmodel.album import Album


class Track:
    def __init__(self, track_id: int, title: str) -> None:
        if isinstance(track_id, int) and track_id >= 0:
            self.__track_id = track_id
        else:
            raise ValueError("ERROR: track id needs to be an integer value")
        self.title = title
        self.__genres = []

    @property
    def track_id(self) -> int:
        return self.__track_id

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title.strip() if isinstance(title, str) and title != "" else None

    @property
    def album(self):
        return self.__album

    @album.setter
    def album(self, album):
        self.__album = album if isinstance(album, Album) else None

    @property
    def artist(self):
        return self.__artist

    @artist.setter
    def artist(self, artist):
        self.__artist = artist if isinstance(artist, Artist) else None

    @property
    def genres(self):
        return self.__genres

    @genres.setter
    def genres(self, genres):
        if isinstance(genres, list):
            self.__genres = genres

    @property
    def track_duration(self):
        return self.__track_duration

    @track_duration.setter
    def track_duration(self, duration):
        if isinstance(duration, int) and duration >= 0:
            self.__track_duration = duration
        else:
            raise ValueError("ERROR: track duration must be a positive integer")

    @property
    def track_url(self) -> str:
        return self.__track_url

    @track_url.setter
    def track_url(self, url):
        if isinstance(url, str) and url != "":
            self.__track_url = url
        else:
            self.__track_url = None

    def __repr__(self):
        return f"<Track {self.title}, track id = {self.track_id}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.track_id == other.track_id

    def __lt__(self, other):
        return self.track_id < other.track_id

    def __hash__(self):
        return hash(self.track_id)

    def add_genre(self, genre):
        self.__genres.append(genre)
