
class Account:
    """
    The Account class is meant to preform deposits and withdraws from a users account
    """

    def __init__(self, name: str, balance=0):
        """
        Constructor is meant to assign the name and balance values to the account
        :param name: persons first name
        :param balance: persons balance
        """
        self.__account_name = name
        self.__account_balance = balance

    def deposit(self, amount: float) -> bool:
        """
        The method deposit allows the person to add money to the persons account
        :param amount: The amount of money the person wants to deposit
        :return: boolean if deposit was successful
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance = self.__account_balance + amount
            return True

    def withdraw(self, amount: float):
        if self.__account_balance < amount or amount <= 0:
            return False
        else:
            self.__account_balance = self.__account_balance - amount
            return True

    def get_balance(self) -> float:
        return self.__account_balance

    def get_name(self) -> str:
        return self.__account_name

