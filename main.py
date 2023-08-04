import accounts
import datetime

def save_transaction(account_id,transaction):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("transaction_history.txt",'a') as file:
        file.write(f"{timestamp} account:  {account_id}   transaction:  {transaction}\n")

bank=accounts.Bank()

account1 = bank.create_account("123456",initial_blance=200, account_holder="Alice",account_type= "savings")
account2 = bank.create_account("789012", initial_blance=200,account_holder="Bob")
account3 = bank.create_account("33752088",initial_blance=200,account_holder="mohamed muhudin",account_type="savings")


while True:
    account_id = input("Enter your account number (or 'exit' to quit): ")
    if account_id.lower() == "exit":
        break
    account = bank.get_account(account_id)
    if account:
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                amount = float(input("Enter the amount to deposit: "))
                transaction = account.deposit(amount)
                print(transaction)
                save_transaction(account_id, transaction)
            elif choice == 2:
                amount = float(input("Enter the amount to withdraw: "))
                transaction = account.with_drawal(amount)
                print(transaction)
                save_transaction(account_id, transaction)
            elif choice == 3:
                balance = account.check_balance()
                print(f"Your balance: ${balance}")
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Account not found. Please enter a valid account number.")