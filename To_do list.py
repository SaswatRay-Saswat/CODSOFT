tasks = []

def addTask():
     task = input("Please enter a task : ")
     tasks.append(task)
     print(f"Task '{task}' added to the  list.")

def listTasks():
    if not tasks:
         print("\nThere are no task currently.")
    else:
         print("\nCurrent Tasks: ")
         for count, task in enumerate(tasks,1):
              print(f"Task #{count}. {task}")
              
          
def deleteTask():
     listTasks()
     try:
        taskTOdelete= int(input("\nChoose the task to be deleted :"))
        if 0 <= taskTOdelete <= len(tasks):
             tasks.pop(taskTOdelete-1)
             print(f"Task #{taskTOdelete} has been removed.")
        else:
             print(f"Task #{taskTOdelete} was not found.")
     except:
          print("Invalid input.")

          
          
if __name__=="__main__":
    print("Welcome to the To-Do list :")
    while True:
         print("\n")
         print("Please select one of the following options->")
         print("1. Add a new task")
         print("2. List tasks")
         print("3. Delete a task")
         print("4. Exit")

         choice = input("\nEnter your choice : ")

         if(choice =="1"):
              addTask()
         elif(choice =="2"):
              listTasks()
         elif(choice =="3"):
              deleteTask()
         elif(choice =="4"):
              break
         else:
              print("Invalid input.\nPlease try again")
    
    print("\nApp closed")

                   

        
        
         
