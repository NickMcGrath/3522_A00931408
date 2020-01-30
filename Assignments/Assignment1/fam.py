from bank_account import BankAccount
from user import *
from moderator import Moderator
from datetime import date
from budget import Budget
from budget_types import BudgetTypes


class Fam():
    """
    FAM helps with personal finances by keeping track of categories of
    spending. Fam uses a text based interface.
    """

    def __init__(self):
        """
        Initialize a Fam with a empty moderator.
        """
        self.moderator = None

    def main_menu(self):
        """
        Display a main menu and deal with user input.
        """
        option = -1
        while (option != 0):
            print('Welcome to the Main Menu!')
            print('----< F-A-M Accounting  >---- ')
            print('Enter a option:')
            print('0: Exit')
            print('1: View Budgets')
            print('2: Record a transaction')
            print('3: View Transactions by Budget')
            print('4: View Bank Account Details')

            option = int(input())
            if option == 1:
                pass
            elif option == 2:
                self.record_transaction_menu()
            elif option == 3:
                pass
            elif option == 4:
                pass
        print('Thanks for using Dank Accounting')

    def record_transaction_menu(self):
        """
        Display options for a transaction and deal with user input.
        """
        self.moderator.notification_check()
        print('Enter a Transaction type:')
        print('1: Games and Entertainment')
        print('2: Clothing and Accessories')
        print('3: Eating Out')
        print('4: Miscellaneous')
        option = int(input())
        while (option != 0):
            amount = float(input('How many Bones? +/-:'))
            if option == 1:
                print(self.moderator.transaction(amount,
                                                 BudgetTypes.GAMES_AND_ENTERTAINMENT))
                break
            elif option == 2:
                print(self.moderator.transaction(amount,
                                                 BudgetTypes.CLOTHING_AND_ACCESSORIES))
                break
            elif option == 3:
                print(self.moderator.transaction(amount,
                                                 BudgetTypes.EATING_OUT))
                break
            elif option == 4:
                print(self.moderator.transaction(amount,
                                                 BudgetTypes.MISCELLANEOUS))
                break

            option = int(input())

    def load_test_user(self):
        """
        Creates a test user with budgets and a moderator to deal with the user.
        Applies moderator to instance variable.
        """
        ba = BankAccount("Account number here", "Bank name there", 99)
        user = User("Nick McGrath", date(1996, 4, 9), ba)
        self.moderator = Moderator(user)
        budget_dic = {}
        budget_dic[BudgetTypes.GAMES_AND_ENTERTAINMENT] = Budget(100)
        budget_dic[BudgetTypes.MISCELLANEOUS] = Budget(100)
        budget_dic[BudgetTypes.EATING_OUT] = Budget(100)
        budget_dic[BudgetTypes.CLOTHING_AND_ACCESSORIES] = Budget(100)
        self.moderator.set_budget_dic(budget_dic)


def main():
    """
    Program Driver.
    """
    driver = Fam()
    driver.load_test_user()
    driver.main_menu()


if __name__ == "__main__":
    main()
