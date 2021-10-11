import urllib.request
import urllib.parse
import os
import random
import math

def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)


# *Checks OTP with the otp recevied from the GET Request
def generatingOTP(number):

    number_with_code = "+91"+number
    OTP = generateOTP()
    apikey="NTE3NzQzNjU2OTZmNTY2MzY1NTk0ODM3Nzk3NDU0NDQ"
    body=" "+OTP+"is Your OTP for confirmation of Placing the order as Cash on delivery and is Valid for 5 minutes only",
    resp =  sendSMS(apikey,number_with_code,7756078806,body)
    return OTP