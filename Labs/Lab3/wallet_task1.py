from datetime import date

"""
This module creates a Wallet and adds Cards to the Wallet.
"""


class Person:
    """
    A Person class that models a person with a name and a date of birth.
    """

    def __init__(self, name, date_of_birth):
        """
        Initialize a person with a name and date of birth.
        :param name: a string
        :param date_of_birth: a date
        """
        self._name = name
        self._date_of_birth = date_of_birth

    def __str__(self):
        """Overridden to print person attributes. """
        return f'Name: {self._name}, date of birth: {self._date_of_birth}'


class Wallet:
    """
    A Wallet class that represents a wallet with a owner and dictionary
    of cards.
    """

    def __init__(self, owner):
        """
        Initialize a wallet with a owner.
        :param owner: a Person
        """
        self._cards = {}
        self._owner = owner

    def remove(self, id_num):
        """
        Remove and return the card if the id matches.
        :param id_num: a string
        :return: a card
        """
        card = self._cards[id_num]
        if card is not None:
            del self._cards[id_num]
        return card

    def search(self, id_num):
        """
        Search for a card with id passed in as a parameter.
        :param id_num: a string
        :return: a Card or None
        """
        if id_num in self._cards:
            return self._cards[id_num]
        return None

    def add(self, card):
        """
        Add a Card to the wallet.
        :param card: a Card
        """
        if card not in self._cards:
            self._cards[card.id_number] = card

    def __str__(self):
        """Overridden to print wallet attributes. """

        return f'Owner: {self._owner}, cards {self._cards}'


class Card:
    """
    A Card class that models a generic card with name, expiry, and id.
    """

    def __init__(self, name, expiry_date, id_number):
        """
        Initialize a Card with a name, expiry date, and id.
        :param name: a string
        :param expiry_date: a date
        :param id_number: a string
        """
        self._name = name
        self._expiry_date = expiry_date
        self._id_number = id_number

    def access_card(self):
        """
        Checks if card can be accessed.
        :return: a bool
        """
        return self._expiry_date < date.today()

    def get_id_number(self):
        """
        Get the id number.
        :return: a string
        """
        return self._id_number

    def __str__(self):
        """Overridden to print person attributes. """
        return f'Name: {self._name}, expiry date {self._expiry_date}, ' \
               f'id number: {self._id_number}'

    id_number = property(get_id_number)


def main():
    """
    Creates a Wallet and tests functions of the wallet.
    """
    p1 = Person('big bub', date(1996, 4, 9))
    w1 = Wallet(p1)

    c1 = Card('Black card', date(2020, 1, 1), 'ARD12345')
    c2 = Card('Yellow card', date(2020, 1, 1), 'ARD54321')
    print(c1, c2)
    w1.add(c1)
    w1.add(c2)

    print(w1)
    print(w1.search('ARD12345'))
    print(w1.remove('ARD12345'))
    print(w1.search('ARD12345'))
    print(w1.search('ARD54321').access_card())


if __name__ == '__main__':
    main()
