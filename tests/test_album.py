import pytest
from domainmodel.album import Album


def test_invalid_id():
    with pytest.raises(ValueError):
        album = Album(-1, "person")
    with pytest.raises(ValueError):
        album = Album("asdf", "person")
    with pytest.raises(ValueError):
        album = Album(None, "person")


def test_invalid_title():
    album = Album(1, "")
    assert album.title == None

    album = Album(2, -123)
    assert album.title == None


def test_invalid_id_and_title():
    with pytest.raises(ValueError):
        album = Album("", -123)
        assert album.title == None


def test_url():
    album = Album(1, "person")
    album.album_url = "http://album.com"
    assert album.album_url == "http://album.com"
    album.album_url = 123
    assert album.album_url == None


def test_type():
    album = Album(1, "person")
    album.album_type = "type"
    assert album.album_type == "type"
    album.album_type = 123
    assert album.album_type == None


def test_release_year():
    album = Album(1, "person")
    album.release_year = 2020
    assert album.release_year == 2020
    album.release_year = "2020"
    assert album.release_year == None


def test_equal():
    album = Album(1, "person")
    album2 = Album(2, "person2")
    assert album.__eq__(album2) == False


def test_not_equal():
    album = Album(3, "person")
    album2 = Album(3, "person2")
    assert album.__eq__(album2)


def test_less_than():
    album = Album(1, "person")
    album2 = Album(2, "person")
    assert album.__lt__(album2)

    album = Album(1, "person")
    album2 = Album(2, "person")
    assert album2.__lt__(album) == False
