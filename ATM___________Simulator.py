#ATM Simulator(ow i'm exciting)
balance = 100000  # random balance
correct_pin = " "  # text pin setup user friendly
transactions = []  # list create because transactions msg store this list

#First of all we set up ATM CARD PIN
def setup_pin():  # function create
    global correct_pin  # To change the main correct_pin variable of the program from within the function
    print("Welcome! This is your first time. Please set up your PIN: ")
    while True:  # this loop use for user because of user mistake his password
        new_pin = input("Enter new 4 digit PIN: ")
        if len(new_pin) != 4 or not new_pin.isdigit():  # jsut check pin 4 digit or not and check o to 9
            print("Must be exactly 4 digit")
            continue
        confirm_pin = input("Confirm your pin: ")
        if new_pin == confirm_pin:  # jsut check the new pin 1234 and confirm pin 1234 then continue the next step
            correct_pin = new_pin
            print("\n PIN set Successful!Congratulations!!!!")
            break
        else:
            print("\n PIN Does not match...Try Again")


def check_pin():
    print("\n Please login your PIN: ")
    for attempt in range(3):  # total 3 times new password try
        pin = input("\nEnter your pin: ")
        if pin == correct_pin:
            print("\nPIN correct! Access granted!")
            return True
        else:
            remaining = 2 - attempt  # check how many times and remaining time
            print(f"\n Wrong PIN! {remaining} attempts left")
    print("\n Too many wrong attempt.Card blocked!!!!")
    return False


def show_balance():  # create function just check the balance
    print("\n" + "=" * 40)
    print("     BALANCE ENQUIRY SUCCESSFUL!     ")
    print("=" * 40)
    print("       Your available balance         ")
    print(f"             {balance} TAKA             ")
    print("=" * 40)
    print("       Thank you for using ATM!       ")
    print("=" * 40 + "\n")


def withdraw_money():
    global balance
    try:
        amount = int(input("Enter amount to withdraw (multiple of 100): "))  # input string থেকে int করা দরকার
        if amount % 100 != 0:
            print("Amount must be multiple of 100! ")
        elif amount > balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Amount must be positive.")
        else:
            balance -= amount
            transactions.append(f"Withdrawn: {amount} Taka")
            print("\n" + "="*50)
            print("         WITHDRAWAL SUCCESSFUL          ")
            print("="*50)
            print(f"   Withdrawn Amount : {amount} Taka     ")
            print(f"   Remaining Balance: {balance} Taka    ")
            print("="*50)
            print("       Please take your cash          ")
            print("       Thank you!                     ")
            print("="*50 + "\n")
    except ValueError:
        print("Invalid input!")


def deposit_money():
    global balance
    try:
        amount = int(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Amount must be positive!")
        else:
            balance += amount
            transactions.append(f"Deposited: {amount} Taka")
            print("\n" + "="*50)
            print("          DEPOSIT SUCCESSFUL            ")
            print("="*50)
            print(f"   Deposited Amount : {amount} Taka     ")
            print(f"   New Balance      : {balance} Taka    ")
            print("="*50)
            print("       Thank you for banking          ")
            print("="*50 + "\n")
    except ValueError:
        print("Invalid input!")


def change_pin():
    global correct_pin
    old_pin = input("Enter old PIN: ")
    if old_pin == correct_pin:
        new_pin = input("Enter new PIN: ")
        confirm_pin = input("Confirm new PIN: ")
        if new_pin == confirm_pin and len(new_pin) == 4 and new_pin.isdigit():
            correct_pin = new_pin
            print("\nPIN changed successfully!\n")
        else:
            print("Invalid new PIN or mismatch!")
    else:
        print("Wrong old PIN!")


def mini_statement():
    print("\n" + "="*50)
    print("          MINI STATEMENT                ")
    print("="*50)
    if len(transactions) == 0:
        print("       No transactions yet.           ")
    else:
        for txn in transactions[-5:]:
            print(f"   {txn}   ")
    print(f"   Current Balance: {balance} Taka      ")
    print("="*50 + "\n")


###### Main Program
print("----------ATM SIMULATOR---------")

if correct_pin.strip() == "":
    setup_pin()

if check_pin():
    while True:
        print("=== ATM Menu ===")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Change PIN")
        print("5. Mini Statement")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            show_balance()
        elif choice == '2':
            withdraw_money()
        elif choice == '3':
            deposit_money()
        elif choice == '4':
            change_pin()
        elif choice == '5':
            mini_statement()
        elif choice == '6':
            print("Thank you for using ATM. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")