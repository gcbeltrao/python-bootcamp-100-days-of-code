import smtplib
import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

with open("quotes.txt") as message:
    motivational_message = message.readlines()
    email_message = random.choice(motivational_message)


if day_of_week == 1:
    MY_EMAIL = "email@email.com"
    PASSWORD = ""  # PUT YOUR PASSWORD HERE

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Motivational\n"
                                                                                          f"\n{email_message}")
