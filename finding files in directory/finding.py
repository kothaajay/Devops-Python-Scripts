import os

directory = input("Please enter the directories sepearted by space:").split(' ')

for i in range(len(directory)):
    try:
        files = os.listdir(directory[i])
        print(f"files in {directory[i]}:")  
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Directory {directory[i]} does not exist.") 
    except PermissionError:
        print(f"Permission denied for directory {directory[i]}.")           
    
    
