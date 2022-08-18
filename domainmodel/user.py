class User:
    def __init__(self, id, username, password):
        pass

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, id):
        pass

    @property
    def user_name(self):
        self.__user_name

    @user_name.setter
    def user_name(self, name):
        pass

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        pass

    @property
    def liked_tracks(self):
        return self.__liked_tracks

    @liked_tracks.setter
    def liked_tracks(self, tracks):
        pass

    @property
    def reviews(self):
        return self.__reviews

    @reviews.setter
    def reviews(self, reviews):
        pass

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

    def add_liked_track(track):
        pass

    def remove_liked_track(track):
        pass

    def add_review(review):
        pass

    def remove_review(review):
        pass
