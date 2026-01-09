expenses=[]#create list and all dictionary element include like amount,category
print("="*50)#jsut formal represent  below some lines
print(" Welcome to Expense Tracker ")
print("="*50)
print("Track your dail expense easily!")
print("Type 'quit' or 'exit' to stop anytime! ")
print("="*50+ '\n')


while True:#this condition maintain infinite loop until we did not break because expense all element (menu) present
   #all menu print this loop maintain
    print("__________Menu__________")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Expense")
    print("4. Exit")


    choice=input("Choice an option (1 to 4): ").lower()#user input and lower maintain function maintain text a and A both are equal

    if choice == 'quit' or choice == 'exit':#just for exit then out the loop
        print("\nThank you for using expense tracker!Stay financially smart.")
        break


    if choice=='1':
        try:#enclose because if anyone text then not show error
            amount=float(input("Enter Amount: "))
            category=input("Enter Category (Food/Transport/Entertainment): ").capitalize()
            expenses.append({"amount":amount,"category":category})
            print(f"\n Add amount {amount} in taka {category} category")
        except ValueError:
            print("Please enter valid number for amount")

    elif choice =="2":#show the cost
        if len(expenses)==0:
            print("\n No expenses recorded yet.")
        else:
            print("\n" + "=" * 50)
            print("           ALL EXPENSES           ")
            print("=" * 50)

            for i, exp in enumerate(expenses, 1):
                print(f"{i}. {exp['amount']} Taka - {exp['category']}")
            print("=" * 50)


    elif choice == "3":#all cost added
        total = sum(exp["amount"] for exp in expenses)
        print("\n" + "=" * 50)
        print(f"     TOTAL EXPENSE: {total} Taka     ")
        print("=" * 50)

    else:#if menu q to 4 did not follow then this message show
        print("Invalid choice! Please select 1-4.")
    print("\n" + "-" * 50)




