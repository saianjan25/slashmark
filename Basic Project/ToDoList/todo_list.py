
class ToDoList:
    #Class constructor  to initialize the list of tasks
    def __init__(self):
        self.tasks=[]

    # this function is used to display the tasks in to-do list
    def displayTasks(self):
        print("\nMy TO-DO List:")
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task['name']} - {'Completed' if task['completed'] else 'Not Completed'}")

    # A function is going to be added to the to-do list
    def addTask(self):
        taskName=input("Enter the task name: ")
        self.tasks.append({"name": taskName, "completed": False})
        print(f"Task '{taskName}' added to my to-do list.")

    # Completed tasks are marked in this function 
    def mark_completed(self):
        self.displayTasks()
        taskNumber = int(input("Enter the task number to mark as completed: "))
        if 1 <= taskNumber <= len(self.tasks):
            self.tasks[taskNumber - 1]['completed'] = True
            print(f"Task '{self.tasks[taskNumber - 1]['name']}' marked as completed.")
        else:
            print("Invalid task number.")

    # this function is going to remove the tasks from the to-do list
    def remove_task(self):
        self.displayTasks()
        taskNumber = int(input("Enter the task number to remove: "))
        if 1 <= taskNumber <= len(self.tasks):
            removed_task = self.tasks.pop(taskNumber - 1)
            print(f"Task '{removed_task['name']}' removed from the to-do list.")
        else:
            print("Invalid task number.")

#This is main function
def main():
    todoList=ToDoList()
    # Main program loop
    while True:
        print("\n TO-DO LIST MENU")
        print("1. Display to-do list")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Quit\n")

        choice = int(input("Enter your choice: "))

        if choice ==1:
            todoList.displayTasks()
        elif choice ==2:
            todoList.addTask()
        elif choice == 3:
            todoList.mark_completed()
        elif choice == 4:
            todoList.remove_task()
        elif choice == 5:
            print("Exiting from the application.Thank you")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__=="__main__":
    main()