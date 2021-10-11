import smtplib
import ssl
import os
import random
import math


# * Generating 4-Digit Random Numbers

def generatemailOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


# *Checks OTP with the otp recevied from the GET Request
def generatingmailOTP(mailid):
    
    receiver_mail = mailid
    OTP = generatemailOTP()
    sender_mailid = "gingertestuser1245@gmail.com"
    passwrd = "stoxvnvworbwyxcs"
    #sender_mailid = "testing.seriinfotech@gmail.com"
    #passwrd = "acerASPIREVX15"
    body = "Your OTP for Resting Password is"+OTP+" and is Valid for 5 minutes only"
    server = smtplib.SMTP('smtp.gmail.com','587')
    context = ssl.create_default_context()
    server.starttls(context=context)
    server.login(sender_mailid,passwrd)
    server.sendmail(sender_mailid,receiver_mail,body)
    return OTP
