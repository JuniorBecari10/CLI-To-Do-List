from os import system, name
from tabulate import tabulate

todolist = []

# Functions

def clear():
    # for windows
    if name == 'nt':
        system('cls')
    
    # for mac and linux(here, os.name is 'posix')-
    else:
        system('clear')

def main():
    clear()
    
    while True:
        try:
            print("To-Do List", "\n")
            
            if not todolist: # if the list is empty
                print("List is empty!", "\n")
            else:
                print(tabulate(todolist, headers=["Index", "Task", "Completed"], showindex="always"), "\n")
            
            print("Choose an option:")
            
            if todolist:
                print("1: Add Task", "\n2: Remove Task\n3: Set Completed/Uncompleted\n4: Rename Task\n5: Swap Tasks" + (" | Deactivated - List is too short" if len(todolist) < 2 else "") + "\n6: Exit")
            else:
                print("1: Add Task\n2: Exit")
            
            print()
            option = input()
            
            if option == "1":
                task = input("Enter the name: ")
                
                todolist.append([task, "No"]);
                
                clear()
            elif option == "2" and todolist:
                index = int(input("Enter index: "))
                
                if index >= len(todolist):
                    clear()
                    continue
                
                todolist.pop(index)
                
                clear()
            elif option == "3" and todolist:
                index = int(input("Enter index: "))
                
                if index >= len(todolist):
                    clear()
                    continue
                
                todolist[index][1] = "Yes" if todolist[index][1] == "No" else "No"
                clear()
            elif option == "4" and todolist:
                index = int(input("Enter index: "))
                name = input("New name: ")
                
                todolist[index][0] = name
                
                clear()
            elif option == "5" and todolist:
                if len(todolist) == 1:
                    clear()
                    continue
                
                idx1 = int(input("First index: "))
                idx2 = int(input("Second index: "))
                
                if idx1 >= len(todolist) or idx2 >= len(todolist):
                    clear()
                    continue
                
                todolist[idx1], todolist[idx2] = todolist[idx2], todolist[idx1]
                
                clear()
            elif option == "6" and todolist or option == "2" and not todolist:
                exit()
            else:
                clear()
                continue
        except Exception:
            clear()
            continue
main()
