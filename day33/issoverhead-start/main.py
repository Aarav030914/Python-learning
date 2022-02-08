import config
import smtplib 

MY_EMAIL = "test.email.udemy@gmail.com"
PASSWORD = "" #Obviously, you won't get the password

MY_LAT = 21.764473
MY_LONG = 72.151932


def send_email():
    
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="2021ucs0080@iitjammu.ac.in",
            msg="Subject:ISS OVERHEAD\n\n Look up! ISS is directly overhead"
        )


if config.check_pos():
    send_email()




