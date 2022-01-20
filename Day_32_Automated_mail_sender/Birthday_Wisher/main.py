##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
from random import randint
import smtplib

# print(file_path)
MY_EMAIL = "feliperojasl.python@hotmail.com"
MY_PASSWORD = "artint2021FZR2303"
today_datetime = dt.datetime.now()
day = today_datetime.day
month = today_datetime.month

bday_data = pd.read_csv('birthdays.csv')
# Using Dictionary Comprehension
# new_dict = {new_key:new_value for (key, value) in dict.items()}

bday_dict = {row["name"]: row["email"] for (index, row) in bday_data.iterrows() if row.month == month and row.day == day}
# print(bday_dict)

if len(bday_dict) > 0:
    # print("There is a birthday!")
    for person in bday_dict.items():
        file_path = f"letter_templates/letter_{randint(1, 3)}.txt"
        # print(person[0])
        with open(file_path) as letter:
            content = letter.read()
            content = content.replace("[NAME]", person[0])
            # print(content)

        with smtplib.SMTP("smtp.office365.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,
                             password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=person[1],
                                msg=f"Subject: Happy Birthday!\n\n{content}")
else:
    print("No birthday today :( ")