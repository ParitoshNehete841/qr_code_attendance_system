from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage


class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("Qr Generator for student")
        self.root.resizable(False,False)

        title=Label(self.root,text=" Qr Code Generator",font=("times new roman",40),bg='#808080',fg='white',anchor='w').place(x=0,y=0,relwidth=1)

        self.var_stud_code=StringVar()
        self.var_stud_name=StringVar()
        self.var_stud_department=StringVar()
        self.var_stud_year=StringVar()

        stud_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        stud_Frame.place(x=50,y=100,width=500,height=380)

        stud_title=Label(stud_Frame,text=" Student",font=("Arial",20),bg='#FF0000',fg='black',anchor='w').place(x=0,y=0,relwidth=1)
        lbl_stud_code=Label(stud_Frame,text="Student Roll No",font=("times new roman",15,'bold'),bg='white').place(x=20,y=60)

        lbl_name=Label(stud_Frame,text="Name",font=("times new roman",15,'bold'),bg='white').place(x=20,y=100)
        lbl_department=Label(stud_Frame,text="Department",font=("times new roman",15,'bold'),bg='white').place(x=20,y=140)
        lbl_Year=Label(stud_Frame,text="Year",font=("times new roman",15,'bold'),bg='white').place(x=20,y=180)

        txt_stud_code=Entry(stud_Frame,text="Student Roll No",font=("times new roman",15,),textvariable=self.var_stud_code,bg='lightyellow').place(x=200,y=60)
        txt_name=Entry(text="Name",font=("times new roman",15,),textvariable=self.var_stud_name,bg='lightyellow').place(x=250,y=200)
        txt_department=Entry(text="Department",font=("times new roman",15,),textvariable=self.var_stud_department,bg='lightyellow').place(x=250,y=240)
        txt_Year=Entry(text="Year",font=("times new roman",15,),textvariable=self.var_stud_year,bg='lightyellow').place(x=250,y=280)

        btn_generator=Button(stud_Frame,text='QR Generator',command=self.generate,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=100,y=281,width=180,height=30)
        btn_clear=Button(stud_Frame,text='Clear',command=self.clear,font=("times new roman",18,'bold'),bg='#607d8b',fg='white').place(x=350,y=281,width=120,height=30)

        self.msg=''
        self.lbl_msg=Label(stud_Frame,text=self.msg,font=("times new roman",20),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=330,relwidth=1)

        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')

        qr_Frame.place(x=600,y=100,width=250,height=350)
        stud_title=Label(qr_Frame,text=" Student QR Code",font=("Arial",20),bg='#FF0000',fg='black',anchor='w').place(x=0,y=0,relwidt=1)

        self.qr_code=Label(qr_Frame,text="QR code \nNot Available",font=('times new romam',15),bg='#3f51b5',fg='white')
        self.qr_code.place(x=35,y=100,width=180,height=180)

    def clear(self):
        self.var_stud_code.set('')
        self.var_stud_name.set('')
        self.var_stud_department.set('')
        self.var_stud_year.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)

    def generate(self):
        if (self.var_stud_code.get()==''or self.var_stud_name.get()==''or self.var_stud_department.get()==''or self.var_stud_year.get()==''):
            self.msg='All Fields Are Required!!!'
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Student Rollno: {self.var_stud_code.get()}\nStudentName:{self.var_stud_name.get()}\nDepartment:{self.var_stud_department.get()}\nYear:{self.var_stud_year.get()}")
            qr_code=qrcode.make(qr_data)
            print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("Student/stud_"+str(self.var_stud_code.get())+'.png')

            self.im=ImageTk.PhotoImage(file="Student/stud_"+str(self.var_stud_code.get())+'.png')
            self.qr_code.config(image=self.im)
            self.msg='QRCODE Generated Successfully!!'
            self.lbl_msg.config(text=self.msg,fg='green')

root=Tk()
obj =Qr_Generator(root)
root.mainloop()