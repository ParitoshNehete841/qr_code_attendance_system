from __future__ import print_function
from tkinter import *
from PIL import Image,ImageTk

class qr_scanner:
    def __init__(self,root,path='/Users/grishma/PycharmProjects/skha/qrcodescanner.py'):
        self.path = path
        self.root=root
        self.root.geometry("720x720+200+50")
        self.root.title("QR Scanner")
        self.root.resizable(False,False)

        title=Label(self.root,text="   QR Scanner",font=("times new roman",30),bg='black',fg='white',anchor='w').place(x=0,y=0,relwidth=1)

        scanner_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        scanner_Frame.place(x=20,y=55,width=680,height=550)
        self.qr_code=Label(scanner_Frame,text='Please click for Taking Attendance',font=('times new roman',15),bg='white',fg='red',bd=1,relief=RIDGE)
        self.qr_code.place(x=00,y=00,width=680,height=550)

        btn= Button(self.root,text="Start Taking Attendance",command=(),font=("times new roman",18,'bold'),bg='black',fg='white').place(x=215,y=650,width=300,height=30)


root=Tk()
obj= qr_scanner(root)
root.mainloop()
