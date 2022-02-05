import datetime
from random import choice
from smtplib import SMTP

my_email = "test.email.udemy@gmail.com"
password = "nZNZs3iya7eDw7h"

cur_day = datetime.datetime.today().weekday()
if cur_day == 4:
    with open("./day32/Birthday Wisher (Day 32) start/quotes.txt") as motiv_file:
        quotes = motiv_file.readlines()
        quote = choice(quotes)

    with SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
        from_addr=my_email,
        to_addrs= "2021ucs0080@iitjammu.ac.in",
        msg= f"Subject:Monday motivation\n\n{quote}"
        )






