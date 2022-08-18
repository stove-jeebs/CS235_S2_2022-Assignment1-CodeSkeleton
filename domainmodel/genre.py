class Genre:
    def __init__(self, genre_id, genre_name):
        self.genre_id = genre_id
        self.name = genre_name

    @property
    def genre_id(self):
        return self.__genre_id

    @genre_id.setter
    def genre_id(self, id):
        if isinstance(id, int) and id >= 0:
            self.__genre_id = id
        else:
            raise ValueError("ERROR: genre id needs to be an integer value")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and name != "":
            self.__name = name.strip()
        else:
            self.__name = None

    def __repr__(self):
        return f"<Genre {self.name}, genre id = {self.genre_id}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.genre_id == other.genre_id

    def __lt__(self, other):
        return self.genre_id < other.genre_id

    def __hash__(self):
        return hash(self.genre_id)
