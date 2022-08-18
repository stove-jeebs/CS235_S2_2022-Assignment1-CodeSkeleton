import datetime
from track import Track


class Review:
    def __init__(self, track, review_text, rating):
        self.__track = track if isinstance(track, Track) else None
        self.review_text = review_text
        self.rating = rating
        self.__timestamp = datetime.datetime.now()

    @property
    def track(self):
        return self.__track

    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def review_text(self):
        return self.__review_text

    @review_text.setter
    def review_text(self, text):
        self.__review_text = (
            text.strip() if isinstance(text, str) and text != "" else "N/A"
        )

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, number):
        if isinstance(number, int) and 0 < number < 6:
            self.__rating = number
        else:
            raise ValueError("rating must be an integer between 1 and 5 inclusive")

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (
            self.track == other.track
            and self.review_text == other.review_text
            and self.rating == other.rating
            and self.timestamp == other.timestamp
        )
