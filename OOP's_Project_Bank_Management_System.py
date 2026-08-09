class BankAccount:
  def __init__(self, initialAmount, acctName):
    self.balance = initialAmount
    self.name = acctName

    print(f"\nAccount '{self.name}' created. \nBalance = ${self.balance:.2f}")
  
  def getBalance(self):
    print(f"\n Account '{self.name}' balance = ${self.balance:.2f}")

  def deposit(self, amount):
    self.balance  = self.balance + amount
    print("\n Deposit Complete.")
    self.getBalance()
  
  def variableTransaction(self, amount):
    if self.balance >= amount:
      return 
    else:
      print(f"\n Sorry account '{self.name}' only has a balance of ${self.balance:.2f}")

  def withdraw(self, amount):
    try: 
      self.variableTransaction(amount)
      self.balance = self.balance - amount
      print("\nWidhdraw Complete.")
      self.getBalance()
    except:
      print(f'\nWidhdraw Interrupted:')

  def transfer(self, amount, account):
    try: 
      print(f'\n*******\n\nBegging Transfer..rocker')
      self.variableTransaction(amount)
      self.withdraw(amount)
      account.deposit(amount)
      print('\n Transfer Complete!')
    except:
      print(f'\nWidhdraw Interrupted:')
  
class InterestRewardsAcct(BankAccount):
  def deposite(self, amount):
    self.balance = self.balance + (amount * 1.05)
    print(f'\nDeposite Compete.')
    self.getBalance()

class SavingAcct(InterestRewardsAcct):
  def __init__(self, initialAmount, acctName):
    super().__init__(initialAmount, acctName)
    self.fee = 5
  
  def withdraw(self, amount):
    try: 
      self.variableTransaction(amount + self.fee)
      self.balance = self.balance - (amount + self.fee)
      print("\nWithdraw completed.")
      self.getBalance()
    except:
      print(f'\nWidhdraw Interrupted:')


Mustafa = BankAccount(1000, "Mustafa")
Raza = BankAccount(5000, "Raza")  

Mustafa.getBalance()
Raza.getBalance()

Mustafa.deposite(500)
Raza.deposit(1000)

Raza.transfer(1000, Mustafa)
Raza.transfer(10, Mustafa)
