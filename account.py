
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
        :return: boolean if deposit was successful or not
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance = self.__account_balance + amount
            return True

    def withdraw(self, amount: float):
        """
        withdraw method takes the amount the person wants out of their account
        :param amount: is the amount of currency the person wants to take out of there account.
        :return: boolean whether the withdraw was successful or not
        """
        if self.__account_balance < amount or amount <= 0:
            return False
        else:
            self.__account_balance = self.__account_balance - amount
            return True

    def get_balance(self) -> float:
        """
        get_balance gives the current amount of balance the aaccount has
        :return: the value of balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        get_name gets the name of the account holder
        :return: string value the name given for the account
        """
        return self.__account_name

