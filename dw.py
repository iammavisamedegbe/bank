from tkinter import *
import tkinter.messagebox
import backend
import random
from front import BankRegister

# REGISTRATION AND LOGIN
class BankLogin:
    def __init__(self, master):
        self.master= master
        self.master.title('Bank\Login')
        self.master.geometry('520x330')
        self.master.config(bg="")
        self.frame=Frame(self.master)
        self.frame.pack()
#====================label/Login===============================
        self.lblTitle=Label(self.frame,text=' Welcome To SeBan Banking Systems', font=('ariel',20,'bold'))
        self.lblTitle.grid(row=0, column=0, pady=0)
#====================frame/Login===============================
        self.loginframe=LabelFrame(self.frame,width=500, height=150, bd=0)
        self.loginframe.grid(row=1, column=0, pady=6)

        self.btnframe = LabelFrame(self.frame, width=500, height=100, bd=0)
        self.btnframe.grid(row=2, column=0, pady=6)
#====================variable===============================

        Usernamelog = StringVar()
        Passwordlog = StringVar()

        fName = StringVar()
        lName = StringVar()
        Username = StringVar()
        Password = StringVar()
        conpassword = StringVar()
        email = StringVar()
        Addr1 = StringVar()
        Addr2 = StringVar()
        Mno = StringVar()
        St = StringVar()
        nKin = StringVar()

        x = random.randint(102034, 504590)
        randRef = str(x)
        Username.set(randRef)
# ============Functions==============================================================================

        def addRec():
            if (len(fName.get() )!= 0):
                backend.addRecord(fName.get(), lName.get(), Username.get(), Password.get(), conpassword.get(), email.get(), Addr1.get()
                                  , Addr2.get(), Mno.get(), St.get(), nKin.get())

        def Login():
            user = (Usernamelog.get())
            pas = (Passwordlog.get())
            for row in backend.login(Usernamelog.get(),Passwordlog.get()):
                if (user in row and pas in row):
                        openReg()
                else:
                     tkinter.messagebox.askyesno('Bank Management Login System', 'Invalid Login')
                     Usernamelog.set("")
                     Passwordlog.set("")

        def openReg():
            self.opens=Toplevel(self.master)
            self.app=BankRegister(self.opens)

        def iExit():
            iExit = tkinter.messagebox.askyesno('Bank Management System', 'Exit From Application?')
            if iExit > 0:
                self.master.destroy()
                return

#====================Register===============================
        def openRegister():
            regWindow = Toplevel(self.master)
            regWindow.title('Bank\Register')
            regWindow.geometry('600x550')
# ====================label/Register===============================
            self.lblTitle = Label(regWindow, text='Banking Systems/Register', font=('ariel', 15, 'bold'))
            self.lblTitle.grid(row=0, column=0,padx=70)
            self.lblTits = Label(regWindow, font=('ariel', 15, 'bold'))
            self.lblTits.grid(row=0, column=1, padx=40)
#====================frame/Register===============================
            self.Registerframe=LabelFrame(regWindow,width=600, height=300, bd=0)
            self.Registerframe.grid(row=1, column=0)
            self.btnframes = LabelFrame(regWindow, width=500, height=100, bd=0)
            self.btnframes.grid(row=2, column=0, pady=6)
##====================frame/Register/Entries===============================
            self.lblfirstName= Label(self.Registerframe, text='First Name:', font=('ariel',15,'bold'),bd=4)
            self.lblfirstName.grid(row=2, column=0)
            self.txtfirstName=Entry(self.Registerframe, textvariable=fName, font=('ariel', 15),width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.txtfirstName.grid(row=2, column=1)

            self.lbllastName = Label(self.Registerframe, text='Last Name:', font=('ariel', 15, 'bold'))
            self.lbllastName.grid(row=3, column=0)
            self.txtlastName = Entry(self.Registerframe, textvariable=lName, font=('ariel', 15),width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.txtlastName.grid(row=3, column=1)

            self.lblUname = Label(self.Registerframe, text='Account Number:', font=('ariel', 15, 'bold'))
            self.lblUname .grid(row=4, column=0)
            self.txtUname  = Entry(self.Registerframe, textvariable=Username, font=('ariel', 15), width=30, relief=SUNKEN, insertwidth=4, bd=7, state='disabled')
            self.txtUname .grid(row=4, column=1)

            self.lblpassword = Label(self.Registerframe, text='Password:', font=('ariel', 15, 'bold'))
            self.lblpassword.grid(row=5, column=0)
            self.txtpassword = Entry(self.Registerframe, textvariable=Password, font=('ariel', 15), width=30,  relief=SUNKEN, insertwidth=4, bd=7)
            self.txtpassword.grid(row=5, column=1)

            self.lblconpassword = Label(self.Registerframe, text='Confirm Password:', font=('ariel', 15, 'bold'))
            self.lblconpassword .grid(row=6, column=0)
            self.txtconpassword  = Entry(self.Registerframe, textvariable=conpassword, font=('ariel', 15), width=30,  relief=SUNKEN, insertwidth=4, bd=7)
            self.txtconpassword .grid(row=6, column=1)

            self.lblemail = Label(self.Registerframe, text='Email:', font=('ariel', 15, 'bold'))
            self.lblemail .grid(row=7, column=0)
            self.txtemail  = Entry(self.Registerframe, textvariable=email, font=('ariel', 15), width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.txtemail .grid(row=7, column=1)

            self.lblAddress1= Label(self.Registerframe, text='Address 1:', font=('ariel', 15, 'bold'))
            self.lblAddress1.grid(row=8, column=0)
            self.txtAddress1 = Entry(self.Registerframe, textvariable=Addr1, font=('ariel', 15),width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.txtAddress1.grid(row=8, column=1)

            self.lblAddress2 = Label(self.Registerframe, text='Address 2:', font=('ariel', 15, 'bold'))
            self.lblAddress2.grid(row=9, column=0)
            self.txtAddress2 = Entry(self.Registerframe, textvariable=Addr2, font=('ariel', 15),width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.txtAddress2.grid(row=9, column=1)

            self.lblMobileNo = Label(self.Registerframe, text='MobileNo.:', font=('ariel', 15, 'bold'))
            self.lblMobileNo.grid(row=10, column=0)
            self.txtMobileNo = Entry(self.Registerframe, textvariable=Mno, font=('ariel', 15),width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.txtMobileNo.grid(row=10, column=1)

            self.lblStatus = Label(self.Registerframe, text='Status:', font=('ariel', 15, 'bold'))
            self.lblStatus .grid(row=11, column=0)
            self.txtStatus = Entry(self.Registerframe, textvariable=St, font=('ariel', 15),width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.txtStatus .grid(row=11, column=1)

            self.lblKins = Label(self.Registerframe, text='Next of Kins:', font=('ariel', 15, 'bold'))
            self.lblKins.grid(row=12, column=0)
            self.txtKins = Entry(self.Registerframe, textvariable=nKin, font=('ariel', 15),width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.txtKins.grid(row=12, column=1)

            self.lblTits = Label(self.btnframes, font=('ariel', 15, 'bold'))
            self.lblTits.grid(row=0, column=2, padx=90)

            self.btnsignin = Button(self.btnframes, text='REGISTER', font=('ariel', 12, 'bold'), relief=RAISED, bd=4, width=10, command=addRec)
            self.btnsignin.grid(row=0, column=4, pady=20, padx=0)
            self.btnsignin = Button(self.btnframes, text='Exit', font=('ariel', 12, 'bold'), relief=RAISED, bd=4,  width=10, command=iExit)
            self.btnsignin.grid(row=0, column=5, pady=20, padx=0)


#LOGIN
        self.lbluserName=Label( self.loginframe,text="Account Number:", font=('ariel',15,'bold') ,width=30)
        self.lbluserName.grid(row=0,column=0)
        self.textUser = Entry(self.loginframe, font=('ariel', 15, 'bold'), textvariable= Usernamelog, width=30, relief=SUNKEN, insertwidth=4, bd=7)
        self.textUser.grid(row=1, column=0, padx=20)

        self.lblpassword= Label(self.loginframe, text="Password:", font=('ariel', 15, 'bold'))
        self.lblpassword.grid(row=2, column=0)
        self.textPass = Entry(self.loginframe, font=('ariel', 15, 'bold'), show='*', textvariable=Passwordlog,  width=30, relief=SUNKEN, insertwidth=4, bd=7)
        self.textPass.grid(row=3, column=0)

        self.check=Checkbutton(self.loginframe, text='Remember me', font=('ariel', 14))
        self.check.grid(row=4, column=0)

        self.btnsignin=Button(self.btnframe, text='REGISTER', font=('ariel', 12,'bold'),relief=RAISED, bd=4, width=10, command= openRegister)
        self.btnsignin.grid(row=0, column=0, pady=20, padx=0)

        self.btnsignin = Button(self.btnframe, text='SIGN IN', font=('ariel', 12,'bold'),  relief=RAISED, bd=4,width=10, command=Login)
        self.btnsignin.grid(row=0, column=1, padx=10)

#MAIN
if __name__=='__main__':
    root=Tk()
    application = BankLogin(root)
    root.mainloop()