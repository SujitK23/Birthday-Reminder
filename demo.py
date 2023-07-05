import csv
from datetime import datetime
import smtplib
import pyodbc
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


with open('demo.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    
    for cid in csvFile:
        print(cid)
        cnxn_str = ("Driver={SQL Server};"
            "Server=192.168.0.34,7998;"
            "Database=ETAM_WEB_TAJ;"
            "UID=sa;"
            "PWD=@Admin123$$;")
        cnxn = pyodbc.connect(cnxn_str)
        print("connected")
        cursor = cnxn.cursor()
        #id1=lines id=str(lines)
        id1=cid[0]
        id1=str(id1)
        print(id1)

        query="select Name,Date_Birth,email from ET_M_EMPLOYEE where CID=" + id1 + " and Date_Birth is Not NULL and email is NOT NULL and Name like '%S'"

        data=cursor.execute(query)
        result = cursor.fetchall()
        final_result = [list(i) for i in result]
        #print(final_result)

        BirthdayBoy = []
        for i in final_result:
            fetched_date_str = i[1]
            fetched_date = datetime.strptime(fetched_date_str, "%d/%m/%Y").date()
            today = datetime.today().date()
            if fetched_date.month == today.month and fetched_date.day == today.day:
                name = i[0]
                BirthdayBoy.append(i[0])
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.ehlo()
                s.starttls()
                s.ehlo()

                s.login("attendanceportal@sentry.co.in", "@Wyse123")
                subject = "Happy Birthday "
                message = """
        <html>
        <body>
        <h2>Wish You Many Many Happy Returns of The Day </h2>
        <p>Dear """+ name  +""",</p>
        <p>Wishing you a fantastic birthday filled with joy, laughter, and wonderful memories!</p>
        <p>May this day be as special as you are!</p>
        <p>Congratulations on your achievements and best wishes for continued success!</p>
        
        <img src="https://presence.attendanceportal.com/etam_prime/assets/hbd.gif" >
        <p>Best regards,</p>
        <h2>Wyse Biometrics Systems</h2>
        </body>
        </html>
    """
                #with open('hbd.gif', 'rb') as image_file:
                 #   image_data = image_file.read()
                msg = MIMEMultipart()
                msg['From'] = "Wyse Biometrics Systems"
                msg['Subject'] = subject 
                msg.attach(MIMEText(message, 'html'))
                message1=msg.as_string()

                print(BirthdayBoy)
                s.sendmail("attendanceportal@sentry.co.in", i[2], message1)
                s.close()
            elif BirthdayBoy:
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.ehlo()
                s.starttls()
                s.ehlo()

                s.login("attendanceportal@sentry.co.in", "@Wyse123")
                message = """From: WYSE Biometrics Systems Birthday Reminder Mail
Subject: BirthDay Reminder.
Dear """ + i[0] + """,

Your Colleague """ + BirthdayBoy[0] + """ has a birthday Today

Regards,
WYSE Biometrics Systems
"""
                print(BirthdayBoy)
                print(i[2])
                s.sendmail("attendanceportal@sentry.co.in", i[2], message)
                s.close()



        
        

        



    
