from budget import Budget


class User:
    """
    User models a user of FAM software.
    """

    def __init__(self, name, dob, bank_account):
        """
        Initialize a User.
        :param name: string
        :param dob: date
        :param bank_account: BankAccount
        """
        self.name = name
        self.dob = dob
        self.bank_account = bank_account
        self.budgets = {}

    def notify(self):
        """Example notify method to be extened and customly impemented"""
        print('bro, i am being notified, that you have a notification')

    def trans_check(self, amount, type):
        """Example of a transaction check, will be replaced by a abstract
        method!"""
        print('Doing a Transaction test in user')

        """Example check"""
        if self.budgets[type].balance + amount >= 0:
            return True
        return False
