from tkinter import *





#COLORS
BG_RIGHT = "red"
BG_LEFT = "cyan"



root = Tk()
root.title="To do List app"
root.geometry('400x300')




#create containers
top_frame = Frame(root)
bottom_frame = Frame(root)


top_frame.pack()
bottom_frame.pack()

#Left Widgets - This is all widgets that are going to be displayed on the left side
title_top_lbl = Label(top_frame,text = "TASKS",font=("Arial Bold",16))
title_top_lbl.grid(row=0,column=0,columnspan=2,pady=20)

tasks_frame = Frame(top_frame)
tasks_frame.grid(row=1,column=0)


#Here it creates al
for i in range(5):
	lbl = Label(tasks_frame, text= f"This is a Task{i}").grid(row=i,column=0)
#Right Widgets - This is all widgets that are going to be displayed on the rigth side

btns_frame = Frame(bottom_frame)
btns_frame.grid(row =1 , column=0,padx=20, pady=20)

# title_right_lbl = Label(right_frame,text = "TO DO LIST APP",font=("Arial Bold",16))
# title_right_lbl.grid(row=0,column=0,columnspan=2,pady=20)



create_btn = Button(btns_frame, text="Create Task")
create_btn.grid(row=1,column=0,padx=5)

delete_btn = Button(btns_frame, text="Delete Task")
delete_btn.grid(row=1,column=1,padx=5)

root.mainloop()
