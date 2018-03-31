
# -*- mode: python ; coding: utf-8 -*-
# © 2018 Venkataramana Pulugari <pvrreddy155@gmail.com>
# License: MIT ; https://opensource.org/licenses/MIT

"""
A simple login with alert message to your phone when invalid access
"""


from Tkinter import *
import sqlite3
import time
import datetime
import tkMessageBox
import way2sms

def power():
        pow = Tk()
        pow.overrideredirect(1)
        w = 200 # width for the Tk root
        h = 80 # height for the Tk root
        
        # get screen width and height
        ws = pow.winfo_screenwidth() # width of the screen
        hs = pow.winfo_screenheight() # height of the screen
        
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2)  - (h/2)
        
        # set the dimensions of the screen 
        # and where it is placed
        pow.geometry('%dx%d+%d+%d' % (w, h, x, y))
        pow.attributes('-alpha', 0.6)
        pow.configure(background='black')
        lbldate = Label(pow, text = 'Coded By', foreground = 'white', background='black', font = ('arial', 10, 'bold'))
        lbldate.pack(side = TOP)
        lbldat = Label(pow, text = 'Venkataramana Pulugari', foreground = 'red', background='black', font = ('arial', 12, 'bold'))
        lbldat.pack(side = TOP)
        lblda = Label(pow, text = 'pvrreddy155@gmail.com', foreground = 'red', background='black', font = ('arial', 10, 'bold'))
        lblda.pack(side = TOP)
        pow.after(5000, pow.destroy)
        pow.mainloop()
        

db = sqlite3.connect('db_file.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Login(username TEXT UNIQUE, password TEXT UNIQUE)''')

############# Set your login Username and Password here ###############################

cursor.execute('''INSERT or IGNORE INTO Login(username, password) VALUES(?,?)''', ('your_username', 'your_password'))
db.commit()
db.close()
db = sqlite3.connect('db_file.db')
cursor = db.cursor()
cursor.execute('SELECT username FROM Login')
login1 = cursor.fetchone()
login1 = [str(login1[0])]
cursor.execute('SELECT password FROM Login')
login2 = cursor.fetchone()
login2 = [str(login2[0])]
    
def access():
    if(username.get() == login1[0]) and (password.get() == login2[0]):
        root.destroy()
        power()
    else:    
        rootm = Tk()
        rootm.focus()
        rootm.overrideredirect(1)
        w = 300 # width for the Tk root
        h = 100 # height for the Tk root
        
        # get screen width and height
        ws = rootm.winfo_screenwidth() # width of the screen
        hs = rootm.winfo_screenheight() # height of the screen
        
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2)  - (h/2)
        
        # set the dimensions of the screen 
        # and where it is placed
        rootm.geometry('%dx%d+%d+%d' % (w, h, x, y))
        rootm.attributes('-alpha', 0.6)
        rootm.configure(background='black')
        lbldate = Label(rootm, text = 'Invalid Login', foreground = 'white', background='black', font = ('arial', 20, 'bold'))
        lbldate.pack(side = TOP)

        ################ This is the invisible close button. To close click at the bottom middle without login ###############
        ################ Remove this if u dont need ##########################################################################

        close = Button(rootm, text = "close", command = lambda: rootm.destroy(), border = '5', background = 'black', foreground = 'white', activebackground = 'black', highlightcolor = 'black')
        close.focus()
        close.bind('<Return>', lambda _: rootm.destroy())
        close.pack(side = TOP)

        ############### Set your way2sms login Number and Password here

        q=way2sms.sms("99XXXXXXXX","your_way2sms_password")

        ############### Your message here and phone number to send the message to ############################## 

        q.send( '99XXXXXXXX', 'Someone is trying to access' )  
        q.msgSentToday()
        q.logout()
        username.set("")
        password.set("")
        e1Username.focus()
        return
    
def exit():
    root.destroy()
    power()

root = Tk()
root.overrideredirect(1)
w = 800 # width for the Tk root
h = 650 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2)  - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (ws, hs, 0, 0))
root.attributes('-alpha', 0.9)
root.configure(background='black')

views = IntVar()
username = StringVar()
password = StringVar()
date = StringVar()
date.set(time.strftime("%d/%m/%Y"))               

def load():
    db = sqlite3.connect('itsmepvr.db')
    cursor = db.cursor()
    #cursor.execute('''DROP TABLE Id''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Views(views INTEGER)''')
    cursor.execute('''SELECT views FROM views''')
    id = cursor.fetchone()
    if(id == None):
        id = str(0)        
        cursor.execute('''INSERT INTO Views(views) VALUES(?)''', (id,))
    else:
        id = str(int(id[0]) + 1)   
    views.set(id)       
    cursor.execute("UPDATE Views SET views = ?",(id,))
    cursor.execute('''SELECT views FROM Views''')
    db.commit()
    db.close()

close = Button(root, text = "", width='20', command = exit, border = '0', background = 'black', foreground = 'white', activebackground = 'black', highlightcolor = 'black')
close.pack(side = BOTTOM, anchor='s')

root1 = Frame(root, background='black')
root1.pack(side = LEFT, anchor = 'n' )

lbldate = Label(root1, textvariable = date, foreground = 'white', background='black', font = ('arial', 12, 'bold'))
lbldate.pack(side = TOP)

root2 = Frame(root, background='black')
root2.pack(side = RIGHT, anchor = 'n')
lblviewstxt = Label(root2, text = "View Counts", foreground = 'white', background='black', font = ('Catull', 12, 'bold'))
lblviewstxt.grid(row = 0, column = 0)
lblviews = Label(root2, textvariable = views, foreground = 'white', background='black', font = ('Catull', 12, 'bold'))
lblviews.grid(row = 0, column = 1)

root3 = Frame(root, background='black')
root3.pack(side = TOP, padx = (380,0), pady = (300,0), anchor = 'w')
lb1Username = Label(root3, font = ('Helvetica', 12, 'bold'), text = "UserName", bd = 20, background = 'black', foreground = 'white')
lb1Username.grid(row = 0, column = 0)
e1Username = Entry(root3, insertbackground = 'white', textvariable = username, bd=0, font = ('arial',12,'bold'), width = 20, background = 'black', foreground = 'white')
e1Username.focus()
e1Username.grid(row = 0, column = 1)
lb1Password = Label(root3, font = ('Helvetica', 12, 'bold'), text = "Password", bd = 20, background = 'black', foreground = 'white')
lb1Password.grid(row = 1, column = 0)
e1Password = Entry(root3, show = '*', insertbackground = 'white', textvariable = password, bd=0, font = ('arial',12,'bold'), width = 20, foreground = 'white', background = 'black')
e1Password.bind('<Return>', lambda _: access())
e1Password.grid(row = 1, column = 1)
root4 = Frame(root, background='black')
root4.pack(side = TOP)
Access = Button(root4, text = "Access", command = access, border = '0.5', background = 'black', foreground = 'white', font = ('arial',12,'bold'), activebackground = 'black', highlightcolor = 'black')
Access.pack(side = TOP, pady = (20,0))

root.winfo_exists()
   
load()
root.mainloop()
 