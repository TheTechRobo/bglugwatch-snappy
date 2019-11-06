# bglugwatch 0.1
# copyright (c) 2019 anthony morassutti
# import necessary modules
import tkinter
from tkinter import Button, Label, Text, messagebox, Menu, ttk, colorchooser
from tkinter import *
main = tkinter.Tk()
menubar = Menu(main)
main.title("BGLUGwatch")
# DECLARING
def hello():
    win = Toplevel()
    win.title('About BGLUG and the program')
    # create child window
    # display message
    message = '''
The Bruce Grey Linux Users Group (BGLUG) was founded in 2000 to bring local Linux users together and to help newcomers to Linux. The group
holds monthly meetings, gives technical presentations, distributes Linux CD-ROMs and hosts a web site, www.bglug.ca, which provides online support.

The Bruce-Grey Linux Users Group is currently centered in Owen Sound, but has members scattered around Bruce and Grey counties. The group is freely open to everyone.

Please see the support section and its sub topics for more information on the various services available.

We gather together for four main reasons:
- advocacy
- education
- support
- socializing

SHORT HISTORY

Bruce Grey Linux Users Group was originally founded by Richard Court in early 2000. Richard Court, Brad Rodriguez, Andrew Howlett and Dan Eriksen have been key members since its creation.

Richard has given up control of BGLUG to the current active maintainer, Dan Eriksen (site admin, LPIC-1 certified). A lot of work is still from the other members of the group, namely Andrew Howlett (meeting
 coordinator, LPIC-1 certified) who started our free CDs service.

Over the last few years we have seen the group grow significantly in size. Nearly everyone has played a role in making the meetings interesting and helping to keep the group going.

The bglug.ca domain was purchased in November 2002. After several months, the forums were added and then eventually our own mailing list.

We are constantly evolving and gladly welcome any constructive feedback and suggestions. If you have any thoughts about the group or the site, please let us know!

BGLUGwatch copyright (c) 2019 Anthony Morassutti. Licensed under the GNU GPLv3. You should have recieved a copy of the license with the program; otherwise go to https://www.gnu.org/licenses/gpl-3.0.en.html
	'''
    Label(win, text=message).pack()
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    Button(win, text='OK', command=win.destroy).pack()
# MENUBAR
# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="About...", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit BGLUGwatch", command=main.quit)
menubar.add_cascade(label="BGLUGwatch", menu=filemenu)
# create another pulldown menu, and add IT to the menu bar
viewmnu = Menu(menubar, tearoff=0)
viewmnu.add_command(label="About...", command=hello)
viewmnu.add_command(label="Articles", command=hello)
viewmnu.add_command(label="Meeting list", command=hello)
viewmnu.add_separator()
viewmnu.add_command(label="Exit BGLUGwatch", command=main.quit)
menubar.add_cascade(label="View", menu=viewmnu)
# display the menu
main.config(menu=menubar)
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
TAB_CONTROL.pack(expand=1, fill="both")
#For tab 1
def moreinfomeeting():
    more = Toplevel()
    more.title('Next meeting -- Info')
    # create child window
    # display message
    message = '''Our December meeting is _th December, 2019 at 7:pm at the United Way Owen Sound.
	Bring your beverage (no alcohol!); Andrew will bring pizza.
	Topic for this meeting: '''
    Label(more, text=message).pack()
ttk.Label(TAB1, text="Meeting December 2019").pack()
ttk.Button(TAB1, text="More info...", command=moreinfomeeting).pack()
#For tab 2
def abtlin():
    abtlin = Toplevel()
    abtlin.title('About BGLUG and the program')
    variablex = '''GNU/Linux ("Linux") is a clone of the operating system Unix. It was originally created by Linus Torvalds with the assistance of thousands of volunteer developers around the world. It is distributed under the GNU 
General Public License which means the source code is freely available to everyone. Linux has powered much of the Internet for years, and is now available with many applications for "desktop" computer users.'''
    ttk.Label(abtlin, text=variablex).pack()
ttk.Button(TAB2, text="About Linux", command=abtlin).pack()
# MESSAGES
# show message on launch
messagebox.showinfo("Welcome!", "Next meeting: November __ 7pm United Way")
main.mainloop()