def to_do_list():
  tasks=[]
  while True:
   print("1. Add task")
   print("2. Remove task")
   print("3. show task")
   print("4. quit")
   choice=input("enter your choices: ")
   if(choice=='1'):
     task=input("enter task: ")
     tasks.append(task)
   elif(choice=='2'):
     task=input("enter task to be remove: ")
     if task in tasks:
        tasks.remove(task)
     else:
        print("Task not found")
   elif(choice=='3'):
     print("Tasks: ")
     for task in tasks:
        print("-"+task)
   elif(choice=='4'):
    break
   else:
    print("invalid choice")

to_do_list()