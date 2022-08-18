class Artist:
    def __init__(self, artist_id, full_name):
        self.artist_id = artist_id
        self.full_name = full_name

    @property
    def artist_id(self):
        return self.__artist_id

    @artist_id.setter
    def artist_id(self, id):
        if isinstance(id, int) and id >= 0:
            self.__artist_id: int = id
        else:
            raise ValueError("ERROR: artist id needs to be an integer value")

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, new_full_name):
        if isinstance(new_full_name, str) and new_full_name != "":
            self.__full_name = new_full_name.strip()
        else:
            self.__full_name = None

    def __repr__(self):
        # we use access via the property here
        return f"<Artist {self.full_name}, artist id = {self.artist_id}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.artist_id == other.artist_id

    def __lt__(self, other):
        return self.artist_id < other.artist_id

    def __hash__(self):
        return hash(self.artist_id)
