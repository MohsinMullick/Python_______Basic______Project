#Student Results Management System
students={}# Create empty dictionary and all information store this library like key=roll_no, values=dictionary of info


#Create welcome screen
print("="*50)#50 equal sign create
print("    Welcome Students Results Management System       ")#print this line
print("="*50)#Again 50 equal sign create
print("Manage students marks easily!")#this line print
print("Type 'quit' or 'exit' to stop .")#this same line print specially for next use this line
print("="*50+'\n')#again equal sign print



#user sow the menu for do this work
while True:#infinite loop create  continue until we create break
    print("\n-----MAIN MENU-----")
    print("1. Add New Student ")
    print("2. View All Student ")
    print("3. Search All Student ")
    print("4. Update Marks ")
    print("5. Delete Student ")
    print("6. Show Top 5 Students ")
    print("7. Exit")
    #if we don't crate break loop continue
    choice=input("Enter choice (1 to 7): ").strip()#input for user choice the menu and .strip control space error
    if choice in ['7','exit','quit']:#if we don't create loop always continue and user don't like
        print("\n Thank you for using student results systems.GoodBye!!")
        break

    #1. Add New Student
    elif choice=="1":
        roll=input("Enter roll number: ").strip()
        if roll in students:#check the roll in students dictionary
            print(f"Roll {roll} already exists.")
            continue

        name=input("Enter student name: ").strip().title()#.strip maintain space and title maintain first letter capital
        try:
            bangla=float(input("Bangla Marks: "))
            english=float(input("English Marks: "))
            math=float(input("Math Marks: "))
            science=float(input("Science Marks: "))
            social=float(input("Social Marks: "))
        except ValueError:#maintain the error because user provide check number or text check
            print("Marks must be numbers.Try again")
            continue

        total=bangla+english+math+science+social#total subject marks
        percentage=(total/500)*100


        students[roll]={#first we declare empty dictionary now use roll means key use and = means key values
            "name":name,
            "bangla":bangla,
            "english":english,
            "math":math,
            "science":science,
            "social":social,
            "total":total,
            "percentage":round(percentage,2)
        }
        print(f"student {name} roll {roll} added successful")


#View All Student
    elif choice=="2":
        if not students:
            print("\n No students added yet.")
        else:
            print("\n" + "=" * 50)
            print("           ALL STUDENTS RESULT              ")
            print("=" * 50)
            print(f"{'Roll':<10} {'Name':<20} {'Bangla':<8} {'English':<8} {'Math':<8} {'Science':<8} {'Social':<8} {'Total':<8} {'%':<8}")
            print("-" * 50)
            for roll, data in students.items():#.items means dictionary key value pair and roll=key and data=value
                print(
                    f"{roll:<10} {data['name']:<20} {data['bangla']:<8} {data['english']:<8} {data['math']:<8} {data['science']:<8} {data['social']:<8} {data['total']:<8} {data['percentage']:<8}")
            print("=" * 50)


    #Search All Students
    elif choice=="3":
        roll=input("Enter roll number to search: ").strip()
        if roll in students:#in operation only check dictionary key and same =True other False
            data=students[roll]#if up condition true then all value contain the new variable
            print(f"\nFound:")
            print(f"Name      : {data['name']}")
            print(f"Bangla    : {data['bangla']}")
            print(f"English   : {data['english']}")
            print(f"Math      : {data['math']}")
            print(f"Science   : {data['science']}")
            print(f"Social    : {data['social']}")
            print(f"Total     : {data['total']}")
            print(f"Percentage: {data['percentage']}%")
        else:
            print(f"\n No students found with roll {roll}")#if the condition false this line print

    #Update All Marks
    elif choice=="4":
        roll=input("Enter Roll Number To Update: ").strip()
        if roll in students:
            subject = input("Which subject to update? (bangla/english/math/science/social): ").lower()
            if subject in ["bangla", "english", "math", "science", "social"]:
                try:
                    new_mark = float(input(f"New marks for {subject}: "))
                    students[roll][subject] = new_mark
                    # recalculate total & percentage
                    data = students[roll]
                    data["total"] = data["bangla"] + data["english"] + data["math"] + data["science"] + data["social"]
                    data["percentage"] = round((data["total"] / 500) * 100, 2)
                    print(f"\n{subject.capitalize()} marks updated! New total: {data['total']}")
                except ValueError:
                    print("Invalid marks!")
            else:
                print("Invalid subject!")
        else:
            print(f"No student with Roll {roll}")

    elif choice == "5":
        roll = input("Enter Roll Number to delete: ").strip()
        if roll in students:
            del students[roll]
            print(f"\nStudent with Roll {roll} deleted successfully!")
        else:
            print(f"No student with Roll {roll}")


#show top 5 students

    elif choice == "6":
        if not students:
            print("\nNo students yet.")
        else:
            sorted_students = sorted(students.items(), key=lambda x: x[1]["total"], reverse=True)#this line maintain students marks
            print("\n" + "=" * 50)
            print("              TOP 5 STUDENTS (by total marks)              ")
            print("=" * 50)
            for i, (roll, data) in enumerate(sorted_students[:5], 1):
                print(f"{i}. {data['name']} (Roll: {roll}) - {data['total']} marks ({data['percentage']}%)")
            print("=" * 50)
    else:
        print("\nInvalid choice! Please enter 1-7.")

    print("-" * 50)