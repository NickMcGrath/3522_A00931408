"""Write a simple program that accepts a character from the user and
replaces all spaces in a string with that character."""

from collections import namedtuple
import not_main

print("MyModule's __name__: {0}".format(__name__))


def change_spaces(c):
    """
    Replaces all spaces in 'hello what is up' with character specified
    :param c: character
    :return: string with specified character
    """
    return 'hello what is up'.replace(' ', c)


"""
Ask the user for book details ATitle, Author, Publication Year (int) and ISBNB.
Print those details to the console using the string format method. Make sure
the book tile is capitalized properly and that the ISBN is upper case.

Now add new functionality. What if you wanted to ask the user for
multiple book details? Save each book's information as a named tuple and
have a list of named tuples representing all the different books.
"""


def book_deets():
    Book = namedtuple('Book', 'title author year isbn')
    book_list = []
    while input("Wana add book info? (y/n)") == 'y':
        book_list.append(
            Book(input("Title: ").title(), input("Author: ").title(),
                 input("Year: ").title(), input("ISBN: ").title()))
    print(book_list)


"""
Write a simple function that takes a floating point value ,the number of digits
for precision and returns the appropriately rounded floating point number.
HINT{ Check out the round function using help )
"""


def precision_maker(f, precision):
    return float(f).__round__(precision)


"""
Write a function that returns True if a string is a palindrome. AA palindrome is
a string that reads the same back-to-front as it does front-to-back). Write
some docstrings and see what gets printed when you use help(function_name)
command. NOTE  This is really simple and shouldn't require you to loop over
the string.
"""


def is_palindrome(p):
    """
    Checks if input is a palindrome.
    :param p: String to check
    :return: True if palindrome
    """
    p = str(p)
    if p[::-1] == p[::]:
        return True
    return False

def main():
    # help(is_palindrome)
    print(change_spaces('f'))
    book_deets()
    print("with pre: {0}".format(precision_maker(input("enter float: "),
                                                 int(input(
                                                     "enter precision: ")))))
    print("is 'hello' a palindrome? {0}".format(is_palindrome("hello")))
    print("is 'elle' a palindrome? {0}".format(is_palindrome("elle")))
    print("is 'ellle' a palindrome? {0}".format(is_palindrome("ellle")))


if __name__ == '__main__':
    main()
