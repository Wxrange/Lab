# testing
# testing 2

from account import *
from pytest import *
class Test:
    def setup_method(self):
        self.account_one = Account("John")
        self.account_two = Account("Jane", 1)
    def teardown_method(self):
        del self.account_one
        del self.account_two
    def test_init(self):
        assert self.account_one.get_name() == "John"
        assert self.account_one.get_balance() == 0

        assert self.account_two.get_name() == "Jane"
        assert self.account_two.get_balance() == 1
    def test_deposit(self):
        assert self.account_one.deposit(1) == True
        # account balance check
        assert self.account_one.get_balance() == 1

        assert self.account_one.deposit(-1) == False
        # account balance check
        assert self.account_one.get_balance() == 1

        assert self.account_one.deposit(1.5) == True
        # account balance check
        assert self.account_one.get_balance() == 2.5

        assert self.account_one.deposit(0) == False
        # account balance check
        assert self.account_one.get_balance() == 2.5

        assert self.account_two.deposit(1) == True
        # account balance check
        assert self.account_two.get_balance() == 2

        assert self.account_two.deposit(-1) == False
        # account balance check
        assert self.account_two.get_balance() == 2

        assert self.account_two.deposit(1.0) == True
        # account balance check
        assert self.account_two.get_balance() == 3

        assert self.account_two.deposit(0) == False
        # account balance check
        assert self.account_two.get_balance() == 3



    def test_withdraw(self):
        assert self.account_one.deposit(1) == True
        assert self.account_one.withdraw(1) == True
        # account balance check
        assert self.account_one.get_balance() == 0

        assert self.account_one.deposit(1) == True
        assert self.account_one.withdraw(-1) == False
        # account balance check
        assert self.account_one.get_balance() == 1

        assert self.account_one.deposit(1) == True
        assert self.account_one.withdraw(1.0) == True
        # account balance check
        assert self.account_one.get_balance() == 1

        assert self.account_one.deposit(1) == True
        assert self.account_one.withdraw(0) == False
        # account balance check
        assert self.account_one.get_balance() == 2

        # starts with 1
        assert self.account_two.deposit(1) == True
        assert self.account_two.withdraw(1) == True
        # account balance check
        assert self.account_two.get_balance() == 1

        assert self.account_two.deposit(1) == True
        assert self.account_two.withdraw(-1) == False
        # account balance check
        assert self.account_two.get_balance() == 2

        assert self.account_two.deposit(1) == True
        assert self.account_two.withdraw(1.0) == True
        # account balance check
        assert self.account_two.get_balance() == 2

        assert self.account_two.deposit(1) == True
        assert self.account_two.withdraw(0) == False
        # account balance check
        assert self.account_two.get_balance() == 3






