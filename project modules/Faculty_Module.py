from tkinter import *
import datetime
import re
import time
import tkinter.messagebox
from tkinter import ttk
from ttkthemes import themed_tk as tk
import mysql.connector

fullname = "Ankit Vishnoi"
class Add:
    def addmod(self):
        rootadd = tk.ThemedTk()
        rootadd.get_themes()
        rootadd.set_theme("radiance")

        rootadd.title("Module Registration System")
        rootadd.iconbitmap(r'images/upes.ico')

        addrImage = PhotoImage(file="images/addrecord.png")
        addrphoto = Label(rootadd, image=addrImage)
        addrphoto.pack(pady=20)

        Fullname = StringVar()
        ModuleName = StringVar()
        Platform = StringVar()
        Date = StringVar()
        link = StringVar()

        def database():
            name = Fullname.get()
            Module = ModuleName.get()
            platform = Platform.get()
            date = Date.get()
            doclink = link.get()
            conn = mysql.connector.connect(host='localhost', user='root', password='', db='erp')
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

            def valid_name(name):
                if fullname == name:
                    return True
                else:
                    return False

            cur = conn.cursor()
            cur.execute(
                'CREATE TABLE IF NOT EXISTS Faculty_Module(Faculty VARCHAR(75),Module_Name VARCHAR(150) UNIQUE,Platform VARCHAR(120), Launch_Date VARCHAR(10),Link VARCHAR(500) UNIQUE)')
            if name != '' and valid_name(name):
                if Module != '':
                    if platform != '':
                        if date != '' and valid_date(datestring):
                            if doclink != '':
                                try:
                                    cur.execute(
                                        'INSERT INTO Faculty_Module(Faculty,Module_Name,Platform,Launch_Date,Link) VALUES(%s,%s,%s,%s,%s)',
                                        (name, Module, platform, date, doclink,))
                                    conn.commit()
                                    statusbar['text'] = 'Hurray!! Record Added Successfully ' + name
                                    tkinter.messagebox.showinfo('Status',
                                                                'New Record Added Succesfully\nFaculty Name : ' + str(
                                                                    name) + '\nModule Name : ' + str(
                                                                    Module) + '\nPlatform on which module is developed : ' + str(
                                                                    platform) + '\nDate of Launching : ' + str(
                                                                    date) + '\nLink for the module :' + str(
                                                                    doclink))
                                    time.sleep(1)
                                    rootadd.destroy()
                                    mu.menu()

                                except:
                                    tkinter.messagebox.showerror("Invalid Module",
                                                                 "Either same module name or link has already being stored in the database...\nPlease enter a new one")

                            else:
                                tkinter.messagebox.showerror('Link Error', 'Please fill the Link of the document!!!')
                        else:
                            tkinter.messagebox.showerror('Date Error',
                                                         'Please fill the valid date\nFormat : DD/MM/YYYY or DD-MM-YYYY!!!')
                    else:
                        tkinter.messagebox.showerror('Platform not found Error', 'Please select a platform carefully!!!')
                else:
                    tkinter.messagebox.showerror('Module Error', 'Hey! Did you forget your Module name?')
            else:
                tkinter.messagebox.showerror('Name Error', 'Hey! Seriously? Did you forget your fullname?')

        statusbar = ttk.Label(rootadd, text="Ready to add a new module!! Lets go...", relief=SUNKEN, anchor=W,
                              font="Times 10 italic")
        statusbar.pack(side=BOTTOM, fill=X)

        subbtn = ttk.Button(rootadd, text='Add Module', width=20, command=database)
        subbtn.pack(side=BOTTOM, pady=20)

        leftframe = Frame(rootadd)
        leftframe.pack(side=LEFT, padx=40, pady=10)

        rightframe = Frame(rootadd)
        rightframe.pack(pady=10, padx=40)

        label_1 = Label(leftframe, text="Faculty Full Name", font="fixedsys 10 normal")
        label_1.pack(pady=10)
        entry_1 = ttk.Entry(rightframe, textvar=Fullname, width=60)
        entry_1.pack(pady=10)

        label_2 = Label(leftframe, text="Name of Module", font="fixedsys 10 normal")
        label_2.pack(pady=10)
        entry_2 = ttk.Entry(rightframe, textvar=ModuleName, width=60)
        entry_2.pack(pady=10)

        label_3 = Label(leftframe, text="Platform of module", font="fixedsys 10 normal")
        label_3.pack(pady=10)
        list = ['', 'E-PG-Pathshala', 'CEC(Under Graduate) ', 'SWAYAM', 'MOOCs platform',
                'NPTEL/NMEICT/any other Government initiatives'];
        droplist = ttk.OptionMenu(rightframe, Platform, *list)
        droplist.config(width=43)
        Platform.set('Select your Platform')
        droplist.pack(pady=10)

        label_4 = Label(leftframe, text="Date of Launching", font="fixedsys 10 normal")
        label_4.pack(pady=10)
        entry_4 = ttk.Entry(rightframe, textvar=Date, width=60)
        entry_4.pack(pady=10)

        label_5 = Label(leftframe, text="Link of the document", font="fixedsys 10 normal")
        label_5.pack(pady=10)
        entry_5 = ttk.Entry(rightframe, textvar=link, width=60)
        entry_5.pack(pady=10)

        rootadd.resizable(0, 0)

        rootadd.mainloop()

class mnu(Add):

    def menu(self,Module):
        print(Module)

add = Add()
mu = mnu()
add.addmod()