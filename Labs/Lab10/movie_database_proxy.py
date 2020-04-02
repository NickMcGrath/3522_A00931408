"""
This module adds a wrapper class for move_database module and tests it.
"""
from enum import Enum
from movie_database import *


class InvalidPermission(Exception):
    """Exception for invalid permission for database functions."""

    def __init__(self):
        super().__init__()


class UserAccessEnum(Enum):
    """
    Enum representing levels of permissions. note lower level higher
    permission
    """

    ADMIN = 1
    MEMBER = 2


class MovieDatabaseProxy:
    """
    Wrapper for the MovieDatabase class, adds cache and permissions.
    Has the same interface as MovieDatabase.
    """

    def __init__(self, access_level: UserAccessEnum, db_file_name: str,
                 movies: list = None):
        """
        Initialize and set cache.
        :param access_level: UserAccessEnum
        :param db_file_name: str
        :param movies: list of movies
        """
        self.movie_database = MovieDatabase(db_file_name, movies)
        self.access_level = access_level
        self.cache = []  # I dont like this here when it gets set next call 🧐
        self.update_cache()

    def update_cache(self):
        """
        Updates the cache with all the movies in the database.
        :return:
        """
        self.cache = self.movie_database.view()

    def connect(self):
        """
        Establishes a connection to the database and instantiates the
        cursor as well. If the movies table or the file does not exist,
        it creates one.
        """
        self.movie_database.connect()

    def close_connection(self):
        """
        Closes the connection to the database preventing further changes.
        """
        self.movie_database.close_connection()

    def insert(self, movie: Movie):
        """
        Inserts a row into the movies database and cache. Refer to the column
        headings in the class comments to see what the movies database
        is composed of.
        :param movie Movie
        :return:
        """
        if self.access_level.value > 1:
            raise InvalidPermission()
        result = self.movie_database.insert(movie)
        # note this is questionable. because there is no return from
        # insert you cant tell what id it will be set to. And calling
        # update_cache is a lot of resources.
        movie.key = result.key
        self.cache.append(movie)

    def view(self) -> list:
        """
        Retrieves all the rows in the movies table from cache, if cache is
        empty, updates cache from database.
        :return: a list of Movies.
        """
        if self.access_level.value > 2:
            raise InvalidPermission()
        if len(self.cache) == 0:
            self.update_cache()
        return self.cache

        # return self.movie_database.view()

    def delete(self, movie_id: str):
        """
        Deletes a row specified by the key in the movies table and
        cache.
        :param movie_id: an int
        """
        if self.access_level.value > 1:
            raise InvalidPermission()
        for movie in self.cache:
            if movie.key == movie_id:
                self.cache.remove(movie)
                break
        self.movie_database.delete(movie_id)

    def search(self, title="", director="", language="",
               release_year=0) -> Movie:
        """
        Retrieves the rows that match any combination of the given
        parameters.
        :param title: a string
        :param director: a string
        :param language: a string, ISO language code
        :param release_year: an int
        :return: a list of rows
        """
        if self.access_level.value > 2:
            raise InvalidPermission()
        results = []
        for movie in self.cache:
            if title in movie.title \
                    and director in movie.director \
                    and language in movie.language \
                    and (release_year == movie.release_year
                         or release_year == 0):
                results.append(movie)
        if len(results) > 0:
            return results
        else:
            print('in else')
            results = self.movie_database.search(title, director, language,
                                                 release_year)
            # no need to if check because wrapee will return a empty list if
            # none
            self.cache.extend(results)
            return results


def main():
    """
    Creates a test area for testing permissions and functions.
    :return: int
    """
    try:
        movies = [
            Movie("Shrek", "Andrew Adamson", 2001, "ENG", 0),
            Movie("Sharknado", "Anthony Ferrante", 2013, "ENG", 1),
            Movie("La La Land", "Damien Chazelle", 2016, "ENG", 2),
            Movie("Avengers Endgame", "Anthony Russo", 2019, "ENG", 3)
        ]
        # create 2 proxies
        account_level = int(input("Access Level proxy1? 1: admin, 2: member "
                                  "> "))
        proxy1 = MovieDatabaseProxy(UserAccessEnum(account_level),
                                    "myDatabase")
        account_level = int(input("Access Level proxy2? 1: admin, 2: member "
                                  "> "))
        proxy2 = MovieDatabaseProxy(UserAccessEnum(account_level),
                                    "myDatabase")

        proxy1.connect()
        proxy2.connect()

        # allow for terminal testing
        while True:
            print('-' * 17)
            print('options:')
            print('"0": view')
            print('"1": search')
            print('"2": insert')
            print('"3": delete')
            print('"exit": exit')
            option = input()

            if option == 'exit':
                break

            proxy = proxy1 if input('proxy? ("1" or "2") > ') == '1' \
                else proxy2
            if option == '0':
                for movie in proxy.view():
                    print('-' * 17)
                    print(movie)
            elif option == '1':
                title = input('title? > ')
                director = input('director? > ')
                lang = input('lang? > ')
                try:
                    year = int(input('release year? > '))
                except ValueError:
                    year = 0
                search = proxy.search(title, director, lang, year)
                for movie in search:
                    print('-' * 17)
                    print(movie)
            elif option == '2':
                movie = Movie(input('title? > '), input('director? > '),
                              int(input('release year? > ')),
                              input('lang? > '))
                proxy.insert(movie)
            elif option == '3':
                proxy.delete(int(input('id to remove > ')))

        proxy1.close_connection()
        proxy2.close_connection()
    # catch if user is trying to access functions they should not
    except InvalidPermission:
        print('Not enough permission buckaroo')
        proxy1.close_connection()
        proxy2.close_connection()


if __name__ == '__main__':
    main()
