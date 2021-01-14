


#This method Creates new tasks, arguments:
# filename: The name of the file
# task: the task the user wants to store

def create_task(filename: str, task: str): 
    with open("data/" + filename + ".txt", "a+") as f: 
        f.write(task + "\n")


#This method Shows  tasks, it will read all lines and print them, arguments:
# filename: The name of the file

def show_task(filename: str):
    with open("data/" + filename + ".txt", "r") as f: 
        lines = f.readlines()
        for line in lines:
            print(line)


#This method Deletes tasks, it reads lines, then compares it with the task that will be deleted 
#and if it is different it will write it again inside the file, arguments:
# filename: The name of the file
# task: the task the user wants to delete
def delete_task(filename: str, task):
    with open("data/" + filename + ".txt", "r+") as f: 
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if line.strip("\n") not in task:
                f.write(line)
        f.truncate()

#This method marks tasks as done, it reads lines, then compares it with the task that will be marked
#and if it is equals it will mark it as done, arguments:
# filename: The name of the file
# task: the task the user wants to mark as done
def done_task(filename: str, task):
    with open("data/" + filename + ".txt", "r+") as f: 
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if line.strip("\n") == task:
                line = line.strip("\n") + " --> Done" + "\n"
            f.write(line)    
        f.truncate()



