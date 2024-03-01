import smtplib
import datetime as dt
import random

email = "76.zulfikar@gmail.com"
pswrd = "jfmnscbvjtzpzzja"

quote = []

send_date = 1

with open("quotes.txt", "r") as quotes:
    quote = [i for i in quotes.readlines()]

if dt.datetime.now().day == send_date:
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connect:
        connect.starttls()
        connect.login(user=email,password=pswrd)
        connect.sendmail(from_addr=email,
                        to_addrs="76.zulfikar@gmail.com", 
                        msg=f"Subject:Motivasi Ges\n\n{random.choice(quote)}")
