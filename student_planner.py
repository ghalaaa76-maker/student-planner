#Names: [Ghala Aloraydi] []
#IDs:[447202149] []
Section:[65084]
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
  task={"id":next_task_id,
        "title":input("task title:"),
        "course":input("Course name:"),
        "due_date":input("Due date:"),
        "priority":input("Priority:"),
        "status":"Pending"}
  tasks.append(task)
  print("Task added successfully!")  
  return next_task_id + 1
def find_task_by_id(tasks,task_id):
  for i in tasks:
    if i["id"]==task_id:
      return i
  return None
def display_task(task):
  print("Task ID:",task["id"])
  print("Task title:",task["title"])
  print("Task coures:",task["course"])
  print("Task Due date:",task["due_date"])
  print("Task priority:",task["priority"])
  print("Task status:",task["status"])
def delete_task(tasks):
  task_id=int(input("Enter task id to delete'))
  task_to_delete=find_task_by_id(tasks,task_id)
  if task_to_delete is None:
     print("Task not found")
  else:
    tasks.remove(task_to_delete)
    print("Task deleted")

def mark_task_completed(tasks):
    task_id=int(input("Enter task id to mark completed")
    task_to_complete=find_task_by_id(tasks,task_id)
    if task_to_complet is None:
       print("task not found")
    else:
       if task_to_complete["status"]=="Completed":
         print("arleady completed")
       else:
         task_to_complete["status"]="completed"




  
  
                    
  
  
  
  









































                                        
