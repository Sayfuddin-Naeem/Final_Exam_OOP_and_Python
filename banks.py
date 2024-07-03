class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.total_balance = 0
        self.total_loan_amount = 0
        self.users = []
        self.loan_feature_enabled = True
    
    def add_user(self, user):
        self.users.append(user)
    
    def view_all_user(self):
        if len(self.users) == 0:
            print("\n\tDo not have any user !")
        else:
            print("\n\t\tAll Users")
            print("\t\t----------\n")
            for user in self.users:
                print(f"User's Name: {user.name}\tAccount Number: {user.account_number}")
    
    def find_user_account(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                return user
        return None
    
    def remove_user_account(self, account_number):
        user = self.find_user_account(account_number)
        if user:
            self.users.remove(user)
            print(f"\n\tAccount Number : {account_number} is deleted !")
        else:
            print("\n\tUser not found !")
        