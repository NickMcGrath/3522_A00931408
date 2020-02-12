from datetime import date

from bank_account import BankAccount
from budget import Budget, BudgetTypes
from user import User, UserTypes #, UserAngel #, TroubleMaker, Rebel


class Moderator:
    """
    Moderator deals with requested user transactions and functions
    related to account management.
    """

    def __init__(self):
        """
        Initialize a Moderator.
        """
        self.user = None  # load with load_user or load_test_user
        self.budgets = {}

    def load_user(self):
        """
        Prompt user for information needed to create a user then create and
        set budgets.
        """
        while True:
            try:
                print('Welcome! Please create a user!')

                # collect the info needed to create a User
                user_values = []
                user_values.append(input('Name: '));
                print('Date of birth (using integer values):')
                user_values.append(date(int(input('\tYear: ')), int(input(
                    '\tMonth: ')), int(input('\tDay: '))))
                bank_values = []
                bank_values.append(input('Bank Account number: '))
                bank_values.append(input('Bank Name: '))
                bank_values.append(float(input('Bank Balance: ')))
                ba = BankAccount(*bank_values)
                user_values.append(ba)
                print('Type of account?')
                print('Angel')
                print('Trouble Maker')
                print('Rebel')
                user_type = UserTypes[input('Account type: ').replace(' ',
                                                                      '_').upper()].value
                # create and set the user in the moderator
                self.user = User(*user_values, **user_type)

                # set the budget dictionary in the user
                self.budgets[BudgetTypes.GAMES_AND_ENTERTAINMENT] = Budget(int(
                    input(
                        'Budget for Games and Entertainment: ')))
                self.budgets[BudgetTypes.MISCELLANEOUS] = Budget(
                    int(input('Budget for Miscellaneous: ')))
                self.budgets[BudgetTypes.EATING_OUT] = Budget(int(input('Budget for '
                                                                        'Eating out: ')))
                self.budgets[BudgetTypes.CLOTHING_AND_ACCESSORIES] = Budget(int(input(
                    'Budget for Clothing and Accessories: ')))
            except ValueError:
                print('Try again :) (bad value)')
                continue

            else:
                break

    def load_test_user(self):
        """
        Creates a test user with budgets and a moderator to deal with the user.
        Applies moderator to instance variable.
        """
        ba = BankAccount("Account number here", "Bank name there", 400)
        user = User("Nick McGrath", date(1996, 4, 9), ba,
                    **UserTypes.TROUBLE_MAKER.value)
        self.user = user
        self.budgets[BudgetTypes.GAMES_AND_ENTERTAINMENT] = Budget(100)
        self.budgets[BudgetTypes.MISCELLANEOUS] = Budget(100)
        self.budgets[BudgetTypes.EATING_OUT] = Budget(100)
        self.budgets[BudgetTypes.CLOTHING_AND_ACCESSORIES] = Budget(100)

    def view_budget(self, key):
        """
        Prints the budget of a specified BudgetType.
        :param key: BudgetType
        """
        print(key)
        for trans in self.budgets[key].transactions:
            print('\t', trans)

    def view_budgets(self, keys):
        """
        Prints the budgets of a list of BudgetTypes.
        :param keys: BudgetType list
        """
        for key in keys:
            print(key)
            val = self.budgets[key]
            print('\t', val)

    def view_bank_account_details(self):
        """
        Prints users bank information and transactions.
        """
        print(self.user.bank_account)
        print('----< Transactions  >---- ')
        for budget in BudgetTypes:
            # print(budget)
            self.view_budget(budget)


    def notify(self):
        """
        Notifies user if budget is exceeded or more than 90% of a budget is
        used.
        """
        print('----< Notifications >---- ')
        for budgetKey in self.budgets.keys():
            if self.budgets[budgetKey].balance < 0:
                print('Exceeded budget in:', budgetKey)
                print(self.budgets[budgetKey])
            elif self.budgets[budgetKey].balance < self.budgets[
                budgetKey].total * self.user.notify_amount_percent:
                print(f'More than {self.user.notify_amount_percent * 100}% of'
                      f' {budgetKey} used!')
                print(self.budgets[budgetKey])

    def transaction(self, amount, type, shop):
        """
        Attempt a transaction.
        :param amount: float, negative if withdraw
        :param type BudgetType
        :return: string, Transaction response
        """
        # trans_check = self.user.bank_account.trans_check(amount)
        # # if transaction fails, return failed reason
        # if trans_check != True:
        #     return 'transaction check failed in back account'
        trans_check = self._trans_check(amount, type)
        if trans_check != True:
            return trans_check
        else:
            self.budgets[type].add_transaction(amount, shop)
            self.user.bank_account.trans(amount)
            self._trans_complete(amount, type)
            return 'Transaction Success'

    def _trans_check(self, amount, type):
        if self.budgets[type].balance < self.budgets[
            type].total * self.user.notify_amount_percent:
            print(
                f'More than {self.user.notify_amount_percent * 100}% of {type} used!')
            print(self.budgets[type])
        if self.user.locked == True:
            return 'Your account is locked BUD >:D'
        if self.budgets[type].locked == True:
            return 'Transaction Failed due to budget being locked!'
        if not self.user.bank_account.trans_check(amount):
            return 'Transaction Failed due to lack of funds!'
        return True

    def _trans_complete(self, amount, type):
        """
        Completes the transfer, Gets locked out if they exceed it by
        100%, if they exceed their budget in 2 or more categories then
        they get locked out fo there account completely.
        :param amount: float
        :param type: BudgetType
        """
        if hasattr(self.user, 'lock_budget_percent'):
            if 1 - self.user.lock_budget_percent >= \
                    self.budgets[type].balance / self.budgets[type].total:
                self.budgets[type].locked = True
        sum_acct_locked = 0
        for bud in self.budgets.values():
            if bud.locked == True:
                sum_acct_locked += 1
            if hasattr(self.user, 'lock_account_amount'):
                if sum_acct_locked >= self.user.lock_account_amount:
                    self.user.locked = True
