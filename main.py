#To do List Main File
# Autor: Samuel Silva
# Date: 14/01/2021
# App: To do List
import file_handler as fh 

MENU = """
	 ----------------
	       MENU
	 -----------------

	 1 -- Create
	 2 -- Delete
	 3 -- List
	 4 -- Check as Done

	 -----------------"""

def get_Menu(menu = MENU): 

	while True: 
		print(menu)

		action = int(input("Insert action -> "))

		if action == 1:
			fh.create_task("test", "Task Test")
		elif action == 2:
			fh.delete_task("test", "Task Test")
		elif action == 3:
			fh.show_task("test")
		elif action == 4:
			fh.done_task("test","Task Test")
		elif action == 5: 
			break
		else: 
			print("Please Insert a valid action")

get_Menu()

