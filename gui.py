import tkinter as tk

root = tk.Tk()

left_Frame = tk.Frame (root, height=300, width = 300, bg = "blue").pack(side = tk.LEFT, fill = "both", expand = True)
right_Frame = tk.Frame (root, height=300, width = 300, bg = "red").pack(side = tk.LEFT, fill = "both", expand = True)

root.mainloop()
