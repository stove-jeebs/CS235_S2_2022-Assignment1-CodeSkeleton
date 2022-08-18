class Album:
    def __init__(self, album_id, title):
        if isinstance(album_id, int) and album_id >= 0:
            self.__album_id = album_id
        else:
            raise ValueError("ERROR: album id needs to be an integer value")
        self.title = title

    @property
    def album_id(self):
        return self.__album_id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title.strip() if isinstance(title, str) and title != "" else None

    @property
    def album_url(self):
        return self.__album_url

    @album_url.setter
    def album_url(self, url):
        self.__album_url = url if isinstance(url, str) and url != "" else None

    @property
    def album_type(self):
        return self.__album_type

    @album_type.setter
    def album_type(self, album_type):
        self.__album_type = (
            album_type if isinstance(album_type, str) and album_type != "" else None
        )

    @property
    def release_year(self):
        return self.__release_year

    @release_year.setter
    def release_year(self, year):
        self.__release_year = year if isinstance(year, int) and year >= 0 else None

    def __repr__(self):
        return f"<Album {self.title}, album id = {self.album_id}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.album_id == other.album_id

    def __lt__(self, other):
        return self.album_id < other.album_id

    def __hash__(self):
        return hash(self.album_id)
