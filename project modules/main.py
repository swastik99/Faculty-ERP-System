from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk

rootmnu = tk.ThemedTk()
rootmnu.get_themes()
rootmnu.set_theme("radiance")

rootmnu.title("Module Registration System")
rootmnu.iconbitmap(r'images/upes.ico')

topframe = Frame(rootmnu)
topframe.pack()

bottomframe = Frame(rootmnu)
bottomframe.pack()

DocImage = PhotoImage(file="images/UseDoc.png")
labelphoto = Label(topframe,image = DocImage)
labelphoto.pack(pady = 40)

AddBtn = ttk.Button(bottomframe, text = "Add Modules", width = 20)
AddBtn.grid(row=0, column=0, padx=40)

DeleteBtn = ttk.Button(bottomframe, text = "Delete Modules", width = 20)
DeleteBtn.grid(row=0, column=1, padx=40)

UpdateBtn = ttk.Button(bottomframe, text = "Update Modules Details", width = 20)
UpdateBtn.grid(row=1, column=0, padx=40, pady = 20)

FetchBtn = ttk.Button(bottomframe, text = "Fetch all Modules", width = 20)
FetchBtn.grid(row=1, column=1, padx=40, pady = 20)

statusbar = ttk.Label(rootmnu, text="Choose an option and go ahead...", relief=SUNKEN, anchor=W, font="Times 10 italic")
statusbar.pack(side=BOTTOM, fill=X)

rootmnu.mainloop()

