import mysql.connector
def connect_db():
    con = mysql.connector.connect(user = "root",password = "",host = "localhost",database = "computech_as")
    print(con)
    if(con):
        print("Connection Success")
    else:
        print("Connection Un-Success")
    return con

