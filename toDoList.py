"""
----------------------------------
Project: a simple to do list
that can be used for everyday tasks
----------------------------------
Author: Abia Shahbaz
----------------------------------
"""
#store all tasks in list
tasksList = []

#ask for user name
print(f"**> Welcome to the to-do list app! <**")
name = input("\nWhat's your name?: ")

#prints list template
print(f"\n\n--{name}'s TO-DO LIST--")

if len(tasksList) == 0:
    
        print(f"  no current tasks")
else:
        #for loop to print each item in list
        for i in tasksList:
            print(i)
            
#menu option           
print("\n\n\n")
print(f"1.Add Task")
print(f"2.Edit")
print(f"3.Delete")
print(f"4.Exit App")



num = 0   
while num != 4: 
    
    #ask user to choose option on menu
    num = int(input(f"What would you like to do (1,2,3,4):"))
    
    #if user chooses one, add a task
    if num==1:
        cnt = 0
        t1 = input("Create Task: ")
        tasksList.append(t1) #add to list
        cnt+=1
        
        #print new list
        print(f"\n\n--{name}'s TO-DO LIST--")

        if len(tasksList) == 0:
            
    
            print(f"  no current tasks")
        else:
        
            for i, task in enumerate(tasksList, start=1):
                print(f"Task {i}: {task}")
                
               
    #if user chooses two, edit task
    elif num==2:
        
        ed = int(input(f"Which task would you like to edit?"))
        
        if len(tasksList)==0:
            print(f"No tasks to edit")
            
        #checks to see if user choice is not out of bounds
        elif ed <=len(tasksList): 
            

            nme = input((f"Change task to: "))
            tasksList[ed-1] = nme #direct change to og list
            
            #print updated list
            print(f"\n\n--{name}'s TO-DO LIST--")

            if len(tasksList) == 0:
            
    
                print(f"  no current tasks")
                
            else:
        
                for i, task in enumerate(tasksList, start=1):
                        print(f"Task {i}: {task}")
        else:
            #for catching errors
            print(f"Task # does not exist, sorry!\n")
            
        
    #if user chooses three, delete a task  
    elif num == 3:
        nm = int(input(f"Which task out of {len(tasksList)} task(s) do you want to delete?"))
        
        #check to see if in bounds
        if nm <=len(tasksList):
            tasksList.pop(nm-1)
            print(f"Task successfully deleted!")
            
            #print edited ver
            print(f"\n\n--{name}'s TO-DO LIST--")

            if len(tasksList) == 0:
            
    
                print(f"  no current tasks")
            else:
        
                for i, task in enumerate(tasksList, start=1):
                    print(f"Task {i}: {task}")
        else:
            print(f"Task # does not exist, sorry!\n")
            
    #if user chooses four, exit list
    elif num ==4:
        
        #exit to do list, user friendly
        print(f"Thank you for using the to do list! We hope to see you soon :D")
        
        
    else:
        print(f"Sorry that option doesnt exist, please try again.")
            
    

  
        
      
    
    


