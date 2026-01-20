#Bank Interest Calculator
#-----Welcome screen-----
print("="*50)
print("     WELCOME TO BANK INTEREST CALCULATOR    ")
print("="*50)
print("Calculate simple interest, compound interest and loan emi.")
print("type 'q' 'quit' or 'exit' to stop ")
print("="*50)

#-----infinite loop use for user-------
while True:
    print("-----MAIN MENU-----")
    print("1. Simple Interest")
    print("2. Compound Interest(Yearly compounding)")
    print("3. Loan EMi Calculator(Monthly installment(")
    print("4. Quit/Exit")

#------user choice main menu-------
    choice=input("Choice an option (1 to 4): ").strip().lower()
    if choice in['4','q','quit','exit']:#user out the loop
        print("Thank you for using bank interest!Good Bye")
        break
    try:#try only use error control
        #----Simple interest------
        if choice=="1":
            principal=float(input("Enter principal amount (TK): "))
            rate=float("Enter annual interest rate(%): ")
            time=float(input("Enter time (in years): "))

            simple_interest=(principal*rate*time)/100#calcualtion
            total_amount=principal+simple_interest
            #--------users results-------
            print("\n" + "-" * 50)
            print(f"Principal Amount     : {principal:,.2f} TK")
            print(f"Interest Rate        : {rate}% per year")
            print(f"Time                 : {time} years")
            print(f"Simple Interest      : {simple_interest:,.2f} TK")
            print(f"Total Amount Payable : {total_amount:,.2f} TK")
            print("-" * 50)
        #------compound interest-------
        elif choice=="2":
            principal=float(input("Enter principal amount (TK): "))
            rate=float(input("Enter annual interest rate(%): "))
            time=float(input("Enter time(in years): "))

            amount=principal*(1+rate/100)**time
            compound_interest=amount-principal

            print("\n" + "-" * 50)
            print(f"Principal Amount     : {principal:,.2f} TK")
            print(f"Interest Rate        : {rate}% per year")
            print(f"Time                 : {time} years")
            print(f"Compound Interest    : {compound_interest:,.2f} TK")
            print(f"Total Amount         : {amount:,.2f} TK")
            print("-" * 50)
       #------loan------
        elif choice=="3":
            principal=float(input("Enter principal amount (TK): "))
            rate=float(input("Enter annual interest rate(%): "))
            tenure=float(input("Enter time(in years): "))

            monthly_rate = rate / 12 / 100
            months = tenure * 12

            emi = principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)
            total_payment = emi * months
            total_interest = total_payment - principal

            print("\n" + "-" * 50)
            print(f"Loan Amount          : {principal:,.2f} TK")
            print(f"Annual Interest Rate : {rate}%")
            print(f"Tenure               : {tenure} years ({months} months)")
            print(f"Monthly EMI          : {emi:,.2f} TK")
            print(f"Total Payment        : {total_payment:,.2f} TK")
            print(f"Total Interest       : {total_interest:,.2f} TK")
            print("-" * 50)

        else:
            print("Invalid choice! Please select 1-4.")

    except ValueError:
        print("Invalid input! Please enter numbers only.\n")
        continue

    print("-" * 50)


