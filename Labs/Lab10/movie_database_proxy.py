from enum import Enum

from movie_database import *


class UserAccessEnum(Enum):
    ADMIN = 1
    MEMBER = 2


class MovieDatabaseProxy:
    """
    Wrapper for the MovieDatabase class.
    Has the same interface as MovieDatabase.
    """

    def __init__(self, access_level: UserAccessEnum, db_file_name: str,
                 movies: list = None):
        self.movie_database = MovieDatabase(db_file_name, movies)
        self.access_level = access_level
        self.cache = []  # I dont like this here when it gets set next call 🧐
        self.update_cache()

    def update_cache(self):
        self.cache = self.movie_database.view()

    def connect(self):
        self.movie_database.connect()

    def close_connection(self):
        self.movie_database.close_connection()

    def insert(self, movie: Movie):
        if self.access_level.value <= 1:
            self.cache.insert(movie)
            self.movie_database.insert(movie)

    def view(self) -> list:
        if self.access_level.value <= 2:
            return self.movie_database.view()

    def delete(self, movie_id: str):
        if self.access_level.value <= 1:
            # for movie in self.cache:
            # if movie.  you have to get the id somehow.
            self.movie_database.delete(movie_id)

    def search(self, title="", director="", language="",
               release_year="") -> Movie:
        if self.access_level.value <= 1:
            for movie in self.cache:
                if title in movie.title and director in movie.director and \
                        language in movie.language and release_year in \
                        movie.release_year:
                    return movie


def main():
    movies = [
        Movie(0, "Shrek", "Andrew Adamson", 2001, "ENG"),
        Movie(1, "Sharknado", "Anthony Ferrante", 2013, "ENG"),
        Movie(2, "La La Land", "Damien Chazelle", 2016, "ENG"),
        Movie(3, "Avengers Endgame", "Anthony Russo", 2019, "ENG")
    ]
    account_level = int(input("Access Level? 1: admin, 2: member > "))
    mdp = MovieDatabaseProxy(UserAccessEnum(account_level), "myDatabase",
                             movies)
    mdp.connect()
    print(mdp.view())
    print(mdp.search(input('title? > '), input('director? > '),
                     input('language? > '), input('release year? > ')))


if __name__ == '__main__':
    main()
