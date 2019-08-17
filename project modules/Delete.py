from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
import mysql.connector

rootdel = tk.ThemedTk()
rootdel.get_themes()
rootdel.set_theme("radiance")


rootdel.title("Module Registration System")
rootdel.iconbitmap(r'images/upes.ico')

playlist = []
fullname = 'Ankit Vishnoi'


def add_to_playlist(module):
    index = 0
    for i in range(0, len(module)):
        playlistbox.insert(index, module[i][1])
        playlist.insert(index,module[i][1])
        playlistbox.pack()
        index+=1

def show_data():
    global mod
    global selected_mod
    selected_mod = playlistbox.curselection()
    selected_mod = int(selected_mod[0])
    mod = playlist[selected_mod]
    conn = mysql.connector.connect(host='localhost', user='root', password='', db='erp')
    cur = conn.cursor()
    cur.execute('SELECT * from Faculty_Module where Faculty = %s and Module_Name = %s',(fullname,mod,))
    data = cur.fetchone()
    label_1['text'] = "Module Name : "
    label_2['text'] = "Platform : "
    label_3['text'] = "Date of Launching: "
    label_4['text'] = "Link of Module : "
    entry_1['text'] = data[1]
    entry_1['relief'] = SUNKEN
    entry_2['text'] = data[2]
    entry_2['relief'] = SUNKEN
    entry_3['text'] = data[3]
    entry_3['relief'] = SUNKEN
    entry_4['text'] = data[4]
    entry_4['relief'] = SUNKEN

def del_data():
    conn = mysql.connector.connect(host='localhost', user='root', password='', db='erp')
    cur = conn.cursor()
    cur.execute('DELETE FROM Faculty_Module WHERE Faculty = %s and Module_Name = %s', (fullname, mod,))
    conn.commit()
    playlist.pop(selected_mod)
    playlistbox.delete(selected_mod)
    statusbar['text'] = fullname+", "+mod+" module has been deleted successfully"

def cancel():
    rootdel.destroy()

statusbar = ttk.Label(rootdel, text="Ready to add a new module!! Lets go...", relief=SUNKEN, anchor=W, font="Times 10 italic")
statusbar.pack(side=BOTTOM, fill=X)

lframe = Frame(rootdel)
lframe.pack(side = LEFT, pady=30, padx = 10)

rframe = Frame(rootdel)
rframe.pack( pady=30)

lbottomframe = Frame(lframe)
lbottomframe.pack(side = BOTTOM)

rbottomframe = Frame(rframe)
rbottomframe.pack(side = BOTTOM)

leftframe = Frame(rframe)
leftframe.pack(side=LEFT)

rightframe = Frame(rframe)
rightframe.pack()

playlistbox = Listbox(lframe)
playlistbox.pack(pady = 10)


showbtn = ttk.Button(lbottomframe, text='SHOW DETAILS', width=20, command=show_data)
showbtn.pack(pady = 10)

delbtn = ttk.Button(rbottomframe, text='DELETE', width=20, command = del_data)
delbtn.grid(row = 0, column = 0, pady = 10)


cancelbtn = ttk.Button(rbottomframe, text='CANCEL', width=20, command = cancel)
cancelbtn.grid(row = 0, column = 1, padx = 50,pady = 10)

label_1 = Label(leftframe, font="fixedsys 10 normal")
label_1.grid(row = 0, column = 0,  pady=15, padx = 10)
entry_1 = Label(rightframe, font="Times 8 normal", width = 40)
entry_1.grid(row = 0, column = 1,  pady=15,padx = 30)

label_2 = Label(leftframe, font="fixedsys 10 normal")
label_2.grid(row = 1, column = 0,  pady=15, padx = 10)
entry_2 = Label(rightframe, font="Times 8 normal", width = 40)
entry_2.grid(row = 1, column = 1,  pady=15, padx = 30)

label_3 = Label(leftframe, font="fixedsys 10 normal")
label_3.grid(row = 2, column = 0,  pady=15, padx = 10)
entry_3 = Label(rightframe, font="Times 8 normal", width = 40)
entry_3.grid(row = 2, column = 1,  pady=15, padx = 30)

label_4 = Label(leftframe, font="fixedsys 10 normal")
label_4.grid(row = 3, column = 0,  pady=15, padx = 10)
entry_4 = Label(rightframe, font="Times 8 normal", width = 40)
entry_4.grid(row = 3, column = 1,  pady=15, padx = 30)

conn = mysql.connector.connect(host='localhost',user='root', password='',db='erp')
cur = conn.cursor()
cur.execute(
    'CREATE TABLE IF NOT EXISTS Faculty_Module(Faculty VARCHAR(75),Module_Name VARCHAR(150),Platform VARCHAR(120), Launch_Date VARCHAR(10),Link VARCHAR(500))')

cur.execute('SELECT * from Faculty_Module where Faculty = %s',(fullname,))
module = cur.fetchall()
add_to_playlist(module)

rootdel.resizable(0,0)

rootdel.mainloop()