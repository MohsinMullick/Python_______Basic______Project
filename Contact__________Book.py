#Contact Book
contacts={}#All content store like: key=book,value=phone number
print("="*50)#arrange
print("        Welcome to Contact Book     ")
print("="*50)
print("Manage your contacts easily!")
print("Type 'quit' or 'exit' to stop anytime.")
print("="*60 +'\n')


while True:#use for infinite loop until we create break and use this loop for menu
    #user choice this menu
    print("\n-----MENU-----")
    print("1. Add new contact")
    print("2. View all contact")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")


    choice=input("Choice input(1-6) ").strip()#user choice to option and .strip() control space

    if choice in ["6", 'quit' , 'exit']:#if user 6 or quit or exit then out of function
        print("\nThank you for using contact book.Good bye.")

    elif choice=='1':#choice option 1
        name=input("Enter contact name: ").strip().title()#user input .strip check space and .title first letter capital
        if name in contacts:#check previously exit or not
            print(f"\n {name} already exits!")
        else:
            phone=input("Enter phone number.").strip()
            contacts[name]=phone
            print(f"\n {name} added successful")#if previously same name book not exit then added successful with phonenumber

    elif choice=='2':
        if not contacts:
            print("\nNo contact save yet.")
        else:
            print("="*50 +"\n")
            print("              All Contacts        ")
            print("="*50)
            for i,(name,phone) in enumerate(contacts.items(),1):
                print(f"{i}.{name}.{phone}")
                print("="*50)
    elif choice=="3":
        search_name=input("Enter name to search: ").strip().title()
        if search_name in contacts:#search same name book
            print(f"\n Found {search_name} to {contacts[search_name]}")
        else:
            print(f"\n No contact found with name {search_name}")

    elif choice == "4":
        name = input("Enter name to update: ").strip().title()
        if name in contacts:
            new_phone = input("Enter new phone number: ").strip()#update contact numbers
            contacts[name] = new_phone
            print(f"\n{name}'s phone updated to {new_phone}")
        else:
            print(f"\nNo contact found with name '{name}'")

    elif choice == "5":
        name = input("Enter name to delete: ").strip().title()
        if name in contacts:#use del function for remove the number
            del contacts[name]
            print(f"\n{name} has been deleted successfully!")
        else:
            print(f"\nNo contact found with name '{name}'")

    else:
        print("\nInvalid choice! Please select 1-6.")

    print("-" * 50)
