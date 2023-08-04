import datetime
from tkinter import *
from tkinter import messagebox
import DBConnect
class Logbook:
    #logbook GUI
    def __init__(self):
        #getting db con
        self.con = DBConnect.connect_db()
        #creating cur in db
        self.cur = self.con.cursor()    #insert login data
        self.cur1 = self.con.cursor()   #check whether student has logged in or not
        #list var for courses
        courseSlNo = 1
        courseList = ['C','CPP','Java','Python','DOM','DCA','DTP','Tally Prime','Network+','Hardware','CCNA','MCSA','Ethical Hacking','RHCSA','CCNA Security','Android Hacking','Socail Engineering',]
        self.win = Tk()
        self.student_id = StringVar()
        self.student_name = StringVar()
        self.course_name = StringVar()
        self.win.title("Student Logbook")
        self.win.minsize(400,300)
        self.win.resizable(0,0)
        studentIdL = Label(self.win,text="Enter ID No:",font = ("Comic Sans MS",12)).grid(row=0,column=0)
        self.studentIdE = Entry(self.win,textvariable=self.student_id,font = ("Comic Sans MS",12))
        self.studentIdE.grid(row=0,column=1)
        studentnameL = Label(self.win,text="Enter Name:",font = ("Comic Sans MS",12)).grid(row=1,column=0)
        self.studentnameE = Entry(self.win,textvariable=self.student_name,font = ("Comic Sans MS",12))
        self.studentnameE.grid(row=1,column=1)
        coursenameL = Label(self.win,text="Select Course:",font = ("Comic Sans MS",12)).grid(row=2,column=0)
        self.courseListBox = Listbox(self.win,font = ("Comic Sans MS",12))
        #course listbox
        for i in courseList:
            self.courseListBox.insert(courseSlNo,i)
            courseSlNo+=1
        self.courseListBox.grid(row=2,column=1)
        loginB = Button(self.win,text="Login",command=self.studentLogin,font = ("Comic Sans MS",12)).grid(row=3,column=0)
        self.win.mainloop()
    def studentLogin(self):
        #fetch current time,id,name,course of student
        dt_login = datetime.datetime.now()
        #id_no =  self.student_id.get()
        #name = self.student_name.get()
        id_no = self.studentIdE.get()
        name = self.studentnameE.get()
        course = str(self.courseListBox.get(self.courseListBox.curselection()))
        print(id_no,type(id_no))
        print(name)
        print(course)
        print(dt_login)
        #sql query
        #checking student already logged in or not
        query1 = "select DATE(dt_login) from student_logbook where id = '"+str(id_no)+"' and DATE(dt_login) = '"+str(dt_login.date())+"';"
        print(query1)
        if(not self.cur1.execute(query1)):
            row1 = self.cur1.fetchall()
            print(row1)
            if(len(row1) == 0):
                query = "insert into student_logbook values("+str(id_no)+",'"+str(name)+"','"+course+"','"+str(dt_login)+"',"+str('null')+");"
                print(query)
                #execute sql query
                if(not self.cur.execute(query)):
                    messagebox.showinfo("Information","Success")
                    self.win.withdraw()
                else:
                    messagebox.showerror("Error","Can't login")
            else:
                messagebox.showerror("Error","Student has already logged in")
                self.win.withdraw()
        else:
            messagebox.showerror("Error","Fail")
        self.con.commit() #compulsory need be added after insert query
        self.con.close()
        self.reset_fields()
    #feilds reset method
    def reset_fields(self):
        self.studentIdE.delete(0,END)
        self.studentnameE.delete(0,END)
        self.studentIdE.insert(0,'')
        self.studentnameE.insert(0,'')
#o1 = Logbook()

