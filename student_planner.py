#Names: [Ghala Aloraydi] [Leena alaqil]
#IDs:[447202149] [447202541]
#Section:[65084]
def display_menu():
  print()
  print("STUDENT PLANNER")
  print("-" * 40)
  print("1. Add  a task")
  print("2. Edit a task")
  print("3. Delete a task")
  print("4 . Find a task by ID")
  print("5. List all task")
  print("6. List tasks by courses")
  print("7. List tasks by priority")
  print("8. Mark a task as completed")
  print("9. View tasks summary")
  print("10. Exit")
  print("-" * 40)
def add_task(tasks,next_task_id):
  title = input("Task title: ").strip()
  while title =="":
    print("This field cannot be empty")
    title =input("Task title: ").strip()
  course = input("Course name: ").strip()
  while course =="":
    print("This field cannot be empty.")
    course =input("Course name: ").strip()
  while True:
    due_date =input("Due date (DD/MM/YYYY): ").strip()
    if (len(due_date) ==10
           and due_date[2] =="/"
           and due_date[5] =="/"
           and due_date[0:2].isdigit()
           and due_date[3:5].isdigit()
           and due_date[6:10].isdigit()):
        break
    print("Invalid date format. Use DD/MM/YYYY")
  priority_level ={"1": "High", "2" : "Medium", "3" : "Low"}
  choice = input("Priority (1=High, 2=Medium, 3=Low): ").strip()
  while choice not in priority_level:
    print("Invalid priority. Enter 1,2 or 3.")
    choice = input("Priority (1=High, 2=Medium, 3=Low): ").strip()
  task = {
      "id": next_task_id,
      "title": title,
      "course":course,
      "due_date":due_date,
      "priority":priority_level[choice],
      "status": "Pending"
      
  }
  tasks.append(task)
  print("Task added successfully. Task ID:", next_task_id)
  return next_task_id +1
           
def find_task_by_id(tasks,task_id):
  for i in tasks:
    if i["id"]==task_id:
      return i
  return None




  
def display_task(task):
  print("ID:",task["id"])
  print("Title:",task["title"])
  print("Course:",task["course"])
  print("Due date:",task["due_date"])
  print("Priority:",task["priority"])
  print("Status:",task["status"])
  



def edit_task(tasks):
    # Check if the task ID is valid
    task_id =input("Enter task ID:").strip()
    if task_id.isdigit():
       if int(task_id) > 0:
          task_id = int(task_id)
       else:
          print("Invalid ID. Enter digits 0-9 with a value greater than zero.")
          return
    else:
        print("Invalid ID. Enter digits 0-9 with a value greater than zero.")
        return
    task = find_task_by_id(tasks, task_id)
    if task is None:
        print("Task not found.")
        return

    if task["status"] == "Completed":
        print("This task is completed you can't edit")
        return

    print("1. Title")
    print("2. Course")
    print("3. Due date")
    print("4. Priority")
    print("5. Cancel")
    user_choice = input("Enter your choice: ").strip()

    if user_choice == "1":
        title = input("Enter new task title: ").strip()
        while len(title) == 0:
            print("This can not be empty")
            title = input("Enter new task title: ").strip()
        task["title"] = title

    elif user_choice== "2":
        course = input("Enter new course: ").strip()
        while len(course) == 0:
            print("This field cannot be empty.")
            course = input("Enter new course: ").strip()
        task["course"] = course

    elif user_choice == "3":
        #read the if the date is true
        while True:
           date = input("Enter new due date (DD/MM/YYYY): ").strip()
           if (len(date) == 10 and
                 date[2] == "/" and
                 date[-5] == "/" and
                 date[0:2].isdigit()and
                 date[3:5].isdigit()and
                 date[6:10].isdigit()):
                break
           else:
                print("Invalid date format- Use DD/MM/YYYY")
                continue
        task["due_date"] = date

    elif user_choice == "4":
        priority_level = {"1": "High", "2": "Medium", "3": "Low"}
        choice = input("Priority (1=High, 2=Medium, 3=Low): ").strip()
        while choice not in priority_level:
            print("Invalid priority. Enter 1, 2, or 3.")
            choice = input("Priority (1=High, 2=Medium, 3=Low): ").strip()
        task["priority"] = priority_level[choice]

    elif user_choice== "5":
        print("Edit cancelled.")
        return

    else:
        print("Invalid choice.")
        return

    print("Task updated successfully.")


def delete_task(tasks):
  task_id=input("Enter task ID: ").strip()
  if not task_id.isdigit() or int(task_id) <=0:
    print("Invalid ID. Enter digits 0-9 with a value greater than zero.")
    return
  task_id=int(task_id)
  task_to_delete =find_task_by_id(tasks, task_id)
  if task_to_delete is None:
     print("Task not found")
  else:
    tasks.remove(task_to_delete)
    print("Task deleted successfully")

# Show all tasks
def list_all_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return
    for task in tasks:
        display_task(task)


# Show tasks by course
def list_tasks_by_course(tasks):
    course = input("Enter course code : ").strip()

    while course == "":
        print("This field cannot be empty.")
        course = input("Enter course code : ").strip()

    exists= False

    for task in tasks:
        if course.lower() == task["course"].lower():
            display_task(task)
            exists = True

    if exists == False:
        print("No tasks exists for this course.")
      


# Display tasks with the selected priority
def list_tasks_by_priority(tasks):
    while True:
        choice = input("Priority (1=High, 2=Medium, 3=Low): ").strip()
        if choice == "1":
            priority = "High"
            break
        elif choice == "2":
            priority = "Medium"
            break
        elif choice == "3":
            priority = "Low"
            break
        else:
            print("Invalid priority. Enter 1, 2, or 3.")
        display_task(task)

    available = False
    for task in tasks:
        if task["priority"] == priority:
            display_task(task)
            available = True

    if available== False:
        print("No available task with this priority.")
    

    
def mark_task_completed(tasks):
    task_id=input("Enter task ID: ").strip()
    if not task_id.isdigit() or int(task_id) <= 0:
        print("Invalid ID. Enter digits 0-9 with a value greater than zero.")
        return
    task_id =int(task_id)
    task = find_task_by_id(tasks, task_id)
    if task is None:
        print("Task not found")
    elif task["status"] =="Completed":
        print("Task is already completed")
    else:
        task["status"] = "Completed"
        print("Task",task_id,"marked as completed.")

def show_summary(tasks):
    total = len(tasks)
    completed = 0
    pending = 0

    for task in tasks:
        if task["status"] == "Completed":
           completed += 1
        else:
            pending += 1

    print("\n--- Task Summary ---")
    print("Total tasks:", total)
    print("Pending tasks:", pending)
    print("Completed tasks:", completed)

    if total != 0:
        percentage = (completed / total) * 100
        print(f"Completion percentage: {percentage:.1f}%")
    else:
        print("Completion percentage: 100%")



# Display the menu and process user choices
def main():
    tasks = []
    next_task_id = 1
    choice = 0

    while choice != 10:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if not choice.isdigit():
            print("Invalid menu choice.")
            continue

        choice = int(choice)

        match choice:
            case 1:
                next_task_id = add_task(tasks, next_task_id)

            case 2:
                edit_task(tasks)

            case 3:
                delete_task(tasks)

            case 4:
                task_id = input("Enter id : ").strip()

                if not task_id.isdigit():
                    print("Invalid ID. Enter digits 0-9 with a value greater than zero.")
                    continue

                task_id = int(task_id)

                if task_id <= 0:
                    print("Invalid ID. Enter digits 0-9 with a value greater than zero.")
                    continue

                task = find_task_by_id(tasks, task_id)

                if task is None:
                    print("Task not found.")
                else:
                    display_task(task)

            case 5:
                list_all_tasks(tasks)

            case 6:
                list_tasks_by_course(tasks)

            case 7:
                list_tasks_by_priority(tasks)

            case 8:
                mark_task_completed(tasks)

            case 9:
                show_summary(tasks)

            case 10:
                print("Goodbye!")

            case _:
                print("Invalid menu choice.")


main()
    
    
    
    
                    
  
  
  
  









































                                        
