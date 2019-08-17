import smtplib
import random
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from ttkthemes import themed_tk as tk
class validate:
    def check(self, mail):
        subroot = tk.ThemedTk()
        subroot.get_themes()
        subroot.set_theme("radiance")

        subroot.title("Verify OTP")
        subroot.iconbitmap(r'images/upes.ico')
        num = 0
        verify = " "
        while len(verify)<6:
            num = num*10+random.randrange(0, 9)
            verify=str(num)


        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("swastikshrivastava2@gmail.com", "swas%99#v")
        server.sendmail(
          "swastikshrivastava2@gmail.com",mail,
          "Hi,\n Verify that it you\n"+verify+ "\nBy just enter this OTP")
        server.quit()

        def ver():
            OTP = otp.get()
            O = int(OTP)
            if O == num:
                print("Successful")

            else:
                print("Please enter the correct otp")

        otp = StringVar()
        subbtn = ttk.Button(subroot, text='Submit', width=20, command=ver)
        subbtn.pack(side = BOTTOM, pady = 5)

        label_1 = ttk.Label(subroot, text="We sent an email to "+mail+" with a 6 digit OTP enter here to reset your password", width=100, font=("Times 10 bold"))
        label_1.pack(padx=20)
        entry_1 = ttk.Entry(subroot, textvar=otp, width=20)
        entry_1.pack(side=LEFT, padx=20)

        subroot.mainloop()

"""mail = "500054670@stu.upes.ac.in"
val = validate()
val.check(mail)"""