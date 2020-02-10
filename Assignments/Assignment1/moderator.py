from datetime import date

from bank_account import BankAccount
from budget import Budget, BudgetTypes
from user import User, UserAngel, TroubleMaker, Rebel


class Moderator:
    """
    Moderator deals with requested user transactions and functions
    related to account management.
    """

    def __init__(self):
        """
        Initialize a Moderator with a user.
        :param user: User
        """
        self.user = None  # load with load_user or load_test_user
        self.budgets = {}

    def load_user(self):
        """
        Prompt user for information needed to create a user then create and
        set the user in a moderator.
        """
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
        bank_values.append(input('Bank Balance: '))
        ba = BankAccount(*bank_values)
        user_values.append(ba)
        user_values.append(self.budgets)

        # create and set the user in the moderator
        self.user = User(*user_values)

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

    def load_test_user(self):
        """
        Creates a test user with budgets and a moderator to deal with the user.
        Applies moderator to instance variable.
        """
        ba = BankAccount("Account number here", "Bank name there", 400)
        user = Rebel("Nick McGrath", date(1996, 4, 9), ba, self.budgets)
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
            print('\t',val)

    def view_bank_account_details(self):
        """
        Prints users bank information and transactions.
        """
        print(self.user.bank_account)
        print('----< Transactions  >---- ')
        for budget in BudgetTypes:
            # print(budget)
            self.view_budget(budget)

    def transaction(self, amount, type, shop):
        """
        Attempt a transaction.
        :param amount: float, negative if withdraw
        :param type BudgetType
        :return: string, Transaction response
        """
        trans_check = self.user.trans_check(amount, type)
        # if transaction fails, return failed reason
        if trans_check != True:
            return trans_check
        else:
            self.budgets[type].add_transaction(amount, shop)
            self.user.trans_complete(amount, type)
            return 'Transaction Success'

    def notify(self):
        """Notify the user to print Warnings."""
        self.user.notify()