import datetime
import DBConnect
# import xlwt
import pandas.io.sql as sql
from tkinter import messagebox
class Logbook:
    def __init__(self):
        # connect the mysql with the python
        self.con = DBConnect.connect_db()
        #fetch current date
        p_dt = datetime.datetime.now()
        dt = datetime.datetime.now()
        #p_dt = p_dt.strftime("%d %m %y %I %M %p") #date and time format
        p_dt = p_dt.strftime("%d-%m-%y") #only date format
        print(p_dt)
        print(type(p_dt))
        # read the data
        df=sql.read_sql("select * from student_logbook where DATE(dt_login) = '"+str(dt.date())+"';",self.con)
        # print the data
        #print(df)
        # export the data into the excel sheet
        df.to_excel(p_dt+'.xls')
        messagebox.showinfo("Information","Excel Sheet Generated Successfully")
#o1 = Logbook()







