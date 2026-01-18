#Number System Converter

#----------User Welcome---------
print("="*50)
print("    WELCOME NUMBER SYSTEM CONVERTER PROGRAM     ")
print("="*50)
print("Convert Number Between Decimal, Binary, Octal, And Hex")
print("Type 'q' or 'quit' or 'exit' to stop")
print("="*50+"\n")

   #---------Infinite loop for main menu----------
while True:
    print("-----Choice Conversation Type-----")
    print("1. Decimal to binary")
    print("2. Decimal to octal")
    print("3. Decimal to hexadecimal")
    print("4. Binary to decimal")
    print("5. Octal to decimal")
    print("6. Hexadecimal to decimal")
    print("7. Quit/Exit")
    choice=input("Enter choice (1 to 7): ")#user input choice any one
    if choice in ['7','q','quit','exit']:#user friendly exit for the loop
        print("Thank you for using number system converter.GoodBye!")
        break#loop break

    try:#try use for error control
        #deciasmal to binary
        if choice=="1":
            num=int(input("Enter Decimal Number: "))#user input for decimal
            print(f"Binary: {bin(num)[2:]}")#bin function use

       #decimal to octal
        elif choice=="2":
            num=int(input("Enter Decimal Number: "))
            print(f"Octal: {oct(num)[2:].upper()}")
        #decimal to hexadecimal
        elif choice=="3":
            num=int(input("Enter Decimal Number: "))
            print(f"Hexadecimal: {hex(num)[2:]}")
        #binary to decimal
        elif choice=="4":
            binary=input("Enter Binary Number: ").strip()
            decimal=int(binary,2)
            print(f"Decimal: {decimal}")
       #octal to decimal
        elif choice=="5":
            octal=input("Enter Octal Number: ").strip()
            decimal=int(octal,2)
            print(f"Decimal: {decimal}")
        #Hexadeciaml to decimal
        elif choice=="6":
            hexa=input("Enter Hexadecimal Number: ").strip()
            decimal=int(hexa, 16)
            print(f"Hexadecimal: {decimal}")
        else:
            print("Invalid Choice Please select 1 to 7.")
    except ValueError:
        print("Invalid Value Error.Please Enter correct Number Format.")
    print("-"*50)


