def menu():
    print("""
    Menu:
    1. Add task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit""")

incomplete_list = ["Nails", "vacuum", "clean"]
complete_list = ["Dishes"]

def add():
    print("what task would you like to add?")
    try:
        new_item = (input("Task: "))
        if new_item:
            incomplete_list.append(new_item)
            print(f"\nYour list is now: {incomplete_list}")
        else:
            print("Task cannot be blank")
    except ValueError:
        print("Please enter a valid task")
    menu()

def view():
    print(f"The tasks that still need done are:\n {incomplete_list}")
    print(f"The tasks you completed are:\n {complete_list}")
    

def complete_task():
    view()
    print("What task have you completed? :")
    completed = input("Completed task: ").strip()
    menu()
    
    if not  completed:
         print("Task cannot be left blank")
         return
    completed_lower = completed.lower()
    incomplete_list_lower = [words.lower() for words in incomplete_list]
   
    if completed_lower in incomplete_list_lower:
           
        index = incomplete_list_lower.index(completed_lower)
        task_move = incomplete_list[index] 

        complete_list.append(task_move)
        incomplete_list.pop(index)
        
        print(f"Your new completed list is: {complete_list}")
        print(f"Your new incomplete list is: {incomplete_list}")
    else:
        print("This is not one of your tasks")
    menu()

def delete():
    view()
    try:
        delete_task = input("Which task would you like to delete: ").strip()
        if not delete_task:
            print("This cannot be left blank")
            return
        delete_lower = delete_task.lower()
        incomplete_list_lower = [words.lower() for words in incomplete_list]
        complete_list_lower = [words.lower() for words in complete_list]    
        
        if delete_task in incomplete_list_lower:
            
            index = incomplete_list_lower.index(delete_lower)
            #task_delete = incomplete_list[index]
            incomplete_list.pop(index)
            print(f"Your new incomplete list is {incomplete_list}")
        
        elif delete_task in complete_list_lower:
            index2 = complete_list_lower.index(delete_lower)
            complete_list.pop(index2)
            print(f"Your new completed list is {complete_list}")
        
        else:
            print("This is not one of your tasks")
    except ValueError:
        print("Please enter a valid task")
    menu()

print("Welcome to the To-Do List App!")
menu()

while True:
    try:
        choice = input("What would you like to do?: ").strip().lower()
        if choice in ["1", "add", "add task"]:
            add()
        elif choice in ["2", "view", "view tasks"]:
            view()
        elif choice in ["3", "complete","mark task complete"]:
            complete_task()
        elif choice in ["4", "delete", "delete task"]:
            delete()
        elif choice == "quit":
            break
        else:
            print("Please input a valid command")
    except ValueError:
        print("Please enter valid characters")
   