import os
import random
import math

from sendsms.message import SmsMessage

def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


# *Checks OTP with the otp recevied from the GET Request
def generatingOTP(number):

    number_with_code = "+91"+number
    OTP = generateOTP()


    message = SmsMessage(body=" "+OTP+"is Your OTP for confirmation of Placing the order as Cash on delivery and is Valid for 5 minutes only",from_phone='+917756078806',to=number_with_code)
    message.send()
    return OTP
#1. You have successfully placed your order on Pluscrown. Your order ID is $123567ABC. Track your order on our website in "My Orders" section.
#2. Your order ID $123567ABC is ready and is out for delivery. Please pay Rs. xyz in cash.
#3. Your order ID $123567ABC is ready for the shipment and would be delivered in 2-3 working days. Thank you.
#4. Your order ID $123567ABC is ready and is out for delivery. Our delivery boy would knock your door soon.
#5. Your Order ID $123567ABC is delivered Successfully.
