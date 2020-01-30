class Transaction:
    """
    Transaction models a basic transaction with date and amount
    """
    def __init__(self, date, amount):
        """
        Initialize a Transaction.
        :param date: datetime, date of transaction
        :param amount: float
        """
        self.date = date
        self.amount = amount
