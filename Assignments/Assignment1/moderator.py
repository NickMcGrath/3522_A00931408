from datetime import date

from bank_account import BankAccount
from budget import Budget, BudgetTypes
from user import User, UserTypes


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
                user_values.append(input('Name: '))
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
                self.budgets[BudgetTypes.EATING_OUT] = Budget(
                    int(input('Budget for '
                              'Eating out: ')))
                self.budgets[BudgetTypes.CLOTHING_AND_ACCESSORIES] = Budget(
                    int(input(
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
                    **UserTypes.REBEL.value)
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
            self.view_budget(budget)

    def notify(self):
        """
        Notifies user if budget is exceeded or more than their specified
        notification amount.
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

    def transaction(self, amount, budget_type, shop):
        """
        Attempt a transaction.
        :param shop:
        :param amount: float, negative if withdraw
        :param budget_type BudgetType
        :return: string, Transaction response
        """
        trans_check = self._trans_check(amount, budget_type)
        if trans_check != True:
            return trans_check
        else:
            self.budgets[budget_type].add_transaction(amount, shop)
            self._trans_complete(amount, budget_type)
            return 'Transaction Success'

    def _trans_check(self, amount, budget_type):
        """
        Helper method to check for any transaction flags.
        :param amount: float
        :param budget_type: BudgetType
        :return: True if good otherwise reason for failure
        """
        if self.budgets[budget_type].balance < \
                self.budgets[budget_type].total \
                * self.user.notify_amount_percent:
            print(
                f'More than {self.user.notify_amount_percent * 100}% of {budget_type} used!')
            print(self.budgets[budget_type])
        if self.user.locked:
            return 'Your account is locked BUD >:D'
        if self.budgets[budget_type].locked:
            return 'Transaction Failed due to budget being locked!'
        if not self.user.bank_account.balance_check(amount):
            return 'Transaction Failed due to lack of funds!'
        return True

    def _trans_complete(self, amount, budget_type):
        """
        Completes the transfer, Gets locked out if they exceed it by
        100%, if they exceed their budget in 2 or more categories then
        they get locked out fo there account completely.
        :param amount: float
        :param budget_type: BudgetType
        """
        self.user.bank_account.purchase(amount)
        if hasattr(self.user, 'lock_budget_percent'):
            if 1 - self.user.lock_budget_percent >= \
                    self.budgets[budget_type].balance \
                    / self.budgets[budget_type].total:
                self.budgets[budget_type].locked = True
        sum_acct_locked = 0
        for budget in self.budgets.values():
            if budget.locked:
                sum_acct_locked += 1
            if hasattr(self.user, 'lock_account_amount'):
                if sum_acct_locked >= self.user.lock_account_amount:
                    self.user.locked = True
