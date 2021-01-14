


#This method Creates new tasks, arguments:
# filename: The name of the file
# task: the task the user wants to store

def create_task(filename: str, task: str): 
	with open("data/" + filename + ".txt", "a+") as f: 
		f.write(task + "\n")

def show_tasks(filename: str):
	with open("data/" + filename + ".txt", "r") as f: 
		lines = f.readlines()
		for line in lines:
			print(line)



create_task("test", "Este e um Teste1")
create_task("test", "Este e um Teste2")
create_task("test", "Este e um Teste3")

show_tasks("test")