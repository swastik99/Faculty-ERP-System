from tkinter import *
import datetime
from tkinter import ttk
from ttkthemes import themed_tk as tk
import mysql.connector
import tkinter.messagebox
import time
import re
import xlsxwriter

class firstpage:

    def auth(self):
        main = tk.ThemedTk()
        main.get_themes()
        main.set_theme("radiance")

        main.title("Module Registration System")
        main.iconbitmap(r'images/upes.ico')

        upesPhoto = PhotoImage(file='images/upes.png')
        label = Label(image=upesPhoto)
        label.pack(side=TOP, pady=20, padx=30)

        def r():
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password=""
            )

            cur = mydb.cursor()

            cur.execute("CREATE DATABASE IF NOT EXISTS erp")
            main.destroy()
            reg.register()

        def l():
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password=""
            )

            cur = mydb.cursor()

            cur.execute("CREATE DATABASE IF NOT EXISTS erp")
            main.destroy()
            log.login()

        regBtn = ttk.Button(main, text="REGISTER", width=20, command=r)
        regBtn.pack(side=LEFT, pady=20, padx=20)

        logBtn = ttk.Button(main, text="LOGIN", width=20, command=l)
        logBtn.pack(pady=20, padx=20)

        main.resizable(0, 0)

        main.mainloop()

class sign_in:
    def register(self):
        master = tk.ThemedTk()
        master.get_themes()
        master.set_theme("radiance")

        master.title("Module Registration System")
        master.iconbitmap(r'images/upes.ico')

        Firstname = StringVar()
        Lastname = StringVar()
        Email = StringVar()
        Password = StringVar()

        def clear_entry(event, entry):
            entry.delete(0, END)

        def regis():
            firstname = Firstname.get()
            lastname = Lastname.get()
            email = Email.get()
            password = Password.get()
            conn = mysql.connector.connect(host='localhost', user='root', password='', db='erp')

            def valid_mail(email):
                y = re.findall('@([^ ]*)', email)
                domain = y[0]
                if domain == "ddn.upes.ac.in":
                    return True
                else:
                    return False

            cur = conn.cursor()
            cur.execute(
                'CREATE TABLE IF NOT EXISTS Faculty_Register(FirstName VARCHAR(50),LastName VARCHAR(50),Email VARCHAR(100) UNIQUE, Password VARCHAR(50))')
            if firstname != '':
                if lastname != '':
                    if email != '' and valid_mail(email):
                        if password != '' and len(password) >= 8:
                            try:
                                cur.execute(
                                    'INSERT INTO Faculty_Register(FirstName,LastName,Email,Password) VALUES(%s,%s,%s,%s)',
                                    (firstname, lastname, email, password,))
                                conn.commit()
                                statusbar['text'] = 'Hurray!! You Have Successfully Registered ' + firstname
                                tkinter.messagebox.showinfo('Status',
                                                            firstname + ', your account has been created successfully\nPlease move to login area')
                                time.sleep(1)
                                master.destroy()
                                log.login()
                            except:
                                tkinter.messagebox.showerror("Invalid user",
                                                             "You have already registered, please proceed to login area")
                                master.destroy()
                                log.login()
                        else:
                            tkinter.messagebox.showerror('Error',
                                                         'Please fill the password carefully\nMinnimum Length of 8 charachters!!!')
                    else:
                        tkinter.messagebox.showerror('Error',
                                                     'Please enter a valid email!!!\nDomain should be ddn.upes.ac.in')
                else:
                    tkinter.messagebox.showerror('Error', 'Hey! Did you forget your last name?')
            else:
                tkinter.messagebox.showerror('Error', 'Hey! Seriously? Did you forget your first name?')

        statusbar = ttk.Label(master, text="Ready to register yourself!! Lets go...", relief=SUNKEN, anchor=W,
                              font="Times 10 italic")
        statusbar.pack(side=BOTTOM, fill=X)

        AddBtn = ttk.Button(master, text="REGISTER", width=20, command=regis)
        AddBtn.pack(side=BOTTOM, pady=10)

        topframe = Frame(master)
        topframe.pack()

        leftframe = Frame(master)
        leftframe.pack(side=LEFT)

        rightframe = Frame(master)
        rightframe.pack(side=RIGHT)

        middleframe = Frame(rightframe)
        middleframe.grid()

        bottomframe = Frame(master)
        bottomframe.pack(side=BOTTOM)

        ruser = PhotoImage(file="images/adduser.png")
        labelphoto = Label(topframe, image=ruser)
        labelphoto.pack(pady=20)

        label_1 = Label(leftframe, text="Name of the Faculty", font="fixedsys 10 normal")
        label_1.grid(row=0, column=0, padx=20, pady=20)

        entry_1 = ttk.Entry(middleframe, textvar=Firstname, width=33)
        placeholder_text = 'FIRST NAME'
        entry_1.insert(0, placeholder_text)
        entry_1.bind("<Button-1>", lambda event: clear_entry(event, entry_1))
        entry_1.grid(row=0, column=0, pady=20)

        space = Label(middleframe)
        space.grid(row=0, column=1, padx=20)

        entry_2 = ttk.Entry(middleframe, textvar=Lastname, width=33)
        placeholder_text = 'LAST NAME'
        entry_2.insert(0, placeholder_text)
        entry_2.bind("<Button-1>", lambda event: clear_entry(event, entry_2))
        entry_2.grid(row=0, column=2, pady=20)

        label_3 = Label(leftframe, text="Email ID", font="fixedsys 10 normal")
        label_3.grid(row=1, column=0, padx=20)
        entry_3 = ttk.Entry(rightframe, textvar=Email, width=75)
        placeholder_text = 'EMAIL ID'
        entry_3.insert(0, placeholder_text)
        entry_3.bind("<Button-1>", lambda event: clear_entry(event, entry_3))
        entry_3.grid(row=1, column=0, padx=20)

        bullet = "\u2022"  # specifies bullet character

        label_4 = Label(leftframe, text="Password", font="fixedsys 10 normal")
        label_4.grid(row=2, column=0, padx=20, pady=20)
        entry_4 = ttk.Entry(rightframe, show=bullet, textvar=Password, width=75)
        placeholder_text = '12345678'
        entry_4.insert(0, placeholder_text)
        entry_4.bind("<Button-1>", lambda event: clear_entry(event, entry_4))
        entry_4.grid(row=2, column=0, padx=20, pady=20)

        master.resizable(0, 0)

        master.mainloop()

class sign_up:
    def login(self):
        rootl = tk.ThemedTk()
        rootl.get_themes()
        rootl.set_theme("radiance")

        rootl.title("Module Registration System")
        rootl.iconbitmap(r'images/upes.ico')

        mailL = StringVar()
        pwordL = StringVar()
        global emailL
        global user
        global fam
        global fullname

        def clear_entry(event, entry):
            entry.delete(0, END)

        def log():
            global emailL
            global user
            global fam
            global fullname
            emailL = mailL.get()
            passwordL = pwordL.get()
            conn = mysql.connector.connect(host='localhost', user='root', password='', db='erp')

            def valid_mail(emailL):
                y = re.findall('@([^ ]*)', emailL)
                domain = y[0]
                if domain == "ddn.upes.ac.in":
                    return True
                else:
                    return False

            cur = conn.cursor()
            cur.execute(
                'CREATE TABLE IF NOT EXISTS Faculty_Register(FirstName VARCHAR(50),LastName VARCHAR(50),Email VARCHAR(100) UNIQUE, Password VARCHAR(50))')
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
                            user = cur.fetchone()[0]

                            cur.execute('SELECT LastName FROM Faculty_Register WHERE Email = %s',
                                        (emailL,))
                            fam = cur.fetchone()[0]
                            fullname = user + " " + fam

                            tkinter.messagebox.showinfo('Status',
                                                        user + ', you are successfully logged in')
                            rootl.destroy()
                            dir.menu()
                        else:
                            tkinter.messagebox.showinfo('Status',
                                                        'Incorrect Password, Please try again...')
                    except TypeError:
                        tkinter.messagebox.showinfo('Status',
                                                    'You are not registered\nPlease register yourself first...')
                        rootl.destroy()
                        reg.register()
                else:
                    tkinter.messagebox.showerror('Error',
                                                 'Please fill the password carefully\nMinnimum Length of 8 charachters!!!')
            else:
                tkinter.messagebox.showerror('Error', 'Please enter a valid email!!!\nDomain should be ddn.upes.ac.in')

        AddBtn = ttk.Button(rootl, text="LOGIN", width=20, command=log)
        AddBtn.pack(side=BOTTOM, pady=10)

        bottomframe = Frame(rootl)
        bottomframe.pack(side=BOTTOM)

        luser = PhotoImage(file="images/loguser.png")
        labelphoto = Label(rootl, image=luser)
        labelphoto.pack(pady=20, padx=150)

        l1 = Label(bottomframe, text="Email ID", font="fixedsys 10 normal")
        l1.grid(row=0, column=0, padx=20)
        e1 = ttk.Entry(bottomframe, textvar=mailL, width=30)
        placeholder_text = 'EMAIL ID'
        e1.insert(0, placeholder_text)
        e1.bind("<Button-1>", lambda event: clear_entry(event, e1))
        e1.grid(row=0, column=1, padx=20)

        bullet = "\u2022"  # specifies bullet character

        l2 = Label(bottomframe, text="Password", font="fixedsys 10 normal")
        l2.grid(row=1, column=0, pady=10, padx=20)
        e2 = ttk.Entry(bottomframe, show=bullet, textvar=pwordL, width=30)
        placeholder_text = '12345678'
        e2.insert(0, placeholder_text)
        e2.bind("<Button-2>", lambda event: clear_entry(event, e2))
        e2.grid(row=1, column=1, pady=10, padx=20)

        rootl.resizable(0, 0)
        rootl.mainloop()

class mnu:
    def menu(self):
        rootmnu = tk.ThemedTk()
        rootmnu.get_themes()
        rootmnu.set_theme("radiance")

        rootmnu.title("Module Registration System")
        rootmnu.iconbitmap(r'images/upes.ico')

        def logout():
            tkinter.messagebox.showinfo("Status", "You have been successfully logout, Please login back again")
            rootmnu.destroy()
            log.login()

        def about_us():
            tkinter.messagebox.showinfo("About Us",
                                        "This is a UPES ERP SYSTEM programmed and build for faculty module information system\nBy -Swastik Shrivastava\n    -Aditi Thapliyal\n    -Ujjwal Bharadwaj")

        def add():
            rootmnu.destroy()
            new.addmod()

        def delete():
            rootmnu.destroy()
            remove.delmod()

        def update():
            rootmnu.destroy()
            improve.upmod()

        def fetch():
            conn = mysql.connector.connect(host='localhost', user='root', password='', db='erp')
            cur = conn.cursor()
            cur.execute(
                'CREATE TABLE IF NOT EXISTS Faculty_Module(Faculty VARCHAR(75),Module_Name VARCHAR(150) UNIQUE ,Platform VARCHAR(120), Launch_Date VARCHAR(10),Link VARCHAR(500) UNIQUE )')

            cur.execute('SELECT * from Faculty_Module where Faculty = %s', (fullname,))
            module = cur.fetchall()
            if module != []:
                workbook = xlsxwriter.Workbook('Modules.xlsx')
                worksheet = workbook.add_worksheet()
                worksheet.title = "Module Information System"
                worksheet.set_column(0, 3, 45)
                worksheet.set_column(4, 4, 90)
                row = 0
                col = 0
                for i in range(0, len(module)):
                    for j in range(0, len(module[i])):
                        worksheet.write(row, col, module[i][j])
                        col += 1
                    col = 0
                    row += 1

                tkinter.messagebox.showinfo("Success Report",
                                            "Your modules has been successfully added to Modules.xlsx file")
                workbook.close()

            else:
                tkinter.messagebox.showerror("Error", "You have no modules in your account!!!")

        menubar = Menu(rootmnu)
        rootmnu.config(menu=menubar)

        subMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="Logout", command=logout)
        subMenu.add_command(label="Exit", command=rootmnu.destroy)

        subMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=subMenu)
        subMenu.add_command(label="About Us", command=about_us)

        topframe = Frame(rootmnu)
        topframe.pack()

        bottomframe = Frame(rootmnu)
        bottomframe.pack()

        DocImage = PhotoImage(file="images/UseDoc.png")
        labelphoto = Label(topframe, image=DocImage)
        labelphoto.pack(pady=30)

        AddBtn = ttk.Button(bottomframe, text="Add Modules", width=20, command=add)
        AddBtn.grid(row=0, column=0, padx=20, pady=10)

        DeleteBtn = ttk.Button(bottomframe, text="Delete Modules", width=20, command=delete)
        DeleteBtn.grid(row=0, column=1, padx=20, pady=10)

        UpdateBtn = ttk.Button(bottomframe, text="Update Modules Details", width=20, command=update)
        UpdateBtn.grid(row=1, column=0, padx=20, pady=10)

        FetchBtn = ttk.Button(bottomframe, text="Fetch all Modules", width=20, command=fetch)
        FetchBtn.grid(row=1, column=1, padx=20, pady=10)

        statusbar = ttk.Label(rootmnu, text="Choose an option and go ahead...", relief=SUNKEN, anchor=W,
                              font="Times 10 italic")
        statusbar.pack(side=BOTTOM, fill=X)

        rootmnu.resizable(0, 0)

        rootmnu.mainloop()

class add:
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
                                    dir.menu()
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

class delete:
    def delmod(self):
        rootdel = tk.ThemedTk()
        rootdel.get_themes()
        rootdel.set_theme("radiance")

        rootdel.title("Module Registration System")
        rootdel.iconbitmap(r'images/upes.ico')

        playlist = []

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
            statusbar['text'] = user + ", " + mod + " module has been deleted successfully"

        def cancel():
            rootdel.destroy()
            dir.menu()

        statusbar = ttk.Label(rootdel, text="Select a module to delete", relief=SUNKEN, anchor=W,
                              font="Times 10 italic")
        statusbar.pack(side=BOTTOM, fill=X)

        lframe = Frame(rootdel)
        lframe.pack(side=LEFT, pady=30, padx=10)

        rframe = Frame(rootdel)
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

        delbtn = ttk.Button(rbottomframe, text='DELETE', width=20, command=del_data)
        delbtn.grid(row=0, column=0, pady=10)

        cancelbtn = ttk.Button(rbottomframe, text='CANCEL', width=20, command=cancel)
        cancelbtn.grid(row=0, column=1, padx=50, pady=10)

        label_1 = Label(leftframe, font="fixedsys 10 normal")
        label_1.grid(row=0, column=0, pady=15, padx=10)
        entry_1 = Label(rightframe, font="Times 8 normal", width=40)
        entry_1.grid(row=0, column=1, pady=15, padx=30)

        label_2 = Label(leftframe, font="fixedsys 10 normal")
        label_2.grid(row=1, column=0, pady=15, padx=10)
        entry_2 = Label(rightframe, font="Times 8 normal", width=40)
        entry_2.grid(row=1, column=1, pady=15, padx=30)

        label_3 = Label(leftframe, font="fixedsys 10 normal")
        label_3.grid(row=2, column=0, pady=15, padx=10)
        entry_3 = Label(rightframe, font="Times 8 normal", width=40)
        entry_3.grid(row=2, column=1, pady=15, padx=30)

        label_4 = Label(leftframe, font="fixedsys 10 normal")
        label_4.grid(row=3, column=0, pady=15, padx=10)
        entry_4 = Label(rightframe, font="Times 8 normal", width=40)
        entry_4.grid(row=3, column=1, pady=15, padx=30)

        conn = mysql.connector.connect(host='localhost', user='root', password='', db='erp')
        cur = conn.cursor()
        cur.execute(
            'CREATE TABLE IF NOT EXISTS Faculty_Module(Faculty VARCHAR(75),Module_Name VARCHAR(150) UNIQUE,Platform VARCHAR(120), Launch_Date VARCHAR(10),Link VARCHAR(500) UNIQUE)')

        cur.execute('SELECT * from Faculty_Module where Faculty = %s', (fullname,))
        module = cur.fetchall()
        add_to_playlist(module)

        rootdel.resizable(0, 0)

        rootdel.mainloop()

class update:
    def upmod(self):
        rootup = tk.ThemedTk()
        rootup.get_themes()
        rootup.set_theme("radiance")

        rootup.title("Module Registration System")
        rootup.iconbitmap(r'images/upes.ico')

        playlist = []

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
            selected_mod = playlistbox.curselection()
            selected_mod = int(selected_mod[0])
            mod = playlist[selected_mod]
            conn = mysql.connector.connect(host='localhost', user='root', password='', db='erp')
            cur = conn.cursor()
            cur.execute('SELECT * from Faculty_Module where Faculty = %s and Module_Name = %s', (fullname, mod,))
            data = cur.fetchone()

            label_1['text'] = "Module Name : "
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
                            try:
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
                                improve.upmod()
                            except:
                                tkinter.messagebox.showerror("Module error",
                                                             "Module name or module link has already being stored in the database, please enter a another one")

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
            dir.menu()

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
            'CREATE TABLE IF NOT EXISTS Faculty_Module(Faculty VARCHAR(75),Module_Name VARCHAR(150) UNIQUE,Platform VARCHAR(120), Launch_Date VARCHAR(10),Link VARCHAR(500)UNIQUE)')

        cur.execute('SELECT * from Faculty_Module where Faculty = %s', (fullname,))
        module = cur.fetchall()
        add_to_playlist(module)

        rootup.resizable(0, 0)

        rootup.mainloop()

start = firstpage()
reg = sign_in()
log = sign_up()
dir = mnu()
new = add()
remove = delete()
improve = update()
start.auth()