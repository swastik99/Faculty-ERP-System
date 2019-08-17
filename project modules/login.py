from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
import mysql.connector
import tkinter.messagebox

rootl = tk.ThemedTk()
rootl.get_themes()
rootl.set_theme("radiance")

rootl.title("Module Registration System")
rootl.iconbitmap(r'images/upes.ico')

mailL = StringVar()
pwordL = StringVar()

def clear_entry(event, entry):
    entry.delete(0, END)

def log():
    emailL = mailL.get()
    passwordL = pwordL.get()
    conn = mysql.connector.connect(host='localhost',user='root', password='',db='erp')
    def valid_mail(emailL):
        y = re.findall('@([^ ]*)',emailL)
        domain = y[0]
        if domain == "ddn.upes.ac.in":
            return True
        else:
            return False

    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS Faculty_Register(FirstName VARCHAR(50),LastName VARCHAR(50),Email VARCHAR(100), Password VARCHAR(50))')
    if emailL != '' and valid_mail(emailL):
        if passwordL != '':
            try:
                cur.execute(
                    'SELECT Password FROM Faculty_Register WHERE Email = %s',
                    (emailL,))
                pas = cur.fetchone()
                if pas[0] == passwordL:
                    cur.execute('SELECT FirstName FROM Faculty_Register WHERE Email = %s',
                    (emailL,))
                    user = cur.fetchone()
                    tkinter.messagebox.showinfo('Status',
                                                user[0]+', you are successfully logged in')
                else:
                    tkinter.messagebox.showinfo('Status',
                                                'Incorrect Password, Please try again...')
            except TypeError:
                tkinter.messagebox.showinfo('Status',
                                            'You are not registered\nPlease register yourself first...')
        else:
            tkinter.messagebox.showerror('Error', 'Please fill the password carefully\nMinnimum Length of 8 charachters!!!')
    else:
        tkinter.messagebox.showerror('Error', 'Please enter a valid email!!!\nDomain should be ddn.upes.ac.in')

AddBtn = ttk.Button(rootl, text = "LOGIN", width = 20, command = log)
AddBtn.pack(side = BOTTOM, pady = 10)

bottomframe = Frame(rootl)
bottomframe.pack(side = BOTTOM)

luser= PhotoImage(file="images/loguser.png")
labelphoto = Label(rootl,image = luser)
labelphoto.pack(pady = 20, padx = 150)

l1 = Label(bottomframe, text="Email ID",  font="fixedsys 10 normal")
l1.grid(row = 0, column = 0,padx = 20)
e1 = ttk.Entry(bottomframe, textvar=mailL, width=30)
placeholder_text = 'EMAIL ID'
e1.insert(0, placeholder_text)
e1.bind("<Button-1>", lambda event: clear_entry(event, e1))
e1.grid(row = 0, column = 1,padx = 20)

bullet = "\u2022" #specifies bullet character

l2 = Label(bottomframe, text="Password",  font="fixedsys 10 normal")
l2.grid(row = 1, column = 0,pady = 10,padx = 20)
e2 = ttk.Entry(bottomframe, show=bullet, textvar=pwordL, width=30)
placeholder_text = '12345678'
e2.insert(0, placeholder_text)
e2.bind("<Button-2>", lambda event: clear_entry(event, e2))
e2.grid(row = 1, column = 1,pady = 10,padx = 20)

rootl.mainloop()