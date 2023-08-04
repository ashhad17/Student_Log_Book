import datetime
from tkinter import *
from tkinter import messagebox
import DBConnect
from functools import partial
class Logbook:
    #logbook GUI
    def __init__(self):
        self.dt = datetime.datetime.now()
        #print(dt)
        #self.listOfId = list()
        #self.buttons = []
        i = 2
        slno = 1
        #getting db con
        self.con = DBConnect.connect_db()
        #creating cur in db
        self.cur = self.con.cursor()
        self.query = "select * from student_logbook where DATE(dt_login) = '"+str(self.dt.date())+"';"
        self.cur.execute(self.query)
        '''for row in self.cur.fetchall():
            print(row)'''
        self.win = Tk()
        self.win.title("Student Logbook")
        self.win.minsize(700,250)
        #self.win.resizable(0,0)
        #heading
        self.currentdateL = Label(self.win,text="Date : " + str(self.dt.date()),relief = RAISED,bd = 8,font = ("Comic Sans MS",14)).grid(row=0,column=0)
        #table
        self.slNoL = Label(self.win,text="Sl No",font = ("Comic Sans MS",12)).grid(row=1,column=0)
        self.studentIdL = Label(self.win,text="Student ID No",font = ("Comic Sans MS",12)).grid(row=1,column=1)
        self.studentnameL = Label(self.win,text="Student Name",font = ("Comic Sans MS",12)).grid(row=1,column=2)
        self.coursenameL = Label(self.win,text="Student Course",font = ("Comic Sans MS",12)).grid(row=1,column=3)
        self.dt_loginL = Label(self.win,text="Student Login",font = ("Comic Sans MS",12)).grid(row=1,column=4)
        self.dt_logout = Label(self.win,text="Student Logout",font = ("Comic Sans MS",12)).grid(row=1,column=5)
        #list of students
        for row in self.cur.fetchall():
            self.listOfId = row[0]
            #print(self.listOfId)
            #print(len(row))
            for j in range(0,len(row)):
                #print(j)
                if(j == 0):
                    self.slNoE = Entry(self.win,width = 6,font = ("Comic Sans MS",12) )
                    self.slNoE.grid(row=i,column=j)
                    self.slNoE.insert(0,str(slno))
                    #self.studentIdE.config(state = DISABLED)
                    self.slNoE.bind("<Key>", lambda a: "break") #breaks when any key is pressed
                    
                self.studentIdE = Entry(self.win,font = ("Comic Sans MS",12))
                self.studentIdE.grid(row=i,column=j+1)
                self.studentIdE.insert(0,str(row[j]))
                #self.studentIdE.config(state = DISABLED)
                self.studentIdE.bind("<Key>", lambda a: "break") #breaks when any key is pressed      
            i = i + 1
            slno = slno + 1
        self.win.mainloop()
    
# o1 = Logbook()

