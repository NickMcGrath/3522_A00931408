from user import User
from budget_types import BudgetTypes


class Moderator:
    """
    Moderator deals with requested user transactions and functions
    related to account management
    """

    def __init__(self, user):
        """
        Initialize a Moderator with a user
        :param user: User
        """
        self.user = user

    def notification_check(self):
        self.user.notify()

    def set_budget_dic(self, budget_list):
        self.user.budgets = budget_list

    def transaction(self, amount, type):
        """
        Attempt a transaction.
        :param amount: float, negative if withdraw
        :param type BudgetType
        :return: string, Transaction response
        """
        if self.user.trans_check(amount, type):
            self.user.budgets[type].add_transaction(amount)
            return 'Transaction Success'
        return 'Transaction Failed :O'
