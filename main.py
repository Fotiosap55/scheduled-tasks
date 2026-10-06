import datetime as dt
import random
import smtplib
import pandas as pd
import os
# 1. Update the birthdays.csv
data=pd.read_csv('birthdays.csv')
new_data=data.to_dict(orient='records')
today = dt.date.today()
day=today.day
month=today.month
my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("MY_PASSWORD")
# 2. Check if today matches a birthday in the birthdays.csv
with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    for person in new_data:
        if person["day"]==day and person["month"]==month:
            choice=random.randint(1,3)
            letter=f"letter_templates/letter_{choice}.txt"
            with open(letter,"r") as f:
                letter_content=f.read()
            final_letter=letter_content.replace("[NAME]",person["name"])
            connection.sendmail(from_addr=my_email,
                                to_addrs=person["email"],
                                msg=f"Subject:Happy Birthday!\n\n{final_letter}")
