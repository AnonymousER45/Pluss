import os
import random
import math

from twilio.rest import Client


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


# *Checks OTP with the otp recevied from the GET Request
def generatingOTP(number):

    number_with_code = "+91"+ number
    OTP = generateOTP()

    # Code for Twilio
    account_sid = 'AC74af50f0be3969928349ceea8a18e8e4'
    auth_token = 'af46f0b4bc239150d8bc833c18d4a6de'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=" "+OTP+"is Your OTP for confirmation of Placing the order as Cash on delivery and is Valid for 5 minutes only",
                         from_='+13852444524',
                         to=number_with_code)

    return OTP
#1. You have successfully placed your order on Pluscrown. Your order ID is $123567ABC. Track your order on our website in "My Orders" section.
#2. Your order ID $123567ABC is ready and is out for delivery. Please pay Rs. xyz in cash.
#3. Your order ID $123567ABC is ready for the shipment and would be delivered in 2-3 working days. Thank you.
#4. Your order ID $123567ABC is ready and is out for delivery. Our delivery boy would knock your door soon.
#5. Your Order ID $123567ABC is delivered Successfully.


def orderplaced(number,orderid):
    number_with_code = "+91"+number
    order_id= "PC2021"+str(orderid)
    # Code for Twilio
    account_sid = 'AC74af50f0be3969928349ceea8a18e8e4'
    auth_token = 'af46f0b4bc239150d8bc833c18d4a6de'
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body="You have successfully placed your order on Pluscrown. Your order ID is"+order_id+ ". You  can except delivery with 3-4 days.",
                         from_='+13852444524',
                         to=number_with_code)

    return order_id

def orderoutfordelivery(number,orderid):
    number_with_code = "+91"+number
    order_id= "PC2021"+str(orderid)
    # Code for Twilio
    account_sid = 'AC74af50f0be3969928349ceea8a18e8e4'
    auth_token = 'af46f0b4bc239150d8bc833c18d4a6de'
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body="Your order "+order_id+ " is ready and is out for delivery. Kindly make payment in cash if Outstanding is pending and ignore if Already Paid",
                         from_='+13852444524',
                         to=number_with_code)

    return order_id


def forgotpassOTP(number):
    newnumber = str(number)
    number_with_code = "+91"+ newnumber
    OTP = generateOTP()
    # Code for Twilio
    account_sid = 'AC74af50f0be3969928349ceea8a18e8e4'
    auth_token = 'af46f0b4bc239150d8bc833c18d4a6de'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=" "+OTP+"is Your OTP for confirmation of Placing the order as Cash on delivery and is Valid for 5 minutes only",
                         from_='+13852444524',
                         to=number_with_code)

    return OTP
