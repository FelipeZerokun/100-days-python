# SMTP = Simple Mail Transfer Protocol
'''
Gmail: smtp.gmail.com

Hotmail: smtp.live.com

Outlook: outlook.office365.com

Yahoo: smtp.mail.yahoo.com
'''

import smtplib
from random import choice
import datetime as dt

with open("quotes.txt", "r") as file:
    messages = file.readlines()

message = choice(messages)
print(message)

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
weekday = now.weekday()
time = now.time()
hour = time.hour
minutes = time.minute
seconds = time.second

print(f"today is {WEEKDAYS[weekday]}, the {day} of {MONTHS[month]} {year}. It is {hour}:{minutes}")

my_birthday = dt.datetime(year=1993, month=3, day= 23, hour= 15)
print(my_birthday)

if WEEKDAYS[weekday] == "Monday":
    print("I will send a motivational email")

    with smtplib.SMTP("smtp.office365.com", port= 587) as connection:
        connection.starttls()
        connection.login(user="your_mail@hotmail.com", password="password123")
        connection.sendmail(from_addr="your_mail@hotmail.com", to_addrs="another_mail@hotmail.com",
                            msg=f"Subject:Motivation\n\nEs lunes para motivarse! \n{message}. \nNo te rindas jamás!")

