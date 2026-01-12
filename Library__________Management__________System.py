#Library Management System cli
library={}#create empty library
#Create user welcome arrangement
print("="*50)#print 50 equal sign just for welcome
print("      Welcome To Library Management System       ")
print("="*50)
print("Manage All Books Easily!!!")
print("Type 'exit ' or 'quit' to stop anytime")
print("="*50 +"\n")

while True:#Create infinite loop because for main menu
    print("----------Main Menu----------")
    print("1. Add New Book")
    print("2. View All Books")
    print("3. Search All Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice=input("Please select (1-7):").strip()#select user from menu 1 to 7

    if choice in ['7','exit','quit']:#at first 7 control because user dissatisfied again same menu show
        print("\n Thank you for using library management system.GoodBye!!")#exit and this msg show
        break

     #Add new book
    elif choice=="1":#selectt 1
        book_id=input("Enter Unique Book ID:").strip()#book id unique
        if book_id in library:#dictionary check same book id exist or not
             print(f"\n Book {book_id} already exit.")
             continue

        title=input("Enter book title name: ").strip().title()#book title
        author=input("Enter book author name: ").strip().title()#author name

        library[book_id]={#dictionary include all
            "title":title,
            "author":author,
            "status":"available"
        }
        print(f"Book {title} by {author} added successful.ID {book_id} ")#print add book name with author and book id


   #View All Books
    elif choice=="2":
        if not library:#check the books in library present or not
            print("\n No books in library yet. ")
        else:
            print("="*50)
            print("       All Books in Library       ")
            print("="*50)
            print(f"{'ID':<10} {'title':<30} {'author':<25} {'status':<15}")#presentation like header column name and <number just position
            for book_id,info in library.items():#.items key value pair
                print(f"{book_id:<10} {info['title']: <30} {info['author']:<25} {info['status']:<15}")
                print("="*50)

          #Search all books
    elif choice=="3":
        search=input("Enter Title or Author or Book id to search: ").strip().lower()
        found=False
        print("\n Search results")
        for book_id, info in library.items():
            if (search in info['title'].lower() or
                    search in info['author'].lower() or
                    search == book_id.lower()):
                print(f"ID: {book_id} | {info['title']} by {info['author']} | Status: {info['status']}")
                found = True
        if not found:
            print("No book found matching your search.")

       #Borrow all books
    elif choice == "4":
        book_id = input("Enter Book ID to borrow: ").strip()
        if book_id in library:
            if library[book_id]["status"] == "Available":
                library[book_id]["status"] = "Borrowed"
                print(f"\nBook '{library[book_id]['title']}' borrowed successfully!")
            else:
                print("\nSorry, this book is already borrowed!")
        else:
            print(f"\nNo book found with ID {book_id}")

      #Return Books
    elif choice == "5":
        book_id = input("Enter Book ID to return: ").strip()
        if book_id in library:
            if library[book_id]["status"] == "Borrowed":
                library[book_id]["status"] = "Available"
                print(f"\nBook '{library[book_id]['title']}' returned successfully!")
            else:
                print("\nThis book is already available (not borrowed)!")
        else:
            print(f"\nNo book found with ID {book_id}")

            #Delete books

    elif choice == "6":
        book_id = input("Enter Book ID to delete: ").strip()
        if book_id in library:
            del library[book_id]
            print(f"\nBook with ID {book_id} deleted successfully!")
        else:
            print(f"\nNo book found with ID {book_id}")

    else:
        print("\nInvalid choice! Please select 1-7.")

    print("-" * 50)