import os
import csv
import ast

from domainmodel.artist import Artist
from domainmodel.album import Album
from domainmodel.genre import Genre
from domainmodel.track import Track
from domainmodel.review import Review
from domainmodel.user import User


class TrackCSVReader:
    def __init__(self, albums_csv_file: str, tracks_csv_file: str):
        self.__albums_csv_file = f"{os.getcwd()}/data/{albums_csv_file}"
        self.__tracks_csv_file = f"{os.getcwd()}/data/{tracks_csv_file}"

        self.__dataset_of_tracks = []
        # Set of unique artists
        self.__dataset_of_artists = set()
        # Set of unique albums
        self.__dataset_of_albums = set()
        # Set of unique genres
        self.__dataset_of_genres = set()

    @property
    def dataset_of_tracks(self) -> list:
        return self.__dataset_of_tracks

    @property
    def dataset_of_albums(self) -> set:
        return self.__dataset_of_albums

    @property
    def dataset_of_artists(self) -> set:
        return self.__dataset_of_artists

    @property
    def dataset_of_genres(self) -> set:
        return self.__dataset_of_genres

    def read_csv_files(self):
        # tracks csv file
        with open(self.__tracks_csv_file, "r", encoding="unicode_escape") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # create track object
                track = Track(int(row["track_id"]), row["track_title"])
                self.dataset_of_tracks.append(track)

                # add album
                track.album = (
                    Album(int(row["album_id"]), row["album_title"])
                    if row["album_id"] != ""
                    else None
                )

                # add artist
                artist = Artist(int(row["artist_id"]), row["artist_name"])
                track.artist = artist
                self.dataset_of_artists.add(artist)

                # add genre
                if row["track_genres"] != "":
                    for genres_dict in ast.literal_eval(row["track_genres"]):
                        genre = Genre(
                            int(genres_dict["genre_id"]), genres_dict["genre_title"]
                        )
                        track.add_genre(genre)
                        self.dataset_of_genres.add(genre)

        # albums csv file
        with open(self.__albums_csv_file, "r", encoding="unicode_escape") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.__dataset_of_albums.add(
                    Album(int(row["album_id"]), row["album_title"])
                )
