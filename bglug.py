# bglugwatch 0.1
# copyright (c) 2019 anthony morassutti
# BGLUGwatch is licensed under the GNU GPLv3
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

============

BGLUGwatch is designed to contain info about BGLUG. It contains new messages from the mailing list, articles, and more -- all offline!
BGLUGwatch is completely opensource; find it on GitHub https://github.com/TheTechRobo/bglugwatch
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
    abtlin.title('About GNU/Linux')
    variablex = '''GNU/Linux ("Linux") is a clone of the operating system Unix. It was originally created by Linus Torvalds with the assistance of thousands of volunteer developers around the world. It is distributed under the GNU 
General Public License which means the source code is freely available to everyone. Linux has powered much of the Internet for years, and is now available with many applications for "desktop" computer users.'''
    ttk.Label(abtlin, text=variablex).pack()
ttk.Button(TAB2, text="About Linux", command=abtlin).pack()
#For tab3.
ttk.Label(TAB3, text="3 NEWEST MAIL ON MAILING LIST").pack()
ttk.Label(TAB3, text='''
1. From: Jeff L
Subject: Win 10 antispyware
"Just heard..."

2. [THREAD] From: Peter and Brad Rodriguez
Subject: [Bglug] Phishing attempt? Virus payload via MS Office macro?
(ORIGIN) "Hi all:...
(REPLY) "Yes, that"''').pack()
def ShowMessageOne():#Message one (Jeff L)
    print("Showing message one, if anyone's listening......")
    content = '''
	Just heard about this thought people might be interested in.

	Free antispy tool for Windows 10
	https://www.oo-software.com/en/shutup10#

	Jeff

	_______________________________________________
	Group mailing list
	Group@bglug.ca
	http://bglug.ca/mailman/listinfo/group_bglug.ca'''
    m1 = Toplevel()
    m1.title('Win 10 antispyware')
    Label(m1, text=content).pack()
def showMessageTwo():
    print("Showing messages...")
    content = '''
	Hi all:

	Earlier this week I received and email, ostensibly from 'Canada Post' claiming there was a missed package delivery, presumably at my home. It had the logos etc and it was addressed to me, pjr@bmts.com. But the tracking number in the email was blank.

	There was no record at the local post office of such a package nor was a 'door hanger' left on our front door to signify someone from CP had tried to deliver a package.

	The email included an attachment which, when I tried to open it, was gibberish - reminded me of a postscript file. It had a filename xxx.doc. The instructions at the top of the page said I should open it with MS Office as it was encrypted. I should have been suspicious immediately as there was no tracking number on the email. The alarm bells did not ring!

	As I do not have MS Office, I could not open the file.

	I got much more suspicious when I tried to forward it, to see if there was a package as the email also had others in the headers. The outgoing email was returned to me by the mail agent because

	"

	host mail.xxxxx.ca[149.248.52.47] said: 550-This message
	    contains a virus or other harmful content 550 (Doc.Dropper.Agent-7400026-0)
	    (in reply to end of DATA command)"

	In summary then, perhaps this was some kind of scam, a phishing attempt, or perhaps opening the attachment to 'decrypt' it would install a virus. MS Office does macros, doesn't it?

	For your information, as some would say.

	Peter


	-- 
	Two things are infinite: the universe and human stupidity; and I'm not sure about the the universe. -  Albert Einstein


	_______________________________________________
	Group mailing list
	Group@bglug.ca
	http://bglug.ca/mailman/listinfo/group_bglug.ca'''
    contentReply = '''
	Yes, that was certainly malware.  .doc files are a not-infrequent vector
	for attacks.  Many Windows users are vulnerable; I don't know if
	Linux OpenOffice tries to execute macros.

	In general, I'm suspicious of any unsolicited email that instructs me
	to "open the attached document" (or zip archive).  I've never had an
	email from UPS or FedEx or Canada Post or *any* legitimate sender come
	that way.  When I see such an email, I delete immediately.

	- Brad
	-- 
	brad@bradrodriguez.com

	_______________________________________________
	Group mailing list
	Group@bglug.ca
	http://bglug.ca/mailman/listinfo/group_bglug.ca'''
    m2 = Toplevel()
    m2.title('[Bglug] Phishing attempt? Virus payload via MS Office macro')
    Label(m2, text=content)
    Label(m2, text='''
	[REPLY]
	''')
    Label(m2, text=contentReply)
    Label()
ttk.Button(TAB3, text="Read", command=ShowMessageOne).pack()
ttk.Label(TAB3, text='''
For messages direct to your mailbox, go to http://bglug.ca/mailman/listinfo/group_bglug.ca and sign
up for the mailing list!''').pack()
#For messages direct to your mailbox, sign up for the mailing list!
#Send mail to group-request@bglug.ca with following format (do not add subject):
 # subscribe [password] [digest|nodigest] [address=<address>]
  #You can also send mail to group-request@bglug.ca with following format (do not add subject):
  #subscribe [password] [digest|nodigest] [address=<address>]''').pack()
subhelp = '''Subscribe to this mailing list.  Your password must be given to
       unsubscribe or change your options, but if you omit the password, one
       will be generated for you.  You may be periodically reminded of your
       password.

       The next argument may be either: `nodigest' or `digest' (no quotes!).
       If you wish to subscribe an address other than the address you sent
       this request from, you may specify `address=<address>' (no brackets
       around the email address, and no quotes!)'''
def subshelp():
    win = Toplevel()
    win.title('Subscribing without the World Wide Web')
    Label(win, text=subhelp).pack()
ttk.Button(TAB3, text="Subscribing without a Web browser", command=subshelp)
# MESSAGES
# show message on launch
messagebox.showinfo("Welcome!", "Next meeting: December __ 7pm United Way")
main.mainloop()