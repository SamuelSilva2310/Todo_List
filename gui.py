from tkinter import *
import tkinter.messagebox
import file_handler as fh 




#COLORS
BG_RIGHT = "red"
BG_LEFT = "cyan"
FILENAME = "test"


root = Tk()
root.title("To-Do List by @SamuelSilva")
root.geometry('400x300')


def add_task(filename = FILENAME):
	task = entry_task.get()
	fh.create_task(filename, task)

	if task != "":
		listbox_tasks.insert(END, task)
		entry_task.delete(0, END)
	else:
		tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


def load_tasks(filename = FILENAME):
	tasks = fh.get_tasks(FILENAME)
	listbox_tasks.delete(0,END)
	for task in tasks:
		 listbox_tasks.insert(END, task)

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    fh.create_task(filename, task)


#TOP Widgets - This is all widgets that are going to be displayed on the left side


frame_tasks = Frame(root,bg=BG_RIGHT)
frame_tasks.pack()

listbox_tasks = Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=LEFT)

scrollbar_tasks = Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=RIGHT, fill=Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = Entry(root, width=50)
entry_task.pack()

#Here it creates all tasks using the get_tasks method from the sfile (file_handler)
#It will create a label inside the tasks_frame
#each label will contain the text of each line from the lines we get from 




#Bottom Widgets - This is all widgets that are going to be displayed on the rigth side
button_add_task = Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = Button(root, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

button_load_tasks = Button(root, text="Load tasks", width=48, command=load_tasks)
button_load_tasks.pack()

button_save_tasks = Button(root, text="Save tasks", width=48, command=save_tasks)
button_save_tasks.pack()

root.mainloop()
