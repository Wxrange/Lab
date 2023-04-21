
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
        :return: if deposit was successful it returns True or if not False
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance = self.__account_balance + amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        withdraw method takes the amount the person wants out of their account
        :param amount: is the amount of currency the person wants to take out of their account.
        :return: withdrawal being successful returns True or if not then False
        """
        if self.__account_balance < amount or amount <= 0:
            return False
        else:
            self.__account_balance = self.__account_balance - amount
            return True

    def get_balance(self) -> float:
        """
        get_balance gives the current amount of balance the account has
        :return: returns value of balance for the acoount
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        get_name gets the name of the account holder
        :return: returns the name given for the account
        """
        return self.__account_name

