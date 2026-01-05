
tasks=[]#all list stor this tasks.And every tasks store the dictionary
def add_task():#define function
    task_name=input("Enter task name: ")#user input
    tasks.append({"task":task_name,"done":False})#use dictionary because dictionary carry the key: and value
    #append =python list built in  method(function) that's add some value when list fulfil then append last value
    print(f"Task",{task_name},"added successful!")

def view_task():#define function
    if not tasks:#this line check the first list tasks[] because at first list always empty
        print("No task available")#show the results
        return#just stop the function because task not available

    print("\n------your to do list------")#jsut one heading nothing else
    for i,task in enumerate(tasks,start=1):#enumerate that's say tasks list all item continue the loop
        status="done" if task["done"] else "x"#just ternary operator
        print(f'{i}.{status}{task["task"]}')

def mark_complete():#define function and user which complete they marked all
    view_task()#this line show the all tasks
    if not tasks:#jsut check
        return

    try:#try-except because user any input included
        num=int(input(f"Which task number to delete?"))
        if 1<=num <=len(tasks):
            removed=tasks.pop(num-1)
            print(f"task {removed}[task],deleted successful!")
        else:
            print(f"invalid task numbers")
    except ValueError:
        print("Please enter a valid numbers")

#######---------Main Menu Mohsin Mullik---------
while True:
    print("\n------To Do List MENU-------")
    print("1. Add new task")
    print("2. View all task")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Exit")


    choice=input("Choice an option (1: 5): ")
    if choice=="1":
        add_task()
    elif choice=="2":
        view_task()
    elif choice=="3":
        mark_complete()
    elif choice=="4":
        delete_task()
    elif choice=="5":
        print("Bye Bye!See you again!!!!!")
        break
    else:
        print("wrong choice ! please select between 1 to 5: ")








