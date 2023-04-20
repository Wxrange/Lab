# testing
# testing 2
import pytest
from account import *
class test:
    def setup_account(self):
        self.account_one = Account("John")
        self.account_two = Account("John", 1)
    def teardown_account(self):
        del self.account_one
        del self.account_two
    def test_deposit(self):
        assert self.account_one.deposit(1) == True
        assert self.account_one.deposit(-1) == False
        assert self.account_one.deposit(1.0) == True
        assert self.account_one.deposit(0) == False
        assert self.account_one.deposit('t') == TypeError
        assert self.account_two.deposit(1) == True
        assert self.account_two.deposit(-1) == False
        assert self.account_two.deposit(1.0) == True
        assert self.account_two.deposit(0) == False
        assert self.account_two.deposit('t') == TypeError
    def test_withdraw(self):
        assert self.account_one.withdraw(1) == True
        assert self.account_one.deposit(-1) == False
        assert self.account_one.deposit(1.0) == True
        assert self.account_one.deposit(0) == False
        assert self.account_one.deposit('t') == TypeError
        assert self.account_two.withdraw(1) == True
        assert self.account_two.deposit(-1) == False
        assert self.account_two.deposit(1.0) == True
        assert self.account_two.deposit(0) == False
        assert self.account_two.deposit('t') == TypeError





