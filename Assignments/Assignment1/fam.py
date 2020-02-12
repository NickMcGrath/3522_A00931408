from moderator import Moderator
from budget import BudgetTypes


class Fam():
    """
    FAM helps with personal finances by keeping track of categories of
    spending. Fam uses a text based interface.
    """

    def __init__(self, moderator):
        """Initialize a Fam with a moderator."""
        self.moderator = moderator

    def main_menu(self):
        """Display a main menu and deal with user input."""
        option = -1
        while (option != 0):
            self.moderator.notify()
            print('----<   Main Menu   >---- ')
            print('Enter a option:')
            print('0: Exit')
            print('1: View Budgets')
            print('2: Record a transaction')
            print('3: View Transactions by Budget')
            print('4: View Bank Account Details')
            while True:
                try:
                    option = int(input('> '))
                except ValueError:
                    print('Please enter a option (integer value)')
                    continue
                else:
                    break
            if option == 1:
                self.moderator.view_budgets(BudgetTypes)
            elif option == 2:
                self.record_transaction_menu()
            elif option == 3:
                self.transactions_by_budget_menu()
            elif option == 4:
                self.moderator.view_bank_account_details()
            elif option == 0:
                break
            else:
                print('Didnt get that, Please enter a option (integer value)')
        print('Thanks for using Dank Accounting')

    def transactions_by_budget_menu(self):
        """Displays a transaction sub menu and deals with user input."""
        while True:
            print('----<   Transaction Menu   >---- ')
            print('View all transactions in:')
            print('0: Back to main menu')
            print('1: Games and Entertainment')
            print('2: Clothing and Accessories')
            print('3: Eating Out')
            print('4: Miscellaneous')
            option = -1
            while True:
                try:
                    option = int(input('> '))
                    if option == 0:
                        return
                    self.moderator.view_budget(BudgetTypes(option))
                except ValueError:
                    print('Please enter a option (integer value)')
                    continue
                else:
                    break

    def record_transaction_menu(self):
        """Display options for a transaction and deal with user input."""
        print('----<   Record Transaction   >---- ')
        print('Enter a Transaction type:')
        print('0: Go back to main menu')
        print('1: Games and Entertainment')
        print('2: Clothing and Accessories')
        print('3: Eating Out')
        print('4: Miscellaneous')
        option = -1
        while True:
            try:
                option = int(input('> '))
                amount = float(input('How many Bones? +/-:'))
                shop = input('Shop: ')
                print(self.moderator.transaction(amount, BudgetTypes(option),
                                                 shop))
            except ValueError:
                print('Please check parameters!')
                continue
            else:
                break
        if option == 0:
            return


def main():
    """Program Driver."""
    driver = Fam(Moderator())

    driver.moderator.load_test_user()
    # driver.moderator.load_user()
    driver.main_menu()


if __name__ == "__main__":
    main()
