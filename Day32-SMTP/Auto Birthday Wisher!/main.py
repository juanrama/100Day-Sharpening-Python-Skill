import smtplib
import datetime as dt
import random
import os
import pandas as pd

email = "76.zulfikar@gmail.com"
pswrd = "jfmnscbvjtzpzzja"

birthday_wish = os.listdir("letter_templates")

birthday_data = pd.read_csv("birthdays.csv")

for i in range(len(birthday_data)):
    if birthday_data.day[i] == dt.datetime.now().day:
        with open(f'./letter_templates/{random.choice(birthday_wish)}', "r") as wish:
            text = wish.read()
            text = text.replace("[NAME]", birthday_data.name[i])
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connect:
            connect.starttls()
            connect.login(user=email,password=pswrd)
            connect.sendmail(from_addr=email,
                            to_addrs=birthday_data.email[i], 
                            msg=f"Subject:Motivasi Ges\n\n{''.join(text)}")




