import smtplib
import random

def send_email(email_variable):
    x=random.randint(100000,999999)
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('some@email.com','api_key')
    server.sendmail('some@email.com',email_variable,' Thank You for Choosing Mitahara, Your OTP is %d , Please do not share it with anyone. '%(x))
    print('Mail Sent')
    return x

#driver code
#y=send_email('somanathnayak1304@gmail.com')
#print(y)
