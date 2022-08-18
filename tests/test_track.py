import pytest
from domainmodel.track import Track


class TestTrack:
    def test_add_genres(self):
        track1 = Track(16563, "compsci235")
        track1.add_genre("hello world")
        assert track1.genres == ["hello world"]
