# 7.Develop a class BankAccount that supports these methods:
# a). init(): Initializes the bank account balance to the value of the 
# input argument, or to 0 if no input argument is given.
# b). withdraw(): Takes an amount as input and withdraws it from the 
# balance.
# c). deposit(): Takes an amount as input and adds it to the balance.
# d). balance(): Returns the balance on the account

class BankAccount:
    def __init__(self,balance=0):
        self.balances=balance
    def withdra(self,amount):
        if(self.balances>=amount):
            self.balances-=amount
            print("{}amount withdrawed successfully".format(amount))
        else :
            print("not enough amount")
    def deposite(self,amount):
        self.balances+=amount
        print("{}amount deposite successfully".format(amount))
    def balance(self):
        print("balance on the account is:{}".format(self.balances))
        

account=BankAccount(int(input("Initial amount of bank:\n")))
loop_runner=True

while loop_runner:
    print("Bank account")
    print("1)withdraw \n2)deposite \n3)balance \n4)exit\n")
    option=int(input("Enter the choice:\n"))
    if option==1:
        account.withdra(int(input("enter the withdraw amount:\n")))
    elif option==2:
        account.deposite(int(input("Enter the deposite amount:\n")))
    elif option==3:
        account.balance()
    else :
        loop_runner=False
        
    