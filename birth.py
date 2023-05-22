from datetime import date
import emoji
import smtplib
print("\U0001F600")

li = [
{"name":"Avdhut Sakhare","email":"ams@wyse.co.in","dob":"2023-05-18"},
 {"name":"Rahul","email":"rahuls@wyse.co.in","dob":"2023-05-14"},
{"name":"Ganesh","email":"ganeshmale77@gmail.com","dob":"2023-05-15"},
{"name":"Nikhil","email":"dev2@wyse.co.in","dob":"2023-05-12"},
{"name":"Devarshi","email":"dev1@wyse.co.in","dob":"2023-05-12"},
{"name":"Aniket","email":"dev3@wyse.co.in","dob":"2023-05-12"},
{"name":"Sagar","email":"dev4@wyse.co.in","dob":"2023-05-12"},
{"name":"Kuldip","email":"support@wyse.co.in","dob":"2023-05-12"},
{"name":"Mrunal Nisal","email":"mrn@wyse.co.in","dob":"2023-05-20"},
{"name":"Gauri","email":"gup@wyse.co.in","dob":"2023-05-12"},
{"name":"Shailesh","email":"skm@wyse.co.in","dob":"2023-05-11"},
{"name":"Ankita","email":"ankita@wyse.co.in","dob":"2023-05-11"},
{"name":"Yogedra Sir","email":"ydw@wyse.co.in","dob":"2023-05-11"},
{"name":"Nilam","email":"production@wyse.co.in","dob":"2023-05-11"},
{"name":"Mithali","email":"mitalibhole2017@gmail.com","dob":"2023-05-15"},
{"name":"Sachin","email":"support2@wyse.co.in","dob":"1997-06-01"}
]
print(li)
BirthdayBoy = []
for i in li:
    if (str(date.today()) == i.get("dob")):
        name = i.get("name")
        BirthdayBoy.append(i.get("name"))
        print(BirthdayBoy)
today = date.today()
print("Today's date:", today)
for i in li:
    print(i.get("dob"))
    if (str(date.today()) == i.get("dob")):
        name = i.get("name")
        BirthdayBoy.append(i.get("name"))
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
                
        s.login("attendanceportal@sentry.co.in", "@Wyse123")
                # message = "Hi Your Friend "+ BirthdayBoy[0] +" have a birthday today"
        message1 = """From: WYSE Biometrics Systems Birthday Mail
Subject: BirthDay Reminder.
Dear """+ name  +""",

Wish you Many Many Happy Returns Of The Dear """+ name +""" 
Have a great sucess in your life,Wishing you a wonderful day as you celebrate another year of life! 
May your day be filled with all the joys that you hope for.

Regards,
WYSE Biometrics Systems
"""
        print(BirthdayBoy)
        s.sendmail("attendanceportal@sentry.co.in", i.get("email"), message1)
        s.close()
    if (str(date.today()) != i.get("dob")):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        
        s.login("attendanceportal@sentry.co.in", "@Wyse123")
        # message = "Hi Your Friend "+ BirthdayBoy[0] +" have a birthday today"
        message = """From: WYSE Biometrics Systems Birthday Mail
Subject: BirthDay Reminder.
Dear Team,

Your Colleague """ + BirthdayBoy[0] + """ Ma'am has a birthday Today

Regards,
WYSE Biometrics Systems
"""
        print(BirthdayBoy)
        s.sendmail("attendanceportal@sentry.co.in", i.get("email"), message)
        s.close()
        
