# Strong Password Generator
import random  # use for random password
import string  # python build in like large small character,number and special character

print("=" * 60)
print("         Welcome to Strong password Generator      ")
print("=" * 60)
print("\nThis will create a secure password for you.")
print("Type 'quit' or 'exit' to 'stop' ")
print("=" * 60 + "\n")

while True:  # just create a loop until i create break
    user_choice = input("Do you want to create password(yes/quit/no): ").lower()
    if user_choice in ['no', 'quit', 'exit']:
        print("\nThank you for using password generator.stay safe!!")
        break

    if user_choice != 'yes':
        print("\n Please type 'yes' or 'quit'\n ")
        continue

    try:
        length = int(input("Enter password length (minimum: 8) : "))
        if length < 8:
            print("Password should be at least 8 character for security.")
            continue

        all_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(all_characters) for i in range(length))

        print("\n" + "=" * 60)
        print("           YOUR GENERATED PASSWORD           ")
        print("=" * 60)
        print(f"       {password}       ")
        print("=" * 60)
        print("   Copy it now! (It's not saved anywhere)   ")
        print("   Use it and stay secure! 🔒   ")
        print("=" * 60 + "\n")

    except ValueError:
        print("\nPlease enter a valid number!\n")