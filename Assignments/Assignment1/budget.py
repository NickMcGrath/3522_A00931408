from bank_account import Transaction
from datetime import datetime

import enum


class BudgetTypes(enum.Enum):
    """Enum of Budget Types."""
    GAMES_AND_ENTERTAINMENT = 1
    CLOTHING_AND_ACCESSORIES = 2
    EATING_OUT = 3
    MISCELLANEOUS = 4

    def __str__(self):
        """Returns budget types in title case without underscores."""
        return self.name.title().replace('_', ' ')


class Budget:
    """
    Models a Budget with transactions in the budget category.
    """

    def __init__(self, balance):
        """
        Initializes a Budget with the balance of the budget.
        :param balance: float
        """
        self.total = balance
        self.balance = balance
        self.transactions = []
        self.locked = False

    def add_transaction(self, amount, shop, date_time=datetime.today()):
        """
        Adds a transaction to the budget.
        :param amount: float
        :param date_time: datetime
        :return: bool, if transaction was added
        """
        self.balance += amount
        self.transactions.append(Transaction(date_time, amount, shop,
                                             self.balance))

    def __str__(self):
        return f'Amount Spent: {self.total - self.balance}, Balance: ' \
               f'{self.balance}, Total allocated: {self.total}, ' \
               f'locked: {self.locked}'
