#To do List Main File
# Autor: Samuel Silva
# Date: 14/01/2021
# App: To do List
 
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

	print(menu)

	return action_Menu(int(input()))


def action_Menu(action : int):

	if action == 1:
		pass
	elif action == 2:
		pass
	elif action == 3:
	else: 
		pass




get_Menu()

