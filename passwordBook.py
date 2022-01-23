from tkinter import *
import sys


def getPassword(user,service):
    print("Clicked")


window = Tk()

windWidth = 300
windHeight = 400
window.geometry(str(windWidth)+'x'+str(windHeight))
window.configure(bg='white')
rowI = 0

window.title("My Password Book")

titleLabel = Label(window, text="My Digital Password Book", font=("Monospace", 10, 'bold'),  width=38, height=1)
titleLabel.grid(column=1, row=rowI)
rowI+=1

titleLabel = Label(window, text="--", font=("Monospace", 10),  width=38, height=1,bg='white')
titleLabel.grid(column=1, row=rowI)
rowI+=1

#v Handle Retrieving Account Infomation v
def retrieve_input():
    input = self.myText_Box.get("1.0",END)


retrieveLabel = Label(window, text="~ Retrieve Account Information ~", font=("Monospace", 10), width=38, height=1,bg='white')
retrieveLabel.grid(column=1, row=rowI)
rowI+=1

service_RetrieveLabel = Label(window, text="Service:", font=("Monospace", 10), height=1,bg='white')
service_RetrieveInput = Entry(window)
service_RetrieveButton = Button(window, text="Retrieve Account Info", command=getPassword("",""), font=("Monospace", 10), cursor="trek")
#TODO: have this button grab user's account info (username password email) and put it in the resultsLabel as one big string

service_RetrieveLabel.grid(column=1, row=rowI, sticky = W, pady = 2)
rowI+=1
service_RetrieveInput.grid(column=1, row=rowI, pady = 2)
rowI+=1
service_RetrieveButton.grid(column=1, row=rowI, pady = 2)
rowI+=1

resultsLabel = Label(window, text="", font=("Monospace", 10), height=1,bg='white') #Label(window, text="(Result will show up here)", font=("Monospace", 5), height = 1,width = windWidth,bg='gray95')
resultsLabel.grid(column=1, row=rowI, pady = 2)
rowI+=1


def keydown(e):
    sys.exit()

#notify: can make multiple pop-ups at once by calling Tk() multiple times
    
titleLabel2 = Label(window, text="--", font=("Monospace", 10),  width=38, height=1,bg='white')
titleLabel2.grid(column=1, row=rowI)
rowI+=1
#v Handle Adding new Account Infomation v


titleLabel3 = Label(window, text="--", font=("Monospace", 10),  width=38, height=1,bg='white')
titleLabel3.grid(column=1, row=rowI)
rowI+=1
#v Keypress to kill on startup feature v
frame = Frame(window, width=0, height=0)
frame.bind("<KeyPress>", keydown)
frame.grid(column=1, row=rowI)
frame.focus_set()


window.mainloop()