from twilio.rest import Client
import smtplib
def send_sms(message):

    account_sid = "AC3e38aa2f1028efc3f4e31ece3082920a"
    account_token = "7a9de64aea4b4560bc2765704e111570"
    client = Client(account_sid, account_token)
    client.messages.create(
        body=message,
        to="+917487853240",
        from_="+19377313747"
    )
def send_email(message, email_id):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(
            user="test.email.udemy@gmail.com",
            password="nZNZs3iya7eDw7h"
        )
        connection.sendmail(
            from_addr="test.email.udemy@gmail.com",
            to_addrs= email_id,
            msg=f"Subject:Flight Deals Update\n\n{message}"
        )
