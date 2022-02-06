import datetime
from random import choice
from smtplib import SMTP
import pandas

my_email = "test.email.udemy@gmail.com"
password = "" #Obviously, you won't get the password


letter_list = [
    "./day32/birthday-wisher-extrahard-start/letter_templates/letter_1.txt",
    "./day32/birthday-wisher-extrahard-start/letter_templates/letter_2.txt",
    "./day32/birthday-wisher-extrahard-start/letter_templates/letter_3.txt"
]


today = datetime.datetime.now()
data = pandas.read_csv("./day32/birthday-wisher-extrahard-start/birthdays.csv")
birthdays = data.to_dict()

for key in range(len(data)):
    if birthdays["month"][key] == today.month and birthdays["day"][key] == today.day:
        
        with open(choice(letter_list)) as happy_file:
            letter = happy_file.read()
            letter1 = letter.replace("[NAME]", birthdays['name'][key])
        
        with SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
            from_addr=my_email,
            to_addrs= birthdays["email"][key],
            msg=f"Subject:Happy Birthday!\n\n{letter1}"
            )











