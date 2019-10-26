import tkinter
from tkinter import Button, Label, Text, messagebox, Menu
main = tkinter.Tk()
messagebox.showinfo("Welcome!", "to the official BGLUG program")
menubar = Menu(main)
menubar.add_command(label="Quit!", command=main.quit)
# display the menu
main.config(menu=menubar)
main.mainloop()