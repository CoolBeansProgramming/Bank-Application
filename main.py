# User parent class 
class User():
    def __init__(self, name: str, age: int):
        #assert isinstance(age,int), f"Please enter a whole number for age"
        
        self.name = name
        self.age = age
        
    def show_user_details(self):
        return f"User Details:\n Name: {self.name.title()}\n Age: {self.age}"
       

# Account child class
class Account(User):
    total_deposits = 0
    total_withdrawals = 0
    
    def __init__(self, name: str, age: int, balance):
        super().__init__(
            name, age
        )
        self.balance = balance 
        
    def deposit(self):
        deposit_amount = float(input(f"{self.name.title()} Please enter how much you would like to deposit: "))
        self.balance += deposit_amount 
        self.total_deposits += 1
        print(f"Deposit Amount: $ {round(deposit_amount,2)}")
        return f"Current Balance: $ {round(self.balance,2)}"
        
        
    def withdraw(self):
        withdrawal_amount = float(input(f"{self.name.title()}, please enter the amount you would like to withdraw: "))
        if withdrawal_amount > self.balance:
            return f"Insufficient Funds | Available Balance: $ {round(self.balance,2)}"
        else:
            self.balance -= withdrawal_amount
            self.total_withdrawals += 1
            print(f"Withdraw: $ {round(withdrawal_amount,2)}")
            return f"Current Balance: $ {round(self.balance,2)}"
            
    def view_balance(self):
        return f"Current Balance: $ {self.balance}"
    
def menu_option(user_two):
    print("Here is a list of options: ")
    
    while True:
        menu_option = int(input(" 1) Check Balance\n 2) Withdraw\n 3) Deposit\n 4) See Total Withdrawals\n 5) See Total Deposits\n 6) Quit\n"))
        if menu_option == 1:
            print(user_one_bank.view_balance())
            if menu_option == 1 and user_two != None:
                print(user_two_bank.view_balance())
        elif menu_option == 2:
            print(user_one_bank.withdraw())
            if menu_option == 2 and user_two != None:
                wd = input(f"{user_two.name} Would you like to withdraw?: Yes or No ")
                if wd.lower() == 'yes':
                    print(user_two_bank.withdraw())
        elif menu_option == 3:
            print(user_one_bank.deposit())
            if menu_option == 3 and user_two != None:
                dep = input(f"{user_two.name} Would you like to make a deposit? Yes or No ")
                if dep.lower() == 'yes':
                    print(user_two_bank.deposit())
        elif menu_option == 4:
            print(f"There have been {user_one_bank.total_withdrawals} withdrawals") 
            if menu_option == 4 and user_two != None:
                print(f"There have been {user_two_bank.total_withdrawals} withdrawals")
        elif menu_option == 5:
            print(f"There have been {user_one_bank.total_deposits} deposits")
            if menu_option == 5 and user_two != None:
                print(f"There have been {user_two_bank.total_deposits} deposits")
        elif menu_option == 6:
            print("Thank you for choosing Lambda Bank.") 
            return False
            break 
        else:
            print("Please choose a number from 1-6")
            
def bank_creation(name):
    balance = float(input(f"{name.name.title()}, how much money do you have? "))
    return balance 

while True:
    print("Welcome to Lambda Bank!")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    user_one = User(name,age)
    user_two = None
    new_user = input("Would you like to register a new person? Type 'No' to create your bank account. ")
    if new_user.lower() == 'yes':
        name = input("Enter the second person's name: ")
        age = int(input("Enter the second person's age: "))
        user_two = User(name, age)
        print("Please create your accounts.")
        user_one_balance = bank_creation(user_one)
        user_two_balance = bank_creation(user_two)
        user_one_bank = Account(user_one.name, user_one.age, user_one_balance)
        user_two_bank = Account(user_two.name, user_two.age, user_two_balance)
        flag = menu_option(user_two)
        if flag == False:
            break
    else: 
        user_one_balance = bank_creation(user_one)
        user_one_bank = Account(user_one.name, user_one.age, user_one_balance)
        flag = menu_option(user_two)
        if flag == False:
            break 
            
