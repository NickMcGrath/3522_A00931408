import abc


class User(abc.ABC):
    """
    User models a user of FAM software. Users have transaction checks and
    notification checks.
    """

    def __init__(self, name, dob, bank_account, budgets):
        """
        Initialize a User.
        :param name: string
        :param dob: date
        :param bank_account: BankAccount
        """
        self.name = name
        self.dob = dob
        self.bank_account = bank_account
        self.budgets = budgets
        self.locked = False

    @abc.abstractmethod
    def notify(self):
        """
        Print any notifications about the current account state.
        """
        pass

    @abc.abstractmethod
    def trans_check(self, amount, type):
        """
        Check if an incoming transaction should be completed.
        :param amount: float
        :param type: BudgetType
        :return: True if good otherwise fail reason
        """
        pass

    @abc.abstractmethod
    def trans_complete(self, amount):
        pass


class UserAngel(User):
    """
    Represents a user that is trusted with there finances.
    """

    def notify(self):
        """
        Notifies user if budget is exceeded or more than 90% of a budget is
        used.
        """
        for budgetKey in self.budgets.keys():
            if self.budgets[budgetKey].balance < 0:
                print('Exceeded budget in:', budgetKey)
                print(self.budgets[budgetKey])
            elif self.budgets[budgetKey].balance < self.budgets[
                budgetKey].total * .1:
                print(f'More than 90% of {budgetKey} used!')
                print(self.budgets[budgetKey])

    def trans_check(self, amount, type):
        """
        Checks if there is enough in the bank account for the transfer.
        :param amount: float
        :param type: BudgetType
        :return: bool: True if good
        """
        if self.bank_account.balance + amount >= 0:
            return True
        return False

    def trans_complete(self, amount, type):
        """
        Completes the Transfer.
        :param amount: float
        :param type: BudgetType
        """
        self.bank_account.balance += amount


class TroubleMaker(User):
    """
    Represents a user that is somewhat trusted with there finances.
    """

    def notify(self):
        """
        Notifies user if they exceeded a budget category, and a warning if
        more than 75% of a budget is used.
        :return:
        """
        for budgetKey in self.budgets.keys():
            if self.budgets[budgetKey].balance < 0:
                print('Exceeded budget in:', budgetKey)
                print(self.budgets[budgetKey])

            elif self.budgets[budgetKey].balance < self.budgets[
                budgetKey].total * .25:
                print(f'More than 75% of {budgetKey} used!')
                print(self.budgets[budgetKey])
            if self.budgets[budgetKey].locked == True:
                print(f'{budgetKey} is Locked!')

    def trans_check(self, amount, type):
        """
        Checks if there is enough in the bank account for the transfer.
        :param amount: float
        :param type: BudgetType
        :return: bool: True if good
        """

        if self.budgets[type].locked == True:
            return 'Transaction Failed due to budget being locked!'
        if self.bank_account.balance + amount < 0:
            return 'Transaction Failed due to lack of funds!'
        return True

    def trans_complete(self, amount, type):
        """
        Completes the Transfer, gets locked out of conducting
        transaction in a budget category if they exceed it by 120%
        :param amount:
        :param type:
        :return:
        """
        self.bank_account.balance += amount
        if -(self.budgets[type].total * .2) > self.budgets[
            type].balance:
            self.budgets[type].locked = True


class Rebel(User):
    """
    Represents a user that can't be trusted with there finances.
    """

    def notify(self):
        """
        Notifies user if budget is exceeded, if transaction af
        budget is
        used.
        """
        for budgetKey in self.budgets.keys():
            if self.budgets[budgetKey].balance < self.budgets[
                budgetKey].total * .5:
                print(f'More than 50% of {budgetKey} used!')
                print(self.budgets[budgetKey])
            if self.budgets[budgetKey].balance < 0:
                print('CMON!! EXCEEDED BUDGET IN: ',
                      budgetKey)
                print(self.budgets[budgetKey])

            if self.budgets[budgetKey].locked == True:
                print(f'{budgetKey} is Locked!')

    def trans_check(self, amount, type):
        if self.budgets[type].balance < self.budgets[
            type].total * .5:
            print(f'More than 50% of {type} used!')
            print(self.budgets[type])
        if self.locked == True:
            return 'Your account is locked BUD >:D'
        if self.budgets[type].locked == True:
            return 'Transaction Failed due to budget being locked!'
        if self.bank_account.balance + amount < 0:
            return 'Transaction Failed due to lack of funds!'
        return True

    def trans_complete(self, amount, type):
        """
        Completes the transfer, Gets locked out if they exceed it by
        100%, if they exceed their budget in 2 or more categories then
        they get locked out fo there account completely.
        :param amount: float
        :param type: BudgetType
        """
        self.bank_account.balance += amount
        if 0 >= self.budgets[
            type].balance:
            self.budgets[type].locked = True
        sum_acct_locked = 0
        for bud in self.budgets.values():
            if bud.locked == True:
                sum_acct_locked += 1
            if sum_acct_locked >= 2:
                self.locked = True
