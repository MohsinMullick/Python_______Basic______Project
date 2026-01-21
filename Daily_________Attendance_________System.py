#Daily Attendance System
from datetime import datetime #python build in datetime module from datetime import
attendance={}#create dictionary and store all data
#---------Welcome user Screen--------
print("="*50)
print("     WELCOME TO DAILY ATTENDANCE SYSTEM     ")
print("="*50)
print("Track easily daily attendance")
print("Type 'q' or 'quit' or 'exit' to stop")
print("="*50)

#---------infinite loop create for user------------
while True:
    print("----------MAIN MENU---------")
    print("1. Add New Person(Student/Employee): ")
    print("2. Marks Today's Attendance")
    print("3. View Today's Attendance")
    print("4. View One Person Attendance History")
    print("5. View Attendance for a Specific Date")
    print("6. Exit/Quit")

    choice=input("Enter choice (1 to 4): ").strip().lower()
    if choice in ['6','exit','quit','q']:
        print("Thank you for using attendance system.GoodBye")
        break

    elif choice=="1":
        person_id=input("Enter Unique ID(e.g.,A001/B001").strip().lower()
        if person_id in attendance:
            print(f"Person ID {person_id} already exit")
            continue

        name=input("Enter Name: ").strip().lower()
        attendance[person_id]={"name":name,"records":{}}
        print(f"Name {name} ID {person_id} added successful.")

    #------Marks Today's Attendance-----
    elif choice=="2":
        today=datetime.now().strftime("%Y-%M-%D")
        print(f"\nMarking attendance for: {today}")

        for pid,info in attendance.items():
            status = input(f"{info['name']} ({pid}) - Present (p) / Absent (a): ").strip().lower()
            if status in ['p', 'present']:
                attendance[pid]["records"][today] = "P"
            elif status in ['a', 'absent']:
                attendance[pid]["records"][today] = "A"
            else:
                attendance[pid]["records"][today] = "?"
                print(f"Invalid input for {info['name']}. Marked as '?'")
        print("\n Today's attendance marked successful")

    #-----Views today's attendance-----
    elif choice == "3":
        today = datetime.now().strftime("%Y-%m-%d")
        print(f"\nToday's Attendance ({today}):")
        print("-" * 50)
        print(f"{'ID':<10} {'Name':<25} {'Status':<10}")
        print("-" * 50)

        for pid, info in attendance.items():
            status = info["records"].get(today, "Not Marked")
            print(f"{pid:<10} {info['name']:<25} {status:<10}")
        print("-" * 50)


    #-----View one person attendance History-----
    elif choice == "4":
        person_id = input("Enter ID to view history: ").strip().upper()
        if person_id in attendance:
            info = attendance[person_id]
            print(f"\nAttendance History of {info['name']} ({person_id}):")
            print("-" * 50)
            total_days = len(info["records"])
            present_days = sum(1 for v in info["records"].values() if v == "P")
            print(f"Total days marked : {total_days}")
            print(f"Present days      : {present_days}")
            print(f"Absent days       : {total_days - present_days}")
            print("\nDate          Status")
            print("-" * 30)
            for date, status in sorted(info["records"].items()):
                print(f"{date}    {status}")
            print("-" * 50)
        else:
            print("No record found!")


    #-----View attendance for a specific date-----
    elif choice == "5":
        date_str = input("Enter date (YYYY-MM-DD): ").strip()
        print(f"\nAttendance on {date_str}:")
        print("-" * 50)
        print(f"{'ID':<10} {'Name':<25} {'Status':<10}")
        print("-" * 50)

        found = False
        for pid, info in attendance.items():
            status = info["records"].get(date_str, "Not Marked")
            if status != "Not Marked":
                print(f"{pid:<10} {info['name']:<25} {status:<10}")
                found = True
        if not found:
            print("No attendance marked on this date.")
        print("-" * 50)

    else:
        print("Invalid choice! Please select 1-6.")

    print("-" * 50)








