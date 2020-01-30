from transaction import Transaction
from datetime import datetime


class Budget:
    """
    Models a Budget with transactions in the budget category.
    """

    def __init__(self, balance):
        """
        Initializes a Budget with the balance of the budget.
        :param balance: float
        """
        self.balance = balance
        self.transactions = []
        self.type = type

    def add_transaction(self, amount, date_time=datetime.today()):
        """
        Adds a transaction to the budget.
        :param amount: float
        :param date_time: datetime
        :return: bool, if transaction was added
        """
        if self.balance + amount >= 0:
            self.transactions.append(Transaction(date_time, amount))
            self.balance += amount
            return True
        else:
            return False
