# Aim:task list
#coder:shreeraj
#Date:19-01-26

print("Task List Manager")
tasks = ["Wakeup","Brush","breakfast"]
print(f"Original Tasks: {tasks}")
 
# add new task
tasks.append("College")
print(f"Update Tasks: {tasks}")
# update a task
#tasks.remove("breakfast")
#tasks.append("lunch")
#print(f"update Tasks: {tasks}")
tasks[2]="lunch"
print(f"update Tasks: {tasks}")

#remove a task
tasks.remove("Brush")
print(f"remove Tasks: {tasks}")

#sort task
tasks.sort()
print(f"sort Tasks: {tasks}")