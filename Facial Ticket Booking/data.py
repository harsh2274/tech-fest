import mysql.connector
from datetime import date
from datetime import datetime , timedelta
import datetime

def mail_ch(lis):
    connection = mysql.connector.connect(host='localhost',
                                            database='try',
                                            user='root',
                                            password='855fc1@NOV25')
    cursor = connection.cursor()
    for email in lis :
        today = date.today()
        time = datetime.datetime.now()
        c="insert into main(Name,Email,Date,Time,Disabality,Source,HashValue,Validate) Values('{}','{}','{}','{}','{}','{}','{}','{}')".format("",email,today,time,"no","","","Face")
        cursor.execute(c)
        connection.commit()
        print(email, "Amount has been deducted from your Account")