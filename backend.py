import sqlite3

def connectData():
    con=sqlite3.connect('bank.db')
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS registration (id INTEGER PRIMARY KEY, fName text,lName text,Username text,Password text,
                    conpassword text, email text, Addr1 text,Addr2 text, Mno text, St text, nKin text)""")
    con.commit()
    con.close()

def addRecord(fName,lName,Username,Password,conpassword,email,Addr1,Addr2,Mno,St,nKin):
    con = sqlite3.connect('bank.db')
    cur = con.cursor()
    cur.execute("INSERT INTO registration VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?)",
                (fName,lName,Username,Password,conpassword,email,Addr1,Addr2,Mno,St,nKin))
    con.commit()
    con.close()

def login(Username,Password):
    con = sqlite3.connect('bank.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM registration WHERE Username=? AND Password=?",(Username,Password))
    rows= cur.fetchall()
    con.close()
    return  rows
def deposit():
    con = sqlite3.connect('bank.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS deposit (id INTEGER PRIMARY KEY, AcctNo text, Amt INTEGER)")
    con.commit()
    con.close()

def adddeposit(AcctNo,Amt):
    con = sqlite3.connect('bank.db')
    cur = con.cursor()
    cur.execute("INSERT INTO deposit VALUES (NULL,?,?)",(AcctNo,Amt))
    con.commit()
    con.close()

deposits=0
def ckbalance(AcctNo):
    con = sqlite3.connect('bank.db')
    cur = con.cursor()
    cur.execute("SELECT  SUM(Amt) FROM deposit WHERE AcctNo=?",[AcctNo])
    rows= cur.fetchall()
    con.close()
    return  rows


def withdrwaamt(id,AcctNo="",Amt=""):
    con = sqlite3.connect('bank.db')
    cur = con.cursor()
    cur.execute("UPDATE deposit SET Amt= Amt-?, AcctNo=? WHERE id =?", (Amt,AcctNo,id))
    con.commit()
    con.close()

def bill(id,AcctNo="",Amt=""):
    con = sqlite3.connect('bank.db')
    cur = con.cursor()
    cur.execute("UPDATE deposit SET Amt= Amt-?, AcctNo=? WHERE id =?", (Amt,AcctNo,id))
    con.commit()
    con.close()

def modifyacct(id,fName="", lName="",  Password="", conpassword="", email="", Addr1="", Addr2="", Mno="", St="", nKin=""):
    con = sqlite3.connect('bank.db')
    cur = con.cursor()
    cur.execute("UPDATE registration SET fName=?, lName=?, Password=?, conpassword=?, email=?, Addr1=?, Addr2=?, Mno=?, St=?, nKin=? WHERE id =?",
                (fName,lName,Password,conpassword,email,Addr1,Addr2,Mno,St,nKin, id))
    con.commit()
    con.close()


def viewrec():
    con = sqlite3.connect('bank.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM  registration")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRecord(Username):
    con = sqlite3.connect('bank.db')
    cur = con.cursor()
    cur.execute("DELETE FROM registration WHERE Username=?", (Username,))
    con.commit()
    con.close()




