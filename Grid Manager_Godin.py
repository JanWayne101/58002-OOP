from tkinter import *

window = Tk()

window.title("Grid Manager")
window.geometry("400x300+10+10")
#button = Button_(window, width=3)
#button.grid(row=0, column=0)
txt = Entry(window, bd=2, justify="center")
txt.grid(row=0, column=0)
txt.insert(0, "row 0 column 0")

txt1 = Entry(window, bd=2, justify="center")
txt1.grid(row=0, column=1)
txt1.insert(0, "row 0 column 1")

txt2 = Entry(window, bd=2, justify="center")
txt2.grid(row=0, column=2)
txt2.insert(0, "row 0 column 2")

txt3 = Entry(window, bd=2, justify="center")
txt3.grid(row=1, column=0)
txt3.insert(0, "row 1 column 0")

txt3 = Entry(window, bd=2, justify="center")
txt3.grid(row=2, column=0)
txt3.insert(0, "row 2 column 0")

txt3 = Entry(window, bd=2, justify="center")
txt3.grid(row=1, column=1)
txt3.insert(0, "row 1 column 1")

txt3 = Entry(window, bd=2, justify="center")
txt3.grid(row=2, column=1)
txt3.insert(0, "row 2 column 1")

txt3 = Entry(window, bd=2, justify="center")
txt3.grid(row=1, column=2)
txt3.insert(0, "row 1 column 2")

txt3 = Entry(window, bd=2, justify="center")
txt3.grid(row=2, column=2)
txt3.insert(0, "row 2 column 2")

txt3 = Entry(window, bd=2, justify="center")
txt3.grid(row=3, column=0)
txt3.insert(0, "row 3 column 0")

txt3 = Entry(window, bd=2, justify="center")
txt3.grid(row=3, column=1)
txt3.insert(0, "row 3 column 1")

txt3 = Entry(window, bd=2, justify="center")
txt3.grid(row=3, column=2)
txt3.insert(0, "row 3 column 2")


window.mainloop()