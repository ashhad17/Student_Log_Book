from tkinter import *
from tkinter import messagebox

import StudentLogBook1
import StudentLogBook2
import ShowStudents
import GenerateExcel
win = Tk()
def login():
    o1 = StudentLogBook1.Logbook()
def logout():
    o2 = StudentLogBook2.Logbook()
def show():
    o3 = ShowStudents.Logbook()
def excel():
    o4 = GenerateExcel.Logbook()
def version():
    messagebox.showinfo("Information", "Version=1.0")
def make_gui():
    win.title("Computech")
    win.state('zoomed') #fullscreen view
    win.resizable(2000,2000)
    welcomeL = Label(win,text = "Student Logbook",font = ("Corbel",36),pady = 20,bd = 8,relief = RAISED).pack(side=TOP)
    version_infoB = Button(win,text = "Version 1.0", relief = RAISED,bd = 4, font = "Fixedsys",command=version).pack(side = BOTTOM)
    loginB = Button(win, command = login ,text = "Login", font = ("Corbel",22),padx = 10).place(x = 480,y = 250)
    logoutB = Button(win, command = logout,text = "Logout",font = ("Corbel",22)).place(x = 640,y = 250)
    showStudnetsB = Button(win, command = show,text = "Show",font = ("Corbel",22)).place(x = 800,y = 250)
    exelB = Button(win, command = excel,text = "Excel",font = ("Corbel",22)).place(x = 940,y = 250)
    win.mainloop()
make_gui()
