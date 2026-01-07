#Simple Calculator CLI
print("="*50)
print("Welcome to simple calculator")
print("="*50)
print("You can do + - * /")
print("Type 'quit' or 'exit' to stop anytime. " )
print("="*50 + "\n")

while True:
    user_input = input("Do you want to calculate?(yes or no or quit): ").lower()
    if user_input in ["no","quit","exit"]:
        print("\nThank you for using calculator.Good bye.")
        break
    if user_input != "yes":
        print("Please type 'yes' or 'quit'")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operator (+ - * /): ").strip()
        print("\n" + "-" * 40)

        if op == "+":
            result = num1 + num2
            print(f"   {num1} + {num2} = {result}   ")
        elif op == "-":
            result = num1 - num2
            print(f"   {num1} - {num2} = {result}   ")
        elif op == "*":
            result = num1 * num2
            print(f"   {num1} × {num2} = {result}   ")
        elif op == "/":
            if num2 == 0:
                print("   Error! Division by zero is not allowed.   ")
            else:
                result = num1 / num2
                print(f"   {num1} ÷ {num2} = {result}   ")
        else:
            print("   Invalid operator! Please use +, -, *, /   ")

        print("-" * 40 + "\n")

    except ValueError:
        print("\nError! Please enter valid numbers.\n")