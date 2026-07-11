from bank_accounts import *

John = BankAccount("0639064993","John Doe", 1000)
Oladele = BankAccount("7025005130", "Oladele", 2000)

John.deposit(1000)

John.withdraw(4000)
John.transfer(10000, Oladele)

Jim = InterestRewardsAcct("04498837843", "Jim", 7000)

Jim.get_balance()

Jim.deposit(4000)

Jim.transfer(200, John)

Blaze = SavingsAccount("00003483930", "Blaze", 2000)

Blaze.get_balance()

Blaze.transfer(500, Jim)