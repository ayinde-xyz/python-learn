class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        print(f"Account created for {self.account_holder} with account number {self.account_number} and initial balance of {self.balance}")

    def get_balance(self):
        print(f"Current balance for {self.account_holder} is {self.balance}")
    

    def deposit(self, amount):
            self.balance += amount
            self.get_balance()
           
    
    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"Sorry, {self.account_holder}, the {amount} wey you wan withdraw is too much. Try dey reason now. You only have {self.balance} ")

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print(f"Jaiye lo my guy, you don withdraw")
            self.get_balance()
        except BalanceException as error:
            print(f"Withdraw interrupted {error}")

    def transfer(self, amount, account):
        try: 
            print('\n**********\n\nBeginning Transfer.. 🚀')
            self.viable_transaction(amount) 
            self.withdraw(amount) 
            account.deposit(amount) 
            print('\nTransfer complete! ✅\n\n**********')
        except BalanceException as error: 
            print(f'\nTransfer interrupted. ❌ {error}')

   

    def __str__(self):
        return f"Account Number: {self.account_number}, Holder: {self.account_holder}, Balance: {self.balance}"
    


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance += (amount * 1.05)
        print("Deposit Complete")
        self.get_balance()


class SavingsAccount(InterestRewardsAcct):
    def __init__(self, account_number, account_holder, balance):
        super().__init__(account_number, account_holder, balance)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("Withdrawal completed")
            self.get_balance()
        except BalanceException as error:
            print(f"Withdrawal interrupted {error}")

        

    # def get_balance(self):
    #     print(f"\nAccount '{self.account_holder}' balance = ${self.balance:.2f}")

    # def deposit(self, amount):
    #     self.balance = self.balance + amount
    #     print("\nDeposit complete.")
    #     self.get_balance()

    # def viable_transaction(self, amount):
    #     if self.balance >= amount:
    #         return
    #     else:
    #         raise BalanceException(
    #             f"\nSorry, account '{self.account_holder}' only has a balance of ${self.balance:.2f}"
    #         )

    # def withdraw(self, amount):
    #     try:
    #         self.viable_transaction(amount)
    #         self.balance = self.balance - amount
    #         print("\nWithdraw complete.")
    #         self.get_balance()
    #     except BalanceException as error:
    #         print(f'\nWithdraw interrupted: {error}')
