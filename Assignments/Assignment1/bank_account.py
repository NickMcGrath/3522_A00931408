class BankAccount:
    """
    Contains bank account attributes including: Account Number, Account Name,
    and Balance.
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

    def balance_check(self, amount):
        """
        Checks if the amount will leave the balance positive.
        :param amount: float
        :return: bool, True if account will still be positive
        """
        return amount + self.balance >= 0

    def purchase(self, amount):
        """
        Completes a purchase by updating the balance.
        :param amount: float
        """
        self.balance += amount
