# import smtplib
#
# my_email = ""
# password = ""
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="",
#         msg="Subject:Hello \n\nThis is the body of my email"
#     )
# import random
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=2000, month=11, day=21)
# print(date_of_birth)

#monday motivational quotes


# import smtplib
# import datetime as dt
# import random
#
# now = dt.datetime.now()
# day_of_week = now.weekday()
# with open(file="quotes.txt") as quote_file:
#     text = quote_file.read()
# quotes = text.split("\n")
# print(random.choice(quotes))
#
# my_email = ""
# password = ""
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="",
#         msg=f"Subject:Hello \n\n{random.choice(quotes)}"
#     )


import smtplib
import datetime as dt
import random

MY_EMAIL = ""
MY_PASSWORD = ""

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Monday Motivation \n\n{quote}"
        )
