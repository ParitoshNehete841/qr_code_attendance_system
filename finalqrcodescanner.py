from __future__ import print_function
from tkinter import *
import cv2 #openswebcam
import numpy as np #for makinh array of polygon while showcasing data on webcam
from pyzbar.pyzbar import decode #decoder
import csv


#qrscanner frontend(tkinter)
class qr_scanner:
    def __init__(self,root):
        self.root=root
        self.root.geometry("720x720+200+50")
        self.root.title("QR Scanner")
        self.root.resizable(False,False)

        title=Label(self.root,text="   QR Scanner",font=("times new roman",30),bg='black',fg='white',anchor='w').place(x=0,y=0,relwidth=1)

        scanner_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        scanner_Frame.place(x=20,y=55,width=680,height=550)


        self.qr_code=Label(scanner_Frame,text='Please click for Taking Attendance',font=('times new roman',15),bg='white',fg='red',bd=1,relief=RIDGE)
        self.qr_code.place(x=00,y=00,width=680,height=550)
        #self.qr_code.


        btn = Button(self.root, text="Start Taking Attendance", command=self.qrcodescanner,
                  font=("times new roman", 18, 'bold'),
                  bg='black', fg='white').place (x=215, y=650, width=300, height=30)


    #qrscanner backend
    def qrcodescanner(self):
        cap = cv2.VideoCapture(0) #openwebcam
        cap.set(3, 480)
        cap.set(3, 480)
        while True:
            success, img = cap.read()
            for barcode in decode(img):
                self.mydata = barcode.data.decode('utf-8') #decoding qr
                print(self.mydata)
                self.pts = np.array([barcode.polygon], np.int32)  #showcase data on cam
                self.pts = self.pts.reshape(-1, 1, 2)
                cv2.polylines(img, [self.pts], True, (34, 139, 34), 2)
                cv2.putText(img, self.mydata, (50, 50), cv2.FONT_ITALIC, 0.9, (255, 0, 0), 2)

                #csv file writer on attendance.csv
                header = ['name', 'dept', 'rollno', 'year']
                rows = [self.mydata]
                with open ('/Users/grishma/PycharmProjects/skha/attendance.csv','wt',encoding='UTF8',newline='') as f:
                    writer = csv.writer(f, quotechar=" ")
                    writer.writerow(header)
                    writer.writerow(rows)
                    f.close()

                #alternate
                # header = ['name','dept','rollno','year']
                # f =open('/Users/grishma/PycharmProjects/skha/attendance.csv','w',encoding='UTF8',newline='')
                # rows=[self.mydata]
                #
                # writer = csv.writer(f)
                # writer.writerow(header)
                # writer.writerow(rows)
                # f.close()
            cv2.imshow ('QR Scanner', img)
            cv2.waitKey (1)


root=Tk()
obj= qr_scanner(root)
root.mainloop()