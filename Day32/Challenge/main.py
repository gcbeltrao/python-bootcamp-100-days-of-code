import pandas as pd
import random
import smtplib
import datetime as dt

PLACE_HOLDER = "[NAME]"
MY_EMAIL = "email@email.com"
PASSWORD = "" #PUT YOUR PASSWORD HERE


# 1. Update the birthdays.csv
data = pd.read_csv("birthdays.csv")
dict_data = data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
actual_month = now.month
today = now.day

for person in dict_data:
    month_birthday = person["month"]
    birthday = person["day"]
    name = person["name"]
    email = person["email"]
    if month_birthday == actual_month and birthday == today:
        number = random.randint(1, 3)
        with open(f"letter_templates/letter_{number}.txt") as letter_file:
            letter_content = letter_file.read()
            new_letter = letter_content.replace(PLACE_HOLDER, name)
        print(new_letter)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f"Subject:Happy Birthday!\n\n{new_letter}")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


# 4. Send the letter generated in step 3 to that person's email address.
