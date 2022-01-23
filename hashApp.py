import sqlite3;
from cryptography.fernet import Fernet


def addUser(user, masterPassword):
    con = sqlite3.connect('testdb.db')
    cur = con.cursor()
    #first check that the user does not exist already
    cur.execute("SELECT user FROM USERS WHERE user = :user1", {"user1": user})
    val = cur.fetchone()
    if(val is None):
        cur.execute("INSERT INTO USERS VALUES(?,?)", (user, masterPassword))
        con.commit()
    else:
        print("failure1")
    con.close()

def addService(user, userName, service):
    con = sqlite3.connect('testdb.db')
    cur = con.cursor()
    cur.execute("SELECT password FROM PASSES WHERE user = :user1 AND site = :service1", {"user1": user, "service1":service})
    if(cur.fetchone() is None):
        cur.execute("SELECT masterPassword FROM USERS WHERE user = :user1", {"user1": user})
        val = cur.fetchone()
        if(val is None):
            print("failure, user does not exist")
        else:
            masterPassword = val[0]
            key = Fernet.generate_key()
            fernet = Fernet(key)
            finalPassword = fernet.encrypt(masterPassword.encode())

            cur.execute("INSERT into Passes VALUES(?,?,?,?)", (user, userName, service, finalPassword))
            con.commit()
    else:
        print("failure")
    con.close()




def getPassword(user, service):
    con = sqlite3.connect('testdb.db')
    cur = con.cursor()

    cur.execute("SELECT userName, password FROM PASSES WHERE user = :user1 AND site = :service1", {"user1": user, "service1":service})
    val = cur.fetchone()
    if(val is None):
        print("none")
        return []
    print(val[0])
    return val 

def getAll():
    con = sqlite3.connect('testdb.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM PASSES")
    print(cur.fetchall())
    cur.execute("SELECT * FROM users")
    print(cur.fetchall())

addUser("dave", "asdf")
addService("dave", "dave1", "aol.com")
getPassword("Aydin", "yahoo.com")
getAll()
