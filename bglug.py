import tkinter
from tkinter import Button, Label, Text, messagebox, Menu
main = tkinter.Tk()
messagebox.showinfo("Welcome!", "to the official BGLUG program")
menubar = Menu(main)
def hello():
	print("salut")
# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=main.quit)
menubar.add_cascade(label="File", menu=filemenu)
# display the menu
main.config(menu=menubar)
main.mainloop()