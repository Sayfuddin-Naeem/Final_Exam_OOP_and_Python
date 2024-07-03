from banks import Bank
from person import User, Admin

amar_bank = Bank("Amar Bank")

def user_interface():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")
    address = input("Enter Your Address : ")
    account_type = input("Enter Account Type : ")
    
    user = User(name, email, phone, address, account_type, amar_bank)
    
    while True:
        print(f"\n\tWelcome {user.name} !!")
        print("1. Deposite Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Check Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Exit")

        choice = input("\nEnter Your Choice : ")

        if choice == '1':
            amount = int(input("\tEnter Deposite Amount : "))
            user.deposite(amount)
        elif choice == '2':
            amount = int(input("Enter Withdraw Amount : "))
            user.withdraw(amount)
        elif choice == '3':
            user.check_balance()
        elif choice == '4':
            user.check_transaction_history()
        elif choice == '5':
            amount = int(input("Enter Loan Amount : "))
            user.take_loan(amount)
        elif choice == '6':
            amount = int(input("Enter Transfer Amount : "))
            receiver = int(input("Enter Receiver Account Number : "))
            user.transfer_money(receiver, amount, amar_bank)
        elif choice == '7':
            break
        else:
            print("\n\tInvalid Input")
    

def admin_interface():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")
    address = input("Enter Your Address : ")

    admin = Admin(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"\n\tWelcome {admin.name} !!")
        print("1. Delete User")
        print("2. Show All User")
        print("3. Check Total Balance of the Bank")
        print("4. Check Total Loan Balance of the Bank")
        print("5. On Loan feature of the Bank")
        print("6. Off Loan feature of the Bank")
        print("7. Exit")

        choice = input("\nEnter Your Choice : ")

        if choice == '1':
            account_number = int(input("Enter Account Number : "))
            admin.remove_user_account(amar_bank, account_number)

        elif choice == '2':
            admin.view_all_user(amar_bank)
        elif choice == '3':
            admin.view_total_balance(amar_bank)
        elif choice == '4':
            admin.view_total_loan_amount(amar_bank)
        elif choice == '5':
            admin.loan_feature_on(amar_bank)
        elif choice == '6':
            admin.loan_feature_off(amar_bank)
        elif choice == '7':
            break
        else:
            print("\n\tInvalid Input")


while True:
    print(f"\n\t\tWelcome to  {amar_bank.name}!!\n")
    print("\t1. User")
    print("\t2. Admin")
    print("\t3. Exit")
    
    choice = input("\nEnter Your Choice : ")
    
    if choice == '1':
        user_interface()
    elif choice == '2':
        admin_interface()
    elif choice == '3':
        break
    else:
        print("\n\tInvalid Input")