'''
BGLUGwatch is currently OUTDATED.
Do not use until v.0.2-stable!
Every version before that is purely for testing purposes.
'''
# bglugwatch 0.0.1
# copyright (c) 2019-2020 ittussarom retals mail ynohtna
# BGLUGwatch is licensed under the GNU GPLv3 or later, a copyleft license.
# copyleft states that it is illegal to switch from GNU GPLv3 or later without the explicit permission of Anthony Morassutti (TheTechRobo)
# ***END OF FILE NOTICES***
# import necessary modules
import tkinter
from tkinter import Button, Label, Text, messagebox, Menu, ttk, colorchooser
from tkinter import *
from runpy import run_path
from sys import exit
# set up window
main = tkinter.Tk()
menubar = Menu(main)
main.title("BGLUGwatch")
# DECLARING
def hello():
    win = Toplevel()

    win.title('About BGLUG and the program')
    # create child window
    # display message
    scrollbar = Scrollbar(win)
    scrollbar.pack( side = RIGHT, fill = Y )
    def insert(string):
        mylist.insert(END, string)
    mylist = Listbox(win, yscrollcommand = scrollbar.set ) #create list
    insert("The Bruce Grey Linux Users Group (BGLUG) was founded in 2000 to bring local Linux users together and to help newcomers to Linux.")
    insert("The group holds monthly meetings, gives technical presentations, distributes Linux CD-ROMs and hosts a web site, www.bglug.ca, which provides online support.")
    insert("The Bruce-Grey Linux Users Group is currently centered in Owen Sound, but has members scattered around Bruce and Grey counties. The group is freely open to everyone.")
    insert("We gather together for four main reasons:")
    insert("advocacy, education, support, and socializing.")
    insert("")
    insert("Bruce Grey Linux User's Group was originally founded by Richard Court in early 2000. Richard Court, Brad Rodriguez, Andrew Howlett and Dan Eriksen have been key members since its creation.")
    insert("Richard has given up control of BGLUG to the current active maintainer, Dan Eriksen (site admin, LPIC-1 certified).")
    insert("A lot of work is still from the other members of the group, namely Andrew Howlett (meeting coordinator, LPIC-1 certified) who started our free CDs service.")
    insert("Over the last few years we have seen the group grow significantly in size. Nearly everyone has played a role in making the meetings interesting")
    insert("and helping to keep the group going.")
    insert("The bglug.ca domain was purchased in November 2002. After several months, the forums were added and then eventually our own mailing list.")
    insert("We are constantly evolving and gladly welcome any constructive feedback and suggestions. If you have any thoughts about the group, please let us know!")
    insert("")
    insert("BGLUGwatch 0.0.1, copyright (c) Ittussarom Retals Mail Ynohtna. Licensed under the GNU GPLv3.")
    insert("Find it on GitHub at: www.github.com/thetechrobo/bglugwatch")
    insert("Thanks for using!")
    mylist.pack(fill = BOTH)
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    Button(win, text='OK', command=win.destroy).pack()
    win.minsize(1200, 100)
def ShowMessageOne(): #Message one (Jeff L)
    print("Showing message one, if anyone's listening......")
    content = '''
    Under Construction!'''
    m1 = Toplevel()
    m1.title(':(')
    Label(m1, text=content).pack()
def showMessageTwo():
    print("Showing messages...")
    content = '''Under Construction'''
    m2 = Toplevel()
    m2.title(':(')
    Label(m2, text=content).pack()
    #Label(m2, text='''
    #[REPLY]
    #''').pack()
    Label(m2, text=contentReply).pack()
def subshelp():
    win = Toplevel()
    win.title('Under Construction')
    Label(win, text="Under construction").pack()
# Tabs (src https://djangocentral.com/creating-tabbed-widget-with-python-for-gui-application/)
#Create Tab Control
TAB_CONTROL = ttk.Notebook(main)
#Tab1
TAB1 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text='Next meeting')
#Tab2
TAB2 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB2, text='Articles')
#Tab3
TAB3 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB3, text='Mailing list')
#TAB4
TAB4 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB4, text='Update cache')
TAB_CONTROL.pack(expand=1, fill="both")
#For tab 1
def moreinfomeeting():
    more = Toplevel()
    more.title('No meeting in April')
    # create child window
    # display message
    message = '''There is currently No Meeting in April due to the COVID-19 pandemic.
    Stay safe!'''
    Label(more, text=message).pack()
    Button(more, text="O.K.", command=more.destroy)
ttk.Label(TAB1, text="(null)").pack()
ttk.Button(TAB1, text="More info...", command=moreinfomeeting).pack()
#For tab 2
def abtlin():
    abtlin = Toplevel()
    abtlin.title('About GNU/Linux')
    linux = '''GNU/Linux ("Linux") is a clone of the operating system Unix. It was originally created by Linus Torvalds with the assistance of
    thousands of volunteer developers around the world. It is distributed under the GNU General Public License which means the source code is
    freely available to everyone. Linux has powered much of the Internet for years, and is now available with many applications for "desktop" computer users.'''
    ttk.Label(abtlin, text=linux).pack()
ttk.Button(TAB2, text="About Linux", command=abtlin).pack()
#For tab3.
ttk.Label(TAB3, text="3 NEWEST MAIL ON MAILING LIST").pack()
ttk.Label(TAB3, text='''
Under construction''').pack()
ttk.Button(TAB3, text="Read", command=ShowMessageOne).pack()
ttk.Label(TAB3, text='''Under Construction''').pack()
ttk.Button(TAB3, text="Read", command=showMessageTwo).pack()
ttk.Label(TAB3, text='''
For messages direct to your mailbox, go to http://bglug.ca/mailman/listinfo/group_bglug.ca and sign
up for the mailing list!''').pack()
#TAB4
def uc():
    try:
        run_path(path_name="check4Update.py")
    except:
        exit("An error occured!")
ttk.Button(TAB4, text="Update cache", command=uc).pack()
ttk.Label(TAB4, text="This button will update the cache of BGLUGwatch. It's helpful if you aren't using the snap-store,\nbut otherwise there is no point whatsoever.").pack()
# MENUBAR
# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="About...", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit BGLUGwatch", command=main.quit)
menubar.add_cascade(label="BGLUGwatch", menu=filemenu)
# create another pulldown menu, and add IT to the menu bar
viewmnu = Menu(menubar, tearoff=0)
viewmnu.add_command(label="About box", command=hello)
viewmnu.add_command(label="Next meeting", command=moreinfomeeting)
viewmnu.add_separator()
viewmnu.add_command(label="Exit BGLUGwatch", command=main.quit)
menubar.add_cascade(label="View", menu=viewmnu)
# display the menu
main.config(menu=menubar)
# show message on launch
messagebox.showerror("No meeting in April, don't even try.", "There is no meeting in April due to the COVID-19 pandemic, staying safe is more important than computers!")
main.mainloop()
