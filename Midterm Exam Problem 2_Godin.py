from tkinter import *
class Myname:
    def __init__(self,win):

        self.lbl0 = Label(win,text="My Fullname")
        self.lbl0.place(x=250,y=50)

        self.lbl1 = Label(win, text= "Enter Given Name: ")
        self.lbl1.place(x=150,y=75)

        self.lbl2 = Label(win, text="Enter Middle Name:")
        self.lbl2.place(x=150,y=105)

        self.lbl3 = Label(win, text="Enter Last Name: ")
        self.lbl3.place(x=150,y=135)

        self.lbl4 = Label(win, text="My Full Name is: ")
        self.lbl4.place(x=150,y=175)

        self.txt1 = Entry(win,bd=2)
        self.txt1.place(x=300,y=80)

        self.txt2 = Entry(win,bd=2)
        self.txt2.place(x=300,y=110)

        self.txt3 = Entry(win,bd=2)
        self.txt3.place(x=300,y=140)

        self.txt4 = Entry(win,bd=2)
        self.txt4.place(x=300,y=170)


        self.btnsfn = Button(wind,text="Show Full Name")
        self.btnsfn.place(x=270,y=250)
        self.btnsfn.bind('<Button-1>',self.sfn)

        self.btncle = Button(win,text="Clear")
        self.btncle.place(x=300, y=300)
        self.btncle.bind('<Button-1>',self.cle)


    def sfn(self,sfn):
        self.text4.delete(0,'end')
        name1 = str(self.text1.get())
        name2 = str(self.text2.get())
        name3 = str(self.text3.get())
        result = name1 + " " + name2 + " " + name3
        self.text4.insert(END, str(result))

    def cle(self,cle):
        self.txt3.delete(0,'end')
        self.txt3.insert(END,str())
        self.txt1.delete(0, 'end')
        self.txt1.insert(END, str())
        self.txt2.delete(0, 'end')
        self.txt2.insert(END, str())



wind = Tk()
mywind = Myname(wind)
wind.geometry("600x400+10+10")
wind.title("Midterm Exam Problem 2")
wind.mainloop()

