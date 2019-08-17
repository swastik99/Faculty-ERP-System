from tkinter import *
import datetime
import re
import time
import tkinter.messagebox
from tkinter import ttk
from ttkthemes import themed_tk as tk
import mysql.connector

rootup = tk.ThemedTk()
rootup.get_themes()
rootup.set_theme("radiance")

rootup.title("Module Registration System")
rootup.iconbitmap(r'images/upes.ico')

playlist = []
fullname = 'Ankit Vishnoi'

ModuleName = StringVar()
Platform = StringVar()
Date = StringVar()
link = StringVar()


def add_to_playlist(module):
    index = 0
    for i in range(0, len(module)):
        playlistbox.insert(index, module[i][1])
        playlist.insert(index, module[i][1])
        playlistbox.pack()
        index += 1


def show_data():
    global mod
    global selected_mod
    selected_mod = playlistbox.curselection()
    selected_mod = int(selected_mod[0])
    mod = playlist[selected_mod]
    conn = mysql.connector.connect(host='localhost', user='root', password='', db='erp')
    cur = conn.cursor()
    cur.execute('SELECT * from Faculty_Module where Faculty = %s and Module_Name = %s', (fullname, mod,))
    data = cur.fetchone()

    label_1['text'] = "Module Name : "
    label_2['text'] = "Platform : "
    label_3['text'] = "Date of Launching: "
    label_4['text'] = "Link of Module : "

    entry_1 = ttk.Entry(rightframe, textvar=ModuleName, width=40)
    entry_1.grid(row=0, column=1, pady=15, padx=30)
    entry_1.insert(0, data[1])

    list = ['', 'E-PG-Pathshala', 'CEC(Under Graduate) ', 'SWAYAM', 'MOOCs platform',
            'NPTEL/NMEICT/any other Government initiatives'];
    droplist = ttk.OptionMenu(rightframe, Platform, *list)
    droplist.config(width=28)
    droplist.grid(row=1, column=1, pady=15, padx=30)
    Platform.set(data[2])

    entry_3 = ttk.Entry(rightframe, textvar=Date, width=40)
    entry_3.grid(row=2, column=1, pady=15, padx=30)
    entry_3.insert(0, data[3])

    entry_4 = Entry(rightframe, textvar=link, width=40)
    entry_4.grid(row=3, column=1, pady=15, padx=30)
    entry_4.insert(0, data[4])

    upbtn['command'] = up_data

def up_data():
    conn = mysql.connector.connect(host='localhost', user='root', password='', db='erp')
    cur = conn.cursor()
    Module = ModuleName.get()
    platform = Platform.get()
    date = Date.get()
    doclink = link.get()
    datestring = str(date)

    def valid_date(datestring):
        try:
            mat = re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$', datestring)
            if mat is not None:
                datetime.datetime(*(map(int, mat.groups()[-1::-1])))
                return True
        except ValueError:
            pass
        return False

    if Module != '':
        if platform != '':
            if date != '' and valid_date(datestring):
                if doclink != '':
                    cur.execute(
                        'UPDATE Faculty_Module SET Module_Name = %s, Platform = %s, Launch_Date = %s, Link = %s WHERE Faculty = %s and Module_Name = %s',
                        (Module, platform, date, doclink, fullname, mod,))
                    conn.commit()
                    statusbar['text'] = fullname + ", " + mod + " module has been updated successfully"
                    tkinter.messagebox.showinfo('Status',
                                                'Record Updated Succesfully\nFaculty Name : ' +
                                                    fullname + '\nModule Name : ' + str(
                                                    Module) + '\nPlatform on which module is developed : ' + str(
                                                    platform) + '\nDate of Launching : ' + str(
                                                    date) + '\nLink for the module :' + str(
                                                    doclink))
                    rootup.destroy()

                else:
                    tkinter.messagebox.showerror('Link Error', 'Please fill the Link of the document!!!')
            else:
                tkinter.messagebox.showerror('Date Error',
                                             'Please fill the valid date\nFormat : DD/MM/YYYY or DD-MM-YYYY!!!')
        else:
            tkinter.messagebox.showerror('Platform not found Error', 'Please select a platform carefully!!!')
    else:
        tkinter.messagebox.showerror('Module Error', 'Hey! Did you forget your Module name?')

def cancel():
    rootup.destroy()


statusbar = ttk.Label(rootup, text="Ready to add a new module!! Lets go...", relief=SUNKEN, anchor=W,
                      font="Times 10 italic")
statusbar.pack(side=BOTTOM, fill=X)

lframe = Frame(rootup)
lframe.pack(side=LEFT, pady=30, padx=10)

rframe = Frame(rootup)
rframe.pack(pady=30)

lbottomframe = Frame(lframe)
lbottomframe.pack(side=BOTTOM)

rbottomframe = Frame(rframe)
rbottomframe.pack(side=BOTTOM)

leftframe = Frame(rframe)
leftframe.pack(side=LEFT)

rightframe = Frame(rframe)
rightframe.pack()

playlistbox = Listbox(lframe)
playlistbox.pack(pady=10)

showbtn = ttk.Button(lbottomframe, text='SHOW DETAILS', width=20, command=show_data)
showbtn.pack(pady=10)

upbtn = ttk.Button(rbottomframe, text='SAVE', width=20)
upbtn.grid(row=0, column=0, pady=10)

cancelbtn = ttk.Button(rbottomframe, text='CANCEL', width=20, command=cancel)
cancelbtn.grid(row=0, column=1, padx=50, pady=10)

label_1 = Label(leftframe, font="fixedsys 10 normal")
label_1.grid(row=0, column=0, pady=15, padx=10)

label_2 = Label(leftframe, font="fixedsys 10 normal")
label_2.grid(row=1, column=0, pady=15, padx=10)

label_3 = Label(leftframe, font="fixedsys 10 normal")
label_3.grid(row=2, column=0, pady=15, padx=10)

label_4 = Label(leftframe, font="fixedsys 10 normal")
label_4.grid(row=3, column=0, pady=15, padx=10)

conn = mysql.connector.connect(host='localhost', user='root', password='', db='erp')
cur = conn.cursor()
cur.execute(
    'CREATE TABLE IF NOT EXISTS Faculty_Module(Faculty VARCHAR(75),Module_Name VARCHAR(150),Platform VARCHAR(120), Launch_Date VARCHAR(10),Link VARCHAR(500))')

cur.execute('SELECT * from Faculty_Module where Faculty = %s', (fullname,))
module = cur.fetchall()
add_to_playlist(module)

rootup.resizable(0, 0)

rootup.mainloop()
