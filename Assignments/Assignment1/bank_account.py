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
