import tkinter as tk
from tkinter import *
from pathlib import Path
import time

root = Tk()
root.title('File Sorter GUI')

frame = Frame(root, padx=10, pady=10)
frame.pack()

# ------------------------------
# functions
# ------------------------------

def get_input():
    directory = e1.get()
    print(f"Directory to sort: {directory}") # testing purpose
    



files = "test file 1.txt"
v = tk.IntVar()

# ------------------------------
# GUI/Main Components
# ------------------------------

welcome_label = Label(
    frame,
    text = "Welcome to the File Sorter Program! \nCan you enter the directory you want to sort?",
    font = ("Helvetica", 12)
)
welcome_label.grid(row=0, column=0, columnspan=2, pady=(10))


Label(frame, text="Directory:").grid(row=1, column=0, sticky="e", pady=5)
e1 = Entry(frame, width=40)
e1.grid(row=1, column=1, pady=5)

p = Path(e1.get())



def view_folders():
    for item in p.iterdir():
        print(item)
        time.sleep(0.2)

Button(frame, text="Submit", command=get_input).grid(row=2, column=0, columnspan=2)

scrollbar = Scrollbar(frame)
scrollbar.grid(row=3, column=3, sticky="ns", pady=10)
mylist = Listbox(frame, yscrollcommand=scrollbar.set, width=50, height=15)
mylist.grid(row=3, column=0, columnspan=2, pady=10)

tk.Radiobutton(root, text="View Files", command=view_folders, variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(root, text="Sort Files", variable=v, value=2).pack(anchor=tk.W)



root.mainloop()