import pytest
from domainmodel.user import User
from domainmodel.track import Track
from domainmodel.review import Review


def test__id():
    user = User(0, "name", "password")
    with pytest.raises(ValueError):
        user = User(-1, "name", "password")
        user2 = User("1", "name", "password")


def test_lowercase():
    user = User(0, "NAME", "password")
    assert user.user_name == "name"


def test_invalid_username():
    user = User(0, "", "password")
    user2 = User(0, 123, "password")
    assert user.user_name == None and user2.user_name == None


def test_password_length():
    user = User(0, "name", "1234567")
    user2 = User(0, "name2", "123456")
    assert user.password == "1234567" and user2.password == None


def test_check_equality():
    user = User(0, "name", "password")
    user2 = User(1, "name2", "password")
    user3 = User(1, "name3", "password")
    assert not user.__eq__(user2) and user2.__eq__(user3)


def test_adding_track():
    user = User(123, "Shyamli", "pw12345")
    track = Track(1, "Ab12")
    user.add_liked_track(track)
    assert user.liked_tracks == [track]


def test_remove_track():
    user = User(123, "Shyamli", "pw12345")
    track = Track(1, "Ab12")
    user.add_liked_track(track)
    user.remove_liked_track(track)
    assert track not in user.liked_tracks


def test_add_review():
    user = User(123, "Shyamli", "pw12345")
    track = Track(1, "Ab12")
    review = Review(track, "review text", 5)
    user.add_review(review)
    assert review in user.reviews


def test_remove_review():
    user = User(123, "Shyamli", "pw12345")
    track = Track(1, "Ab12")
    review = Review(track, "review text", 5)
    user.add_review(review)
    user.remove_review(review)
    assert review not in user.reviews
