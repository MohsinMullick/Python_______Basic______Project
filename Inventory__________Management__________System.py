#Inventory Management System
inventory={}#Create dictionary that's store all items
  #----------See the User Welcome----------
print("="*50)
print("    Welcome to Inventory Management System     ")
print("="*50)
print(" Manage your product stock easily!!")
print(" Type 'quit' or 'exit' to stop anytime ")
print("="*50)

  #----------Create infinite loop for Menu Bar until we break----------
while True:
    print("----------Main Menu----------")
    print("1. Add New Product ")
    print("2. View All products ")
    print("3. Search product ")
    print("4. Update product ")
    print("5. Delete product ")
    print("6. Show low stock products(less than 10): ")
    print("7. Exit")


    choice=input("Enter choice (1 to 7): ").strip()#at first create exit because for User friendly

    if choice in ['7','quit','exit']:#Create condition for exit okr quit,in just right to check exit or not
        print("\n Thank you for using Inventory Management System : ")
        break#when condition true like 7 or quit or exit then out of loop

    #---------Add New Products--------
    elif choice=="1":
        prod_id=input("Enter Product Unique ID: ").strip().title()#.strip() maintain space
        if prod_id in inventory:# this condition check all items in inventory dictionary
            print(f"\n Product {prod_id} already exit.")
            continue#if condition true then the show the message

        name=input("Enter Product name: ").strip().title()#first we add product so at first we take name input


        try:#try use for error check
            price=float(input("Enter price: "))
            stock=int(input("Enter initial stock: "))

        except ValueError:#user shows the good message for this error
            print("\n Price must be number and stock must be integer. ")
            continue

        category=input("Enter Category(e.g. Electronic/Clothing").strip().title()
        inventory[prod_id]={#create dictionary for save and then provide inventory main dictionary
            "name":name,#prod_id =key and name,price,stock,category=value
            "price":price,
            "stock":stock,
            "category":category
        }
        print(f"\n Product {name} added successful! ID {prod_id}")


     #----------View All Products---------
    elif choice=="2":
        if not inventory:#first check product save found or not
            print("\n No products in inventory yet.")
        else:
            print("\n"+ 50*"=")
            print("----------All Products of Inventory----------")
            print("="*50)
            print(f"{"ID":<10} {"Name":<25} {"Product":<10} {"Stock":<8} {"Category":<20}")
            print("="*50)
            for pid, info in inventory.items():#this loop full inventory dictionary every item one times check
                #Create Header like: prod_id,name,price,stock,category
                print(f"{pid:<10} {info['name']:<25} {info['price']:<10.2f} {info['stock']:<8} {info['category']:<20}")
            print("=" * 50)

    #----------Search Products----------
    elif choice=="3":
        search=input("Enter product Name/ID/Category: ").strip().lower()
        found =False#boolean flag variable this variable use just for assume because when we don't find any value we print no product found yet
        print("\n Search Results: ")
        for pid,info in inventory.items():# this loop full inventory dictionary every item one times continue or check
            #dictionary all key and value give the list help inventory.items()
            #like pid=key and info all values: "name":"t-shirts","price":450
            #when we don't use inventory.items() we don't get key value pair just show individual key and value
            if (search in info["name"].lower() or search in pid.lower()
                    or search in info["category"].lower()):#This condition check user what write like product name,id price,stock
                print(
                    f"ID: {pid} | {info['name']} | Price: {info['price']} | Stock: {info['stock']} | Category: {info['category']}")
                found = True
            if not found:
                print("No product found.")


    #----------Update Stock----------
    elif choice=="4":
        prod_id=input("Enter product id to update stock: ").strip().title()
        if prod_id in inventory:#first prod_id check exit or not in inventory dictionary
            try:
                change = int(input("Enter stock change (+ to add, - to reduce): "))
                new_stock = inventory[prod_id]["stock"] + change
                if new_stock < 0:
                    print("Stock cannot be negative!")
                else:
                    inventory[prod_id]["stock"] = new_stock
                    print(f"\nStock updated! New stock: {new_stock}")
            except ValueError:
                print("Enter valid number!")
            else:
                print(f"No product with ID {prod_id}")


    #-----------Delete Product ID----------
    elif choice == "5":
        prod_id = input("Enter Product ID to delete: ").strip().upper()
        if prod_id in inventory:
            del inventory[prod_id]#del method use for delete prod_id
            print(f"\nProduct ID {prod_id} deleted successfully!")
        else:
            print(f"No product with ID {prod_id}")



    #----------Show low stock products-----------
    elif choice == "6":
        low_stock = [(pid, info) for pid, info in inventory.items() if info["stock"] < 10]
        if not low_stock:
            print("\nNo low stock products (all ≥ 10).")
        else:
            print("\n" + "=" * 50)
            print("           LOW STOCK PRODUCTS (less than 10)           ")
            print("=" * 50)
            for pid, info in low_stock:
                print(f"ID: {pid} | {info['name']} | Stock: {info['stock']} | Price: {info['price']}")
            print("=" * 50)

    else:
        print("\nInvalid choice! Please select 1-7.")

    print("-" * 50)


















