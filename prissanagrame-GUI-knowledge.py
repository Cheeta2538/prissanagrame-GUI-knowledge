
from tkinter import*
from tkinter import ttk #theme of tk
from tkinter import messagebox
from PIL import Image,ImageTk

##########กำหนดหน้าจอโปรแกรม###########
GUI = Tk() #นี่คือหน้าจอหลักของโปรแกรม
GUI.title('ทายภาพปริศนา') #นี่คือชื่อโปรแกรม
GUI.geometry('1000x1000') #นี่ืคือขนาดโปรแกรม


#####################ชื่อเกมส์############
L1 = Label(GUI, text='ทายภาพปริศนา', font=('Angsana New', 30), fg='blue')
L1.pack()
L1.place(x=150,y=20)

###################กล่องข้อความเฉลย################################
def Button1():
    text = 'เฉลย1'
    messagebox.showinfo(text,'ข้าวมันไก่') 
def Button2():
    text = 'เฉลย2'
    messagebox.showinfo(text,'เห็ดหูหนู')
def Button3():
    text = 'เฉลย3'
    messagebox.showinfo(text,'มะรุม')
######################################################
FB1 = Frame(GUI)
FB1.place(x=50,y=80)
B1=ttk.Button(FB1,text='ภาพที่1',command=Button1)
B1.pack(ipadx=20,ipady=20)

FB2 = Frame(GUI)
FB2.place(x=50,y=180)
B2=ttk.Button(FB2,text='ภาพที่2',command=Button2)
B2.pack(ipadx=20,ipady=20)

FB3 = Frame(GUI)
FB3.place(x=50,y=280)
B3=ttk.Button(FB3,text='ภาพที่3',command=Button3)
B3.pack(ipadx=20,ipady=20)
#######################################################

img1 = ImageTk.PhotoImage(Image.open("images/111.png"))
label = Label(GUI,image = img1)
label.place(x=350,y=80)

img2 = ImageTk.PhotoImage(Image.open("images/222.png"))
label = Label(GUI,image = img2)
label.place(x=350,y=180)

img3 = ImageTk.PhotoImage(Image.open("images/333.png"))
label = Label(GUI,image = img3)
label.place(x=350,y=280)
######################################################

GUI.mainloop()
