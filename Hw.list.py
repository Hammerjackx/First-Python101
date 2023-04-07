from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() # หน้าจอหลักของโปรแกรม 
GUI.title('Daily Color') # ชื่อโปรแกรม
GUI.geometry('500x450') # ขนาดของโปรแกรม

L1 = Label(GUI,text='Daily Color',font= ('sukhumvit',30),fg='black')
L1.place(x=165,y=30)


##################
def Button1():
    text = 'สีแดง'
    messagebox.showinfo('วันอาทิตย์',text) #หรืออาจจะเป็น .showwarning , .showerror

FB1 = Frame(GUI) #คล้ายกระดาน ,LabelFrame>>จะมีขอบ
FB1.place(x=200,y=100)
B1 = ttk.Button(FB1,text='Sunday',command=Button1)
B1.pack(ipadx=20,ipady=5)
##################
def Button2():
    text = 'สีเหลือง'
    messagebox.showinfo('วันจันทร์',text) #หรืออาจจะเป็น .showwarning , .showerror

FB2 = Frame(GUI) #คล้ายกระดาน ,LabelFrame>>จะมีขอบ
FB2.place(x=200,y=140)
B2 = ttk.Button(FB1,text='Monday',command=Button2)
B2.pack(ipadx=20,ipady=5)
##################
def Button3():
    text = 'สีชมพู'
    messagebox.showinfo('วันอังคาร',text) #หรืออาจจะเป็น .showwarning , .showerror

FB3 = Frame(GUI) #คล้ายกระดาน ,LabelFrame>>จะมีขอบ
FB3.place(x=200,y=180)
B3 = ttk.Button(FB1,text='Tuesday',command=Button3)
B3.pack(ipadx=20,ipady=5)
##################
def Button4():
    text = 'สีเขียว'
    messagebox.showinfo('วันพุธ',text) #หรืออาจจะเป็น .showwarning , .showerror

FB4 = Frame(GUI) #คล้ายกระดาน ,LabelFrame>>จะมีขอบ
FB4.place(x=200,y=220)
B4 = ttk.Button(FB1,text='Wednesday',command=Button4)
B4.pack(ipadx=20,ipady=5)
##################
def Button5():
    text = 'สีส้ม'
    messagebox.showinfo('วันพฤหัสบดี',text) #หรืออาจจะเป็น .showwarning , .showerror

FB5 = Frame(GUI) #คล้ายกระดาน ,LabelFrame>>จะมีขอบ
FB5.place(x=200,y=260)
B5 = ttk.Button(FB1,text='Thursday',command=Button5)
B5.pack(ipadx=20,ipady=5)
##################
def Button6():
    text = 'สีฟ้า'
    messagebox.showinfo('วันศุกร์',text) #หรืออาจจะเป็น .showwarning , .showerror

FB6 = Frame(GUI) #คล้ายกระดาน ,LabelFrame>>จะมีขอบ
FB6.place(x=200,y=300)
B6 = ttk.Button(FB1,text='Friday',command=Button6)
B6.pack(ipadx=20,ipady=5)
##################
def Button7():
    text = 'สีม่วง'
    messagebox.showinfo('วันเสาร์',text) #หรืออาจจะเป็น .showwarning , .showerror

FB7 = Frame(GUI) #คล้ายกระดาน ,LabelFrame>>จะมีขอบ
FB7.place(x=200,y=340)
B7 = ttk.Button(FB1,text='Saturday',command=Button7)
B7.pack(ipadx=20,ipady=5)
##################





GUI.mainloop()
