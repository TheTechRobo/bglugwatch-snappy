# bglugwatch 0.2.3
# copyright (c) 2019-2020 ittussarom retals mail ynohtna
# BGLUGwatch is licensed under the GNU GPLv3 or later, a copyleft license.
# copyleft states that it is illegal to switch to a different license without the explicit permission of TheTechRobo
# END OF NOTICES
# import necessary modules
import tkinter
from tkinter import Button, Label, Text, Menu, ttk
from tkinter import messagebox as msg
from tkinter import *
import subprocess
from sys import exit
import webbrowser
# set up window
main = tkinter.Tk()
menubar = Menu(main)
main.title("BGLUGwatch")
# DECLARING
def uc(): #source stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output/9266901#9266901
    msg.showinfo("Attempting to update...", "Please wait while git does its job.")
    output = subprocess.Popen(["git pull"],stdout=subprocess.PIPE, shell=True)
    response = output.communicate()
    if response == (b'Already up to date.\n', None):
        print("Already up to date.")
        msg.showinfo("Already up to date.", "You can now use BGLUGwatch freely!")
    else:
        msg.showinfo("Updated!", "BGLUGwatch will now exit, please restart it.")
        exit()
def clist(winname):
    scrollbar = Scrollbar(winname) #add scrollbar
    scrollbar.pack(side=RIGHT, fill=Y) #pack scrollbar
    mylist = Listbox(winname, yscrollcommand=scrollbar.set)#create list
    return mylist
def hello():
    win = Toplevel()
    win.title('About BGLUG and the program')
    # create child window
    # display message
    mylist = clist(win)
    def insert(string):
        mylist.insert(END, string)
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
    insert("BGLUGwatch 0.2.3, copyright (c) Ittussarom Retals Mail Ynohtna. Licensed under the GNU GPLv3.")
    insert("Find it on GitHub at: www.github.com/thetechrobo/bglugwatch")
    insert("Thanks for using!")
    mylist.pack(fill = BOTH)
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    Button(win, text='OK', command=win.destroy).pack()
    winname.minsize(1200, 100)
def ShowMessageOne(): #Message one (Jeff L)
    print("Showing message one, if anyone's listening......")
    m1 = Toplevel() #create window
    m1.title("Message 1")
    mylist = clist(m1)
    def insert(string):
        mylist.insert(END, string)
    insert("Message from LP")
    insert("")
    insert("I just got the word 'All LUG meetings at the United Way are cancelled until further notice' Chris.")
    insert("Sent from ProtonMail <protonmail.ch>, encrypted email based in Switzerland.")
    insert("")
    insert("Reply from TtR")
    insert("")
    insert("Well, I'm sad, but it was bound to happen.")
    insert("Sent from TtR's iPhone 4")
    insert("")
    insert("Reply from Brad Rodriguez")
    insert("")
    insert("I have updated the web page to show this.")
    insert("")
    insert("- Brad")
    insert("")
    insert("Reply from Logan Streondj")
    insert("How about we meet on Jitsi (open-source video chat)")
    insert("https://meet.jit.si/bglug")
    Button(m1, text="OK", command=m1.destroy).pack()
    m1.minsize(1000, 100)
    mylist.pack(fill=BOTH)
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
def contrib():
    webbrowser.open("https://github.com/thetechrobo/bglugwatch", new=1) # SOURCE: gist.github.com/RandomResourceWeb/93e887facdb98937ab5d260d1a0df270
# Tabs (source www.djangocentral.com/creating-tabbed-widget-with-python-for-gui-application/)
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
    # create child window
    more = Toplevel()
    more.title('No meeting in April')
    # display message
    message = '''There is currently No Meeting in April due to the COVID-19 pandemic.
    Stay safe!'''
    Label(more, text=message).pack()
    Button(more, text="OK", command=more.destroy)
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
ttk.Label(TAB3, text="Newest Mail on the Mailing List").pack()
ttk.Label(TAB3, text='''SUBJECT: All LUG Meetings are Cancelled until further notice !
I just got the word...''').pack()
ttk.Button(TAB3, text="Read", command=ShowMessageOne).pack()
ttk.Label(TAB3, text='''Under Construction''').pack()
ttk.Button(TAB3, text="Read", command=showMessageTwo).pack()
ttk.Label(TAB3, text='''
For messages direct to your mailbox, go to http://bglug.ca/mailman/listinfo/group_bglug.ca and sign
up for the mailing list!''').pack()
#TAB4
ttk.Button(TAB4, text="Update cache", command=uc).pack()
ttk.Label(TAB4, text="This button will update the cache of BGLUGwatch. It's helpful if you aren't using the snap-store,\nbut otherwise there is no point whatsoever.\nIf you don't have git installed, this will fail. So please, make sure git is installed.").pack()
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
utilmnu = Menu(menubar, tearoff=0)
utilmnu.add_command(label="Update BGLUGwatch", command=uc)
utilmnu.add_command(label="Contribute!", command=contrib)
menubar.add_cascade(label="Utilities", menu=utilmnu)
# display the menu
main.config(menu=menubar)
# show message on launch
msg.showerror("No meeting in April, don't even try.", "There is no meeting in April due to the COVID-19 pandemic, staying safe is more important than computers!")
main.mainloop()
