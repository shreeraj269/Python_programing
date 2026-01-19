# Aim:task list
#coder:shreeraj
#Date:19-01-26

print("Task List Manager")
task1 = input("enter first task ")
task2 = input("enter second task ")
task3 = input("enter third task ")

tasks =[task1,task2,task3]
print(f"Original Tasks: {tasks}")
 
# add new task
append_task=input("enter new task which you want to add :")
tasks.append(append_task)
print(f"Update Tasks: {tasks}")
# update a task
#tasks.remove("breakfast")
#tasks.append("lunch")
#print(f"update Tasks: {tasks}")
tasks[2]="lunch"
print(f"update Tasks: {tasks}")

#remove a task
tasks.remove(task2)
print(f"remove Tasks: {tasks}")

#sort task
tasks.sort()
print(f"sort Tasks: {tasks}")