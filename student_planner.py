#Names: [Ghala Aloraydi] []
#IDs:[447202149] []
Section:[65084]
def display_menu():
  print()
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










































                                        
