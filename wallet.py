"""
Wallet app
"""

class Wallet:
    """
    Wallet class to add & spend cash
    """

    def __init__(self, initial_amount=0):
        """
        Initial amount
        """
        self.balance = initial_amount

    def spend_cash(self, amount):
        """
        Spend cash
        """
        if self.balance < amount:
            raise Exception('Not enough available to spend {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        """
        Add cash to wallet
        """
        self.balance += amount

if __name__ == "__main__":
    print("This is your wallet")
    cash_amount = input("Enter cash amount: ")