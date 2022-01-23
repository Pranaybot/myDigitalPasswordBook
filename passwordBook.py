from tkinter import *


def getPassword(user,service):
    print("Clicked")


window = Tk()

windWidth = 300
windHeight = 400
window.geometry(str(windWidth)+'x'+str(windHeight))
window.configure(bg='white')
rowI = 0

window.title("My Password Book")
titleLabel = Label(window, text="My Digital Password Book", font=("Monospace", 10),  width=38, height=1)

titleLabel.grid(column=1, row=rowI)
rowI+=1

#v Handle Retrieving Account Infomation v
def retrieve_input():
    input = self.myText_Box.get("1.0",END)


retrieveLabel = Label(window, text="Retrieve Account Information", font=("Monospace", 10), width=38, height=1,bg='white')
retrieveLabel.grid(column=1, row=rowI)
rowI+=1

service_RetrieveLabel = Label(window, text="Service:", font=("Monospace", 10), width=38, height=1,bg='white')
service_RetrieveInput = Entry(window,width=10)
service_RetrieveButton = Button(window, text="Retrieve Account Info", command=getPassword("",""), font=("Monospace", 10))

service_RetrieveLabel.grid(column=1, row=rowI)
service_RetrieveInput.grid(column=2, row=rowI)
service_RetrieveButton.grid(column=3, row=rowI)
rowI+=1



#v Handle Adding new Account Infomation v





window.mainloop()