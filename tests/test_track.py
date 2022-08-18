import pytest
from domainmodel.track import Track
from domainmodel.genre import Genre


def test_add_genres():
    track = Track(16563, "compsci235")
    genre = Genre(1, "hello world")
    track.add_genre(genre)
    assert genre in track.genres
