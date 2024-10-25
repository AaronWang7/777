"""
This is a simple bank account management system
"""
class BankAccount:
    def __init__(self, account_number, balance=0): #Def init
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount): #def deposit
        if amount > 0: # checking if money = 0
            self.balance += amount 
            return True
        return False

    def withdraw(self, amount): 
        if 0 < amount <= self.balance: # checking if 0 is smaller than 0
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

def create_account():
    account_number = input("Enter account number: ") # takes in user's account number
    initial_balance = float(input("Enter initial balance: "))# takes user's initial balance
    return BankAccount(account_number, initial_balance) # return account number and initial balance

def main():
    accounts = {}
    while True: # while loop
        print("\n1. Create Account") # display create account
        print("2. Deposit")# display deposit
        print("3. Withdraw") # display withdraw
        print("4. Check Balance") # display check balance
        print("5. Exit")# dislplay exit
        
        choice = input("Enter your choice (1-5): ") # the virable named chice store the user's input, 1-5.
        
        if choice == '1': # check if choice = 1
            account = create_account() # the varible account = create_account
            accounts[account.account_number] = account 
            print(f"Account {account.account_number} created successfully!")#display the number of account, and created successfully
        
        elif choice in ['2', '3', '4']: #else if choice is one of them, 2,3,4
            account_number = input("Enter account number: ")
            if account_number in accounts: #check if account number is one of 2,3,4
                account = accounts[account_number] #set account to accounts[account_number]
                if choice == '2': # check if choice is 2
                    amount = float(input("Enter deposit amount: ")) # turn it to float, use amount to store it, and ask user to enter depisit amount
                    if account.deposit(amount): # check if deposit is amount
                        print(f"Deposited ${amount:.2f} successfully!") # display deposited amount with 2 decimal places, and successfully
                    else: # if not, else
                        print("Invalid deposit amount.")# display Invalis deposit amount
                elif choice == '3': # else if choice is 3
                    amount = float(input("Enter withdrawal amount: ")) # set amount to float and ask user to enter a Withdrawal amount
                    if account.withdraw(amount): # check if account have the amount of money
                        print(f"Withdrawn ${amount:.2f} successfully!") # print "Withdrawn $money with 2 decimal places successfully!"
                    else: # if not, else
                        print("Invalid withdrawal amount or insufficient funds.")# display Invalid withdrawal amount or insufficient funds.
                else: # if not, else
                    print(f"Current balance: ${account.get_balance():.2f}") #display Current balance and the amount of money with 2 decimal places
            else: # if not, else
                print("Account not found.") # display Account not found.
        
        elif choice == '5': # else if choice is 5
            print("Thank you for using our banking system. Goodbye!") # display Thank you for using our banking system. Goodbye!
            break # stops the loop
        
        else: # if not, else
            print("Invalid choice. Please try again.") # display Invalid choice. Please try again.

if __name__ == "__main__": # function recall
    main()