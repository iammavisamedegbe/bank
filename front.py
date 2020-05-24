from tkinter import *
import backend

class BankRegister:
    def __init__(self, master):
        self.master = master
        self.master.title('Bank\Main')
        self.master.geometry('820x400')
        self.master.config(bg="")
        self.frame = Frame(self.master)
        self.frame.pack()
#==================front frame============================
        self.Titleframe= Frame(self.frame , width=500, height=10, bd=0)
        self.Titleframe.grid(row=0, column=0, pady=6)

        self.Homeframe =Frame( self.frame , width=800, height=400, bd=0)
        self.Homeframe.grid(row=1, column=0, pady=70)

# ==================Variables============================
        AcctNo=StringVar()
        AcctNos=StringVar()
        Amt=IntVar()
        balance=StringVar()
        balances=StringVar()

        fname = StringVar()
        lname = StringVar()
        password = StringVar()
        confpassword = StringVar()
        emails = StringVar()
        Addr1 = StringVar()
        Addr2 = StringVar()
        Mno = StringVar()
        St = StringVar()
        nKin = StringVar()
        deleAcct=IntVar()
        MomoAmt=StringVar()
        MomoAcct= StringVar()
# ==================Functions============================

        #add deposit
        def adddeposit():
            if (len(AcctNo.get()) != 0):
                backend.adddeposit(AcctNo.get(),Amt.get())
        #checkbalance
        def checkbalance():
            for row in backend.ckbalance(AcctNo.get()):
                balance.set(row)
        #withdraw
        global sb
        def withdraws( ):
            sb=balances.get()
            if (len(AcctNos.get()) != 0):
                backend.withdrwaamt(sb[0],AcctNos.get(),balances.get())

            #modify account
        def modifyAccts():
            sb=password.get()
            if (len(fname.get()) != 0):
                print(backend.modifyacct(sb[0], fname.get(), lname .get(),password.get(),confpassword.get(),emails.get(),Addr1.get(),
                                   Addr2.get(),Mno.get(),St.get(),nKin.get()))


        #delete Account
        def deleteData():
            backend.deleteRecord(deleAcct.get())
            print('success')
        #buy airtime
        def payAirtime():
            sb = MomoAcct.get()
            if (len(MomoAcct.get()) != 0):
                backend.bill(sb[0],MomoAcct.get(),MomoAmt.get())
        #pay bills
        def paybill():
            sb = MomoAcct.get()
            if (len(MomoAcct.get()) != 0):
                backend.bill(sb[0], MomoAcct.get(), MomoAmt.get())
        #send funds
        def transferFund():
            sb = MomoAcct.get()
            if (len(MomoAcct.get()) != 0):
                backend.bill(sb[0], MomoAcct.get(), MomoAmt.get())


 # ==================CHECK BALANCE===========================
        def checkbalanceform():
            ckWindow = Toplevel(self.master)
            ckWindow.title('Bank\Check Balance')
            ckWindow.geometry('400x300')

            ckframe = Frame(ckWindow, width=500, height=10, bd=0)
            ckframe.grid(row=0, column=0, pady=6)
            ckbtnframe = Frame(ckWindow, width=500, height=10, bd=0)
            ckbtnframe.grid(row=1, column=0, pady=6)

            lblbalance= Label(ckframe, text="ACCOUNT No.:", font=('ariel', 15, 'bold'), width=30)
            lblbalance.grid(row=1, column=0)
            textbalance = Entry(ckframe, font=('ariel', 15, 'bold'), textvariable=AcctNo, width=30, relief=SUNKEN, insertwidth=4, bd=7)
            textbalance.grid(row=2, column=0, padx=20)

            textbalance = Entry(ckframe, text='', font=('ariel', 15, 'bold'), bd=20, textvariable=balance)
            textbalance.grid(row=3, column=0, padx=50)

            self.btnEnt = Button(ckbtnframe , text='ENTER', font=('ariel', 15, 'bold'), bd=7, relief=RAISED, command=checkbalance)
            self.btnEnt .grid(row=0, column=0, padx=0, pady=10)

            self.btnEntC = Button(ckbtnframe , text='CANCEL', font=('ariel', 15, 'bold'), bd=7, relief=RAISED, command=ckWindow.destroy)
            self.btnEntC.grid(row=0, column=1, padx=0, pady=10)

# ==================WITHDRAW FORM===========================
        def withdrawform():
            withdraw= Toplevel(self.master)
            withdraw.title('Bank\Withdraw')
            withdraw.geometry('400x300')

            wframe = Frame(withdraw, width=500, height=10, bd=0)
            wframe.grid(row=0, column=0, pady=6)
            wbtnframe= Frame(withdraw, width=500, height=10, bd=0)
            wbtnframe.grid(row=1, column=0, pady=6)

            lblbalancew = Label( wframe, text="ACCOUNT No.:", font=('ariel', 15, 'bold'), width=30)
            lblbalancew.grid(row=1, column=0)
            lblbalancew = Entry( wframe, font=('ariel', 15, 'bold'), textvariable=AcctNos, width=30, relief=SUNKEN,  insertwidth=4, bd=7)
            lblbalancew.grid(row=2, column=0, padx=20)

            lblbalancew = Label(wframe, text="AMOUNT:", font=('ariel', 15, 'bold'), width=30)
            lblbalancew.grid(row=3, column=0)

            textbalancew = Entry( wframe, text='', font=('ariel', 15, 'bold'), bd=7, textvariable=balances,width=30)
            textbalancew.grid(row=4, column=0, padx=20)

            self.btnEnts = Button( wbtnframe, text='ENTER', font=('ariel', 15, 'bold'), bd=7, relief=RAISED,command=withdraws)
            self.btnEnts.grid(row=0, column=0, padx=0, pady=10)

            self.btnEntCs = Button( wbtnframe, text='CANCEL', font=('ariel', 15, 'bold'), bd=7, relief=RAISED, command=withdraw.destroy)
            self.btnEntCs.grid(row=0, column=1, padx=0, pady=10)

# ==================DEPOSIT FORM===========================
        def depositform():
            depWindow = Toplevel(self.master)
            depWindow.title('Bank\Deposit')
            depWindow.geometry('400x300')

            depframe = Frame(depWindow, width=500, height=10, bd=0)
            depframe.grid(row=0, column=0, pady=6)

            depbtn = Frame(depWindow, width=500, height=10, bd=0)
            depbtn.grid(row=1, column=0, pady=6)

            self.lblT = Label(depframe, text='', font=('ariel', 15, 'bold'))
            self.lblT.grid(row=0, column=0, padx=70)

            lbluserName = Label(depframe, text="ACCOUNT No.:", font=('ariel', 15, 'bold'), width=30)
            lbluserName.grid(row=1, column=0)
            textUsers = Entry(depframe, font=('ariel', 15, 'bold'), textvariable=AcctNo, width=30, relief=SUNKEN, insertwidth=4, bd=7)
            textUsers.grid(row=2, column=0, padx=20)

            lblAmt = Label(depframe, text="ENTER AMOUNT:", font=('ariel', 15, 'bold'), width=30)
            lblAmt.grid(row=3, column=0)
            textAmt = Entry(depframe, font=('ariel', 15, 'bold'), textvariable=Amt, width=30, relief=SUNKEN,insertwidth=4, bd=7)
            textAmt.grid(row=4, column=0, padx=20)

            self.btnSav = Button(depbtn, text='SAVE', font=('ariel', 15, 'bold'), bd=7, relief=RAISED, command=adddeposit)
            self.btnSav.grid(row=0, column=0, padx=10)

            self.btnCancel = Button(depbtn, text='CANCEL', font=('ariel', 15, 'bold'), bd=7, relief=RAISED, command=depWindow.destroy)
            self.btnCancel.grid(row=0, column=1, padx=10)

# ==================MODFIFY FORM===========================
        def modifyAcct():
            ModWindow = Toplevel(self.master)
            ModWindow.title('Bank/Modify')
            ModWindow.geometry('600x550')
            # ====================label/Register===============================
            self.lblTitle = Label(ModWindow, text=' SeBan Bank', font=('ariel', 15, 'bold'))
            self.lblTitle.grid(row=0, column=0, padx=70)
            self.lblTits = Label(ModWindow, font=('ariel', 15, 'bold'))
            self.lblTits.grid(row=0, column=1, padx=40)
            # ====================frame/Register===============================
            self.Registerframe = LabelFrame(ModWindow, width=600, height=300, bd=0)
            self.Registerframe.grid(row=1, column=0)
            self.btnframes = LabelFrame(ModWindow, width=500, height=100, bd=0)
            self.btnframes.grid(row=2, column=0, pady=6)
            ##====================frame/Modify===============================
            self.lblfirstName = Label(self.Registerframe, text='First Name:', font=('ariel', 15, 'bold'), bd=4)
            self.lblfirstName.grid(row=2, column=0)
            self.txtfirstName = Entry(self.Registerframe, textvariable=fname, font=('ariel', 15), width=30,relief=SUNKEN, insertwidth=4, bd=7)

            self.txtfirstName.grid(row=2, column=1)

            self.lbllastName = Label(self.Registerframe, text='Last Name:', font=('ariel', 15, 'bold'))
            self.lbllastName.grid(row=3, column=0)
            self.txtlastName = Entry(self.Registerframe, textvariable=lname, font=('ariel', 15), width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.txtlastName.grid(row=3, column=1)


            self.lblpassword = Label(self.Registerframe, text='Password:', font=('ariel', 15, 'bold'))
            self.lblpassword.grid(row=5, column=0)
            self.txtpassword = Entry(self.Registerframe, textvariable=password, font=('ariel', 15), width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.txtpassword.grid(row=5, column=1)

            self.lblconpassword = Label(self.Registerframe, text='Confirm Password:', font=('ariel', 15, 'bold'))
            self.lblconpassword.grid(row=6, column=0)
            self.txtconpassword = Entry(self.Registerframe, textvariable= confpassword, font=('ariel', 15), width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.txtconpassword.grid(row=6, column=1)

            self.lblemail = Label(self.Registerframe, text='Email:', font=('ariel', 15, 'bold'))
            self.lblemail.grid(row=7, column=0)
            self.txtemail = Entry(self.Registerframe, textvariable=emails, font=('ariel', 15), width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.txtemail.grid(row=7, column=1)

            self.lblAddress1 = Label(self.Registerframe, text='Address 1:', font=('ariel', 15, 'bold'))
            self.lblAddress1.grid(row=8, column=0)
            self.txtAddress1 = Entry(self.Registerframe, textvariable=Addr1, font=('ariel', 15), width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.txtAddress1.grid(row=8, column=1)

            self.lblAddress2 = Label(self.Registerframe, text='Address 2:', font=('ariel', 15, 'bold'))
            self.lblAddress2.grid(row=9, column=0)
            self.txtAddress2 = Entry(self.Registerframe, textvariable=Addr2, font=('ariel', 15), width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.txtAddress2.grid(row=9, column=1)

            self.lblMobileNo = Label(self.Registerframe, text='MobileNo.:', font=('ariel', 15, 'bold'))
            self.lblMobileNo.grid(row=10, column=0)
            self.txtMobileNo = Entry(self.Registerframe, textvariable=Mno, font=('ariel', 15), width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.txtMobileNo.grid(row=10, column=1)

            self.lblStatus = Label(self.Registerframe, text='Status:', font=('ariel', 15, 'bold'))
            self.lblStatus.grid(row=11, column=0)
            self.txtStatus = Entry(self.Registerframe, textvariable=St, font=('ariel', 15), width=30, relief=SUNKEN,insertwidth=4, bd=7)
            self.txtStatus.grid(row=11, column=1)

            self.lblKins = Label(self.Registerframe, text='Next of Kins:', font=('ariel', 15, 'bold'))
            self.lblKins.grid(row=12, column=0)
            self.txtKins = Entry(self.Registerframe, textvariable=nKin, font=('ariel', 15), width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.txtKins.grid(row=12, column=1)

            self.lblTits = Label(self.btnframes, font=('ariel', 15, 'bold'))
            self.lblTits.grid(row=0, column=2, padx=90)

            self.btnsignin = Button(self.btnframes, text='UPDATE', font=('ariel', 12, 'bold'), relief=RAISED, bd=4,  width=10, command=modifyAccts)
            self.btnsignin.grid(row=0, column=4, pady=20, padx=0)

            self.btnsignin = Button(self.btnframes, text='Exit', font=('ariel', 12, 'bold'), relief=RAISED, bd=4, width=10, command=ModWindow.destroy)
            self.btnsignin.grid(row=0, column=5, pady=20, padx=0)

 ##====================Delete===============================
        def deleteAcct():
            delWindow = Toplevel(self.master)
            delWindow.title('Bank/Delete')
            delWindow.geometry('400x150')

            self.lbldel = Label(delWindow, text='ACCOUNT NO.:', font=('ariel', 15, 'bold'))
            self.lbldel .grid(row=0, column=0)
            self.txtAcct = Entry(delWindow, textvariable=deleAcct, font=('ariel', 15), width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.txtAcct.grid(row=1, column=0,padx=20)

            self.btnAcct = Button(delWindow, text='DELETE', font=('ariel', 12, 'bold'), relief=RAISED, bd=4,  width=10, command=deleteData)
            self.btnAcct.grid(row=2, column=0, pady=20, padx=0)

##====================TRANSER FUNDS==============================
        def transfund():
            fundWindow = Toplevel(self.master)
            fundWindow.title('Bank/Tranfer Funds')
            fundWindow.geometry('400x280')

            self.fundframe = LabelFrame( fundWindow, width=600, height=300, bd=0)
            self.fundframe.grid(row=0, column=0)
            self.fundbtnframes = LabelFrame(fundWindow, width=500, height=100, bd=0)
            self.fundbtnframes.grid(row=1, column=0, pady=6)

            self.lbluserName = Label(self.fundframe, text="ACCOUNT NO.:", font=('ariel', 15, 'bold'), width=30)
            self.lbluserName.grid(row=0, column=0)
            self.textUser = Entry(self.fundframe, font=('ariel', 15, 'bold'), textvariable=MomoAcct, width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.textUser.grid(row=1, column=0, padx=20)

            self.lblpassword = Label(self.fundframe, text="AMOUNT:", font=('ariel', 15, 'bold'))
            self.lblpassword.grid(row=2, column=0)
            self.textPass = Entry(self.fundframe, font=('ariel', 15, 'bold'), textvariable=MomoAmt,  width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.textPass.grid(row=3, column=0)

            self.lbluserName = Label(self.fundframe, text=" RECIPIENT ACCOUNT NO.:", font=('ariel', 15, 'bold'), width=30)
            self.lbluserName.grid(row=4, column=0)
            self.textUser = Entry(self.fundframe, font=('ariel', 15, 'bold'), textvariable="MomoAcct", width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.textUser.grid(row=5, column=0, padx=20)

            self.btnsignin = Button(self.fundbtnframes, text='TRANSFER', font=('ariel', 12, 'bold'), relief=RAISED, bd=4,  width=10, command=transferFund)
            self.btnsignin.grid(row=0, column=0, pady=20, padx=0)

            self.btnsignin = Button(self.fundbtnframes, text='CANCEL', font=('ariel', 12, 'bold'), relief=RAISED, bd=4,  width=10, command=fundWindow .destroy)
            self.btnsignin.grid(row=0, column=1, padx=10)

##====================PAY BILLS==============================
        def bills():
            billsWindow = Toplevel(self.master)
            billsWindow.title('Bank/Electricity/Water')
            billsWindow.geometry('400x280')

            self.billframe = LabelFrame(billsWindow, width=600, height=300, bd=0)
            self.billframe.grid(row=0, column=0)
            self.billbtnframes = LabelFrame(billsWindow, width=500, height=100, bd=0)
            self.billbtnframes.grid(row=1, column=0, pady=6)

            self.lbluserName = Label(self.billframe, text="ACCOUNT NO.:", font=('ariel', 15, 'bold'), width=30)
            self.lbluserName.grid(row=0, column=0)
            self.textUser = Entry(self.billframe, font=('ariel', 15, 'bold'), textvariable=MomoAcct, width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.textUser.grid(row=1, column=0, padx=20)

            self.lbluserName = Label(self.billframe, text="METER NO.:", font=('ariel', 15, 'bold'), width=30)
            self.lbluserName.grid(row=2, column=0)
            self.textUser = Entry(self.billframe, font=('ariel', 15, 'bold'), textvariable="Usernamelog", width=30,  relief=SUNKEN, insertwidth=4, bd=7)
            self.textUser.grid(row=3, column=0, padx=20)

            self.lblpassword = Label(self.billframe, text="AMOUNT:", font=('ariel', 15, 'bold'))
            self.lblpassword.grid(row=4, column=0)
            self.textPass = Entry(self.billframe, font=('ariel', 15, 'bold'), textvariable=MomoAmt,  width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.textPass.grid(row=5, column=0)

            self.btnsignin = Button(self.billbtnframes, text='MAKE PAYMENT:', font=('ariel', 12, 'bold'), relief=RAISED, bd=4, width=14, command=paybill)
            self.btnsignin.grid(row=0, column=0, pady=20, padx=0)

            self.btnsignin = Button(self.billbtnframes, text='CANCEL', font=('ariel', 12, 'bold'), relief=RAISED,   bd=4,width=10, command=billsWindow.destroy)
            self.btnsignin.grid(row=0, column=1, padx=10)

##====================AIRTIME=============================
        def airtime():
            airtimeWindow = Toplevel(self.master)
            airtimeWindow.title('Bank/Airtime')
            airtimeWindow.geometry('400x280')

            self.airtimeframe = LabelFrame(airtimeWindow, width=600, height=300, bd=0)
            self.airtimeframe.grid(row=0, column=0)
            self.airbtnframes = LabelFrame(airtimeWindow, width=500, height=100, bd=0)
            self.airbtnframes.grid(row=1, column=0, pady=6)

            self.lbluserName = Label(self.airtimeframe, text="ACCOUNT NO.:", font=('ariel', 15, 'bold'), width=30)
            self.lbluserName.grid(row=0, column=0)
            self.textUser = Entry(self.airtimeframe, font=('ariel', 15, 'bold'), textvariable=MomoAcct, width=30,relief=SUNKEN, insertwidth=4, bd=7)
            self.textUser.grid(row=1, column=0, padx=20)

            self.lblpassword = Label(self.airtimeframe, text="AMOUNT:", font=('ariel', 15, 'bold'))
            self.lblpassword.grid(row=2, column=0)
            self.textPass = Entry(self.airtimeframe, font=('ariel', 15, 'bold'),  textvariable=MomoAmt, width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.textPass.grid(row=3, column=0)

            self.lblpassword = Label(self.airtimeframe, text="MOBILE NO.:", font=('ariel', 15, 'bold'))
            self.lblpassword.grid(row=4, column=0)
            self.textPass = Entry(self.airtimeframe, font=('ariel', 15, 'bold'), textvariable="MomoAmt",  width=30, relief=SUNKEN, insertwidth=4, bd=7)
            self.textPass.grid(row=5, column=0)

            self.btnsignin = Button(self.airbtnframes, text='MAKE PAYMENT:', font=('ariel', 12, 'bold'),  relief=RAISED,  bd=4,  width=14, command=payAirtime)
            self.btnsignin.grid(row=0, column=0, pady=20, padx=0)

            self.btnsignin = Button(self.airbtnframes, text='CANCEL', font=('ariel', 12, 'bold'), relief=RAISED, bd=4, width=10, command=airtimeWindow.destroy)
            self.btnsignin.grid(row=0, column=1, padx=10)

# ==================front buttons===========================
        self.lblTitle=Label(self.Titleframe, text='Seban Online Banking System', font=('ariel', 25,'bold'))
        self.lblTitle.grid(row=0,column=1)

        self.lblT = Label(self.Homeframe, text='', font=('ariel', 15, 'bold'))
        self.lblT.grid(row=0, column=0)

        self.btndep=Button(self.Homeframe, text='DEPOSIT', font=('ariel', 15,'bold'),bd=7, relief=RAISED, command=depositform)
        self.btndep.grid(row=1, column=1,padx=10)

        self.btnwithd = Button(self.Homeframe, text='WITHDRAW', font=('ariel', 15, 'bold'), bd=7, relief=RAISED,command=withdrawform)
        self.btnwithd.grid(row=1, column=2,padx=10)

        self.btnairtime = Button(self.Homeframe, text='BUY AIRTIME', font=('ariel', 15, 'bold'), bd=7, relief=RAISED, command=airtime)
        self.btnairtime .grid(row=1, column=3,padx=10)

        self.btnmodify = Button(self.Homeframe, text='MODIFY ACCOUNT', font=('ariel', 15, 'bold'), bd=7, relief=RAISED, command=modifyAcct)
        self.btnmodify .grid(row=2, column=1,padx=10)

        self.lblT = Label(self.Homeframe, text='', font=('ariel', 15, 'bold'))
        self.lblT.grid(row=2, column=0)

        self.btncheckbal= Button(self.Homeframe, text='CHECK BALANCE', font=('ariel', 15, 'bold'), bd=7, relief=RAISED, command=checkbalanceform)
        self.btncheckbal.grid(row=2, column=2,padx=10)

        self.btnfunds = Button(self.Homeframe, text='TRANSFER FUNDS', font=('ariel', 15, 'bold'), bd=7, relief=RAISED, command=transfund)
        self.btnfunds.grid(row=2, column=3, padx=10)

        self.btnbills = Button(self.Homeframe, text='PAY BILLS(water/electrity)', font=('ariel', 15, 'bold'), bd=7, relief=RAISED, command=bills)
        self.btnbills.grid(row=3, column=1,padx=10)

        self.btndel = Button(self.Homeframe, text='DELETE ACCOUNT', font=('ariel', 15, 'bold'), bd=7, relief=RAISED, command=deleteAcct)
        self.btndel.grid(row=3, column=2, padx=10)

        self.btnreq = Button(self.Homeframe, text='COMPLAINS/REQUESTS', font=('ariel', 15, 'bold'), bd=7, relief=RAISED)
        self.btnreq.grid(row=3, column=3, padx=13)













