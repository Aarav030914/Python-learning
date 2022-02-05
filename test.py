from smtplib import SMTP
my_email = "test.email.udemy@gmail.com"
password = "nZNZs3iya7eDw7h"
with SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
            from_addr=my_email,
            to_addrs= "ajaarav14@gmail.com",
            msg=f"Subject:Happy Birthday!\n\n"
            )