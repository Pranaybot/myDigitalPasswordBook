import sqlite3;
from cryptography.fernet import Fernet


def addUser(user, masterPassword):
    con = sqlite3.connect('project.db')
    cur = con.cursor()
    #first check that the user does not exist already
    cur.execute("SELECT user FROM USERS WHERE user = :user1", {"user1": user}) #.execute is used to get data
    val = cur.fetchone()
    #if there is no user yet, we can add them
    if(val is None):
        cur.execute("INSERT INTO USERS VALUES(?,?)", (user, masterPassword))
        con.commit() #con.commit() is used to save changes
    #user alreayd exists
    else:
        print("failure1")
    con.close()

def addService(user, userName, service):
    con = sqlite3.connect('project.db')
    cur = con.cursor()
    cur.execute("SELECT password FROM PASSES WHERE user = :user1 AND site = :service1", {"user1": user, "service1":service})
    #check that user/service pair does not exist already, fails if it does
    if(cur.fetchone() is None):
        #get the original master password
        cur.execute("SELECT masterPassword FROM USERS WHERE user = :user1", {"user1": user})
        val = cur.fetchone()
        #make sure we get the master password - if not, failure
        if(val is None):
            print("failure, user does not exist")
        #encrypt password and store for later use
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
    con = sqlite3.connect('project.db')
    cur = con.cursor()

    #get username password pair from db
    cur.execute("SELECT userName, password FROM PASSES WHERE user = :user1 AND site = :service1", {"user1": user, "service1":service})
    val = cur.fetchone()
    #check to make sure we have output, if we don't we have an error
    if(val is None):
        print("none")
        return []
    print(val[0])
    return val 

#for testing
def getAll():
    con = sqlite3.connect('project.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM PASSES")
    print(cur.fetchall())
    cur.execute("SELECT * FROM users")
    print(cur.fetchall())

addUser("dave", "asdf")
addService("dave", "dave1", "aol.com")
getPassword("Aydin", "yahoo.com")
getAll()
