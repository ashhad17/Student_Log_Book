import datetime
from tkinter import *
# from tkinter import messagebox
import DBConnect
from functools import partial
class Logbook:
    #logbook GUI
    def __init__(self):
        dt = datetime.datetime.now()
        print(dt)
        self.listOfId = list()
        self.buttons = []
        i = 1
        #getting db con
        self.con = DBConnect.connect_db()
        #creating cur in db
        self.cur = self.con.cursor()
        self.query = "select * from student_logbook where DATE(dt_login) = '"+str(dt.date())+"' and dt_logout is null;"
        self.cur.execute(self.query)
        '''for row in self.cur.fetchall():
            print(row)'''
        self.win = Tk()
        self.win.title("Student Logbook")
        self.win.minsize(600,250)
        #self.win.resizable(0,0)
        #heading
        self.studentIdL = Label(self.win,text="Student ID No",font = ("Comic Sans MS",12)).grid(row=0,column=0)
        self.studentnameL = Label(self.win,text="Student Name",font = ("Comic Sans MS",12)).grid(row=0,column=1)
        self.coursenameL = Label(self.win,text="Student Course",font = ("Comic Sans MS",12)).grid(row=0,column=2)
        self.dt_loginL = Label(self.win,text="Student Login",font = ("Comic Sans MS",12)).grid(row=0,column=3)
        self.dt_logout = Label(self.win,text="Student Logout",font = ("Comic Sans MS",12)).grid(row=0,column=4)
        #list of students
        for row in self.cur.fetchall():
            self.listOfId = row[0]
            print(self.listOfId)
            #print(len(row))
            for j in range(0,len(row) + 1):
                print(j)
                if(j <= 4):
                    self.studentIdE = Entry(self.win,font = ("Comic Sans MS",12))
                    self.studentIdE.grid(row=i,column=j)
                    self.studentIdE.insert(0,str(row[j]))
                    #self.studentIdE.config(state = DISABLED)
                    self.studentIdE.bind("<Key>", lambda a: "break") #breaks when any key is pressed 
                else:
                    #partial helps to  know which button is pressed
                    self.logoutB = Button(self.win,text="Logout",command = partial(self.OnButtonClick,self.listOfId),font = ("Comic Sans MS",12)).grid(row=i,column=5)
                    self.buttons.append(self.logoutB)
            i = i + 1
        self.win.mainloop()
    def OnButtonClick(self,id):
        print(id)
        dt_logout = str(datetime.datetime.now())
        updt_query = "update student_logbook set dt_logout = '" + dt_logout + "' where id = " + str(id)
        print(updt_query)
        self.cur.execute(updt_query)
        self.con.commit()
        self.con.close()
        #messagebox.showinfo("Information","Success")
        #close window
        self.win.withdraw()
        #redraw window
        o2 = Logbook()
#o1 = Logbook()

