class Bank():

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance < amount:
            print("Balance too low")
        else:
            self.balance -= amount
            print("new balance: {0}".format(self.balance))

    def withdraw2(self, amount):
        if balance < amount:
            pass

            