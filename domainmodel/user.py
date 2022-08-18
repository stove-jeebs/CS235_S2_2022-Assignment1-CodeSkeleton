from track import Track
from review import Review


class User:
    def __init__(self, id, username, password):
        if isinstance(id, int) and id >= 0:
            self.__user_id = id
        else:
            raise ValueError("user id must be a positive integer")
        self.__user_name = (
            username.strip().lower()
            if isinstance(username, str) and username != ""
            else None
        )

        self.__password = (
            password if isinstance(password, str) and len(password) >= 7 else None
        )
        self.__liked_tracks = []
        self.__reviews = []

    @property
    def user_id(self):
        return self.__user_id

    @property
    def user_name(self):
        return self.__user_name

    @property
    def password(self):
        return self.__password

    @property
    def liked_tracks(self):
        return self.__liked_tracks

    @property
    def reviews(self):
        return self.__reviews

    def __repr__(self):
        return f"<User {self.user_name}, user id = {self.user_id}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.user_id == other.user_id

    def __lt__(self, other):
        return self.user_id < other.user_id

    def __hash__(self):
        return hash(self.user_id)

    def add_liked_track(self, track):
        if isinstance(track, Track) and track not in self.liked_tracks:
            self.liked_tracks.append(track)

    def remove_liked_track(self, track):
        if track in self.liked_tracks:
            self.liked_tracks.remove(track)

    def add_review(self, review):
        if isinstance(review, Review) and review not in self.reviews:
            self.reviews.append(review)

    def remove_review(self, review):
        if review in self.reviews:
            self.reviews.remove(review)
