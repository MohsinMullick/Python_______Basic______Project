# Prime Even Odd Checker
# ----------User Welcome---------
print("=" * 50)
print("        PRIME EVEN ODD CHECKER PROGRAM    ")
print("=" * 50)
print("Enter any numbers check its properties.")
print("Type 'q' or 'quit' or 'exit' to stop. ")
print("=" * 50)

# ---------Infinite Loop user for user-----------
while True:
    user_input = input("Enter a number (or 'q' to quit): ").strip().lower()#user friendly for out the menu bar
    if user_input in ['q', 'quit', 'exit']:#this condition use for out the loop
        print("\n Thank you for using the checker!GoodBye.")
        break

    try:##try use for error control
        num = int(user_input)#target main menu
    except ValueError:
        print("Please enter valid integer number!\n")
        continue

    print("\n" + "-" * 50)
    print(f"Number your entered: {num}")

    if num % 2 == 0:#this  condition use for even numbers
        print("This is even numbers")
    else:
        print("This is odd numbers")

    if num > 0:#check the positive numbers
        print("Positive Number")
    elif num < 0:#check the negative numbers
        print("Negative Number")
    else:#for 0 condition
        print("Zero Number")

    if num <= 1:#this condition use for
        print("Not a prime Number.please select greater than 1")
    else:
        is_prime = True#assume flag variable
        for i in range(2, int(num ** .5) + 1):#range start 2 and prime formula
            if num % i == 0:#check
                is_prime = False
                break


        if is_prime:
            print("Yes,its a prime number")
        else:
            print("not a prime number")

    print("-" * 50 + "\n")