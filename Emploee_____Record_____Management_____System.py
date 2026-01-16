#Employee Record Management System CLI
employees={}#Create dictionary key=emp_id and value=name,position,department,salary,joint_date
  #welcome for user
print("="*50)
print("  Welcome to Employee Record Management System  ")
print("="*50)
print("Manage employee record easily! ")
print("Type 'quit' or 'exit' to stop  any time. ")
print("="*50 + '\n')

  #infinite loop use for menu bar
while True:
    print("1. Add New Employee: ")
    print("2. View All Employees: ")
    print("3. Search Employee: ")
    print("4. Update Employee Record: ")
    print("5. Delete Employee Record: ")
    print("6. View Employee Department: ")
    print("7. View Highest and Lowest Salary: ")
    print("8. Exit")


    choice=input("\n Choice option (1-8): ").strip() #user choice menu
    if choice in['7','exit','quit']:#choice exit for user fiendly
        print("\n Thank you for using Employee Record Management System.!! ")
        break
    #-------Add Employee New ID---------
    elif choice == "1":
        emp_id = input("Enter unique Employee ID: ").strip().upper()
        if emp_id in employees:
            print(f"Employee ID {emp_id} already exists!")
            continue#when id same then give message and again try

        name = input("Enter Employee Name: ").strip().title()
        position = input("Enter Position: ").strip().title()
        department = input("Enter Department: ").strip().title()
        try:#if any one salary text then give message float .so try use for special error
            salary = float(input("Enter Salary: "))
        except ValueError:
            print("Salary must be a number!")
            continue
        join_date = input("Enter Join Date (YYYY-MM-DD): ").strip()

        employees[emp_id] = {
            "name": name,
            "position": position,
            "department": department,
            "salary": salary,
            "join_date": join_date
        }
        print(f"\nEmployee {name} (ID: {emp_id}) added successfully!")

    #------View All Employees----------
    elif choice=="2":
        if not employees:
            print("\nNo employee added yet.")
        else:
            print("="*50)
            print("----------All Employee Records----------")
            print("="*50)
            #Create header line
            print(f"{"ID":<10} {"Name":<25} {"Position":<20} {"Department":<20} {"Salary":<12} {"Join_Date":<12}")
            for eid,info in employees.items():
                print(f"{eid:<10} {info["Name"]:<25} {info["Position"]:<20} {info["Department"]:<20} {info["Salary"]:<12} {info["Join_Date"]:<12}")
            print("="*50)

   #--------Search Employee Record-------
    elif choice == "3":
        search = input("Enter Name / ID / Position / Department: ").strip().lower()
        found = False
        print("\nSearch Results:")
        for eid, info in employees.items():
            if (search in info['name'].lower() or
                    search in eid.lower() or
                    search in info['position'].lower() or
                    search in info['department'].lower()):
                print(
                    f"ID: {eid} | {info['name']} | {info['position']} | {info['department']} | Salary: {info['salary']} | Join: {info['join_date']}")
                found = True
        if not found:
            print("No employee found matching your search.")
   #-------Update Employee Record------
    elif choice == "4":
        emp_id = input("Enter Employee ID to update: ").strip().upper()
        if emp_id in employees:
            field = input("What do you want to update? (name/position/department/salary): ").lower()
            if field in ["name", "position", "department"]:
                new_value = input(f"New {field}: ").strip().title()
                employees[emp_id][field] = new_value
                print(f"\n{field.capitalize()} updated successfully!")
            elif field == "salary":
                try:
                    new_salary = float(input("New Salary: "))
                    employees[emp_id]["salary"] = new_salary
                    print("\nSalary updated successfully!")
                except ValueError:
                    print("Invalid salary!")
            else:
                print("Invalid field!")
        else:
            print(f"No employee with ID {emp_id}")
    #------Delete Employee Record------
    elif choice == "5":
        emp_id = input("Enter Employee ID to delete: ").strip().upper()
        if emp_id in employees:
            del employees[emp_id]#del function use for delete
            print(f"\nEmployee ID {emp_id} deleted successfully!")
        else:
            print(f"No employee with ID {emp_id}")
    #-------Employee Department Check--------
    elif choice == "6":
        dept = input("Enter Department name: ").strip().title()
        found = False#boolean flag variable ,first we assume condition false
        print(f"\nEmployees in {dept}:")
        for eid, info in employees.items():
            if info["department"] == dept:
                print(f"ID: {eid} | {info['name']} | {info['position']} | Salary: {info['salary']}")
                found = True
        if not found:
            print(f"No employees found in {dept} department.")
    #-------View Highest and lowest salary check----------
    elif choice == "7":
        if not employees:
            print("\nNo employees yet.")
        else:
            salaries = [info["salary"] for info in employees.values()]
            print(f"\nHighest Salary : {max(salaries)}")
            print(f"Lowest Salary  : {min(salaries)}")

    else:
        print("\nInvalid choice! Please select 1-8.")

    print("-" * 50)

