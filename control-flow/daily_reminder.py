task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case 'high':
        reminder = ' is a high priority task'
    case 'medium':  
          reminder = ' is a medium priority task'
    case 'low':    
           reminder = ' is a low priority task' 

if time_bound == 'yes':
     print(f"Reminder: '{task}' {reminder} that requires immediate attention today!")
elif  time_bound == 'no':
     print(f"Note'{task}' {reminder}. Consider completing it when you have free time.")
     
        