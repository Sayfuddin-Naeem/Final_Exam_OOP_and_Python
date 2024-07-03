from abc import ABC, abstractmethod
import random
from datetime import datetime, date

class Person(ABC):
    def __init__(self, name, email, phone, address) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class User(Person):
    used_account_number = set() # To track which account numbers are used
    def __init__(self, name, email, phone, address, account_type, bank) -> None:
        super().__init__(name, email, phone, address)
        self.account_type = account_type
        self.balance = 0
        self.account_number = self.generate_account_number()
        self.transaction_history = []
        self.loan_count = 0
        self.bank = bank
        self.bank.add_user(self)
    
    @staticmethod
    def generate_account_number():
        while True:
            account_number = random.randint(100000, 999999)
            if account_number not in User.used_account_number:
                User.used_account_number.add(account_number)
                return account_number
    
    def view_account_number(self):
        print(f"\n\tAccount Number : {self.account_number}")
    
    def deposite(self, amount):
        self.balance += amount
        self.bank.total_balance += amount
        timestamp = datetime.now().strftime("%d-%m-%Y %I:%M %p")
        self.transaction_history.append(f"\t{timestamp}\n\tDeposited : {amount}")
        print(f"\n{self.transaction_history[-1]} is successful")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("\n\tWithdrawal amount exceeded")
            
        elif self.bank.total_balance < amount:
            print(f"\n\t{self.bank.name} is bankrupt !")
        else:
            self.balance -= amount
            timestamp = datetime.now().strftime("%d-%m-%Y %I:%M %p")
            self.transaction_history.append(f"\t{timestamp}\n\tWithdrew : {amount}")
            print(f"\n{self.transaction_history[-1]} is successful")
    
    def check_balance(self):
        print(f"\n\tCurrent Balance : {self.balance}")
    
    def check_transaction_history(self):
        if len(self.transaction_history) > 0:
            print("\n\t\tTransaction History")
            print("\t\t--------------------\n")
            for history in self.transaction_history:
                print(f"{history}\n")
        else:
            print("\n\tDon't have any transaction !")
    
    def take_loan(self, amount):
        if not self.bank.loan_feature_enabled:
            print("\n\tLoan feature is currently disabled !")
        elif self.bank.total_balance < amount:
            print(f"\n\t Do not have sufficient money !")
        elif self.loan_count >= 2:
            print("\n\tLoan limit reached !")
        else:
            self.balance += amount
            self.bank.total_balance -= amount
            self.loan_count += 1
            timestamp = datetime.now().strftime("%d-%m-%Y %I:%M %p")
            self.transaction_history.append(f"\t{timestamp}\n\tLoan taken : {amount}")
            self.bank.total_loan_amount += amount
            
            print(f"\n{self.transaction_history[-1]} is successful !")
    
    def transfer_money(self, receiver_account_number, amount, bank):
        receiver = bank.find_user_account(receiver_account_number)
        if not receiver:
            print("\n\tAccount does not exist !")
        elif amount > self.balance:
            print("\n\tTransfer amount exceeded !")
        elif self.bank.total_balance < amount:
            print(f"\n\t{self.bank.name} is bankrupt !")
        else:
            self.balance -= amount
            timestamp = datetime.now().strftime("%d-%m-%Y %I:%M %p")
            self.transaction_history.append(f"\t{timestamp}\n\tTransferred : {amount} to Account : {receiver_account_number}")
            receiver.balance += amount
            receiver.transaction_history.append(f"\t{timestamp}\n\tReceived : {amount} from Account : {self.account_number}")
            
            print(f"\n{self.transaction_history[-1]} is successful !")
            


class Admin(Person):
    def __init__(self, name, email, phone, address) -> None:
        super().__init__(name, email, phone, address)
    
    def view_all_user(self, bank):
        bank.view_all_user()
    
    def view_total_balance(self, bank):
        print(f"Total available balance: {bank.total_balance}")
        
    def view_total_loan_amount(self, bank):
        print(f"Total loan amount: {bank.total_loan_amount}")
    
    def loan_feature_on(self, bank):
        bank.loan_feature_enabled = True
        print("\n\tLoan Feature On successfully !")
        
    def loan_feature_off(self, bank):
        bank.loan_feature_enabled = False
        print("\n\tLoan Feature Off successfully !")
    
    def remove_user_account(self, bank, account_number):
        bank.remove_user_account(account_number)