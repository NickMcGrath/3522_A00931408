class BankAccount:
    """
    Contains bank account attributes.
    """

    def __init__(self, account_num, account_name, balance):
        """
        Initializes a Bank Account with Account Number, Account Name,
        and Balance.
        :param account_num: string
        :param account_name: string
        :param balance: float
        """
        self.account_num = account_num
        self.account_name = account_name
        self.balance = balance

    def __str__(self):
        """returns bank account information."""
        return f'Account Name: {self.account_name}, Account Number:' \
               f' {self.account_num}, Balance: {self.balance}'


class Transaction:
    """
    Transaction models a basic transaction with date, amount, shop,
    and current balance.
    """

    def __init__(self, date, amount, shop, balance):
        """
        Initialize a Transaction.
        :param date: datetime, date of transaction
        :param amount: float
        :param shop: String, the name of the shop
        :param balance: float, the current balance at the time of the
        transaction
        """
        self.date = date
        self.amount = amount
        self.shop = shop
        self.balance = balance

    def __str__(self):
        """Returns Transaction information."""
        return f'Date: {self.date.strftime("%c")}, Budget balance:' \
               f' {self.balance}, ' \
               f'Amount: {self.amount}, Shop:' \
               f' {self.shop}'
