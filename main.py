import requests
import json
import smtplib
import time
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#Client's Inputs
set_price=float(input("Get alert for price:\n"))
receiver_mail = input("Client Address:- paperhands@gmail.com\n")
time_sec = int(input("Enter time in minutes:\n"))
#Sender's inputs
sender_mail = input("Sender's Address:- example@gmail.com\n")
password = getpass.getpass("Sender's pass: xyz#toTheM00n\n")

def send_mail_down(sender_mail,password,receiver_mail):
    #Setting Up the mime
  msg = MIMEMultipart()
  password = password
  msg['From'] = sender_mail
  msg['To'] = receiver_mail
  msg['Subject'] = "Price Alert!!"
  message = "Your price is down."
  
  msg.attach(MIMEText(message, 'plain'))
  
  server = smtplib.SMTP('smtp.gmail.com: 587')
  
  server.starttls()
  server.login(msg['From'], password)

  server.sendmail(msg['From'], msg['To'], message)
  server.quit()
  print("Mail is sent successfully.")

def send_mail_up(sender_mail,password,receiver_mail):
    #Setting Up the mime
  msg = MIMEMultipart()
  password = password
  msg['From'] = sender_mail
  msg['To'] = receiver_mail
  msg['Subject'] = "Price Alert!!"
  message = "Your price is Up."
  
  msg.attach(MIMEText(message, 'plain'))
  
  server = smtplib.SMTP('smtp.gmail.com: 587')
  
  server.starttls()
  server.login(msg['From'], password)

  server.sendmail(msg['From'], msg['To'], message)
  server.quit()
  print("Mail is sent successfully.")

url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'
response = requests.get(url)
#JSON output keys:
#[{"id": "currency_name" ,"symbol": "ABC","image":"URL","current_price"...},{},]
prices = response.json()
#This gets the details of first crypto in the list which is bitcoin
currency = prices[0]
krypto_price = currency['current_price']#stores the latest price
#User input price
def alert(sender_mail,password,receiver_mail, set_price):
    if krypto_price < float(set_price):
        print("Price of",currency['id'],"is below ",set_price)
        #sending mail function triggered
        send_mail_down(sender_mail,password,receiver_mail)
    elif krypto_price > float(set_price):
        print("Price of",currency['id'],"is above ",set_price)
        #sending mail function triggered
        send_mail_up(sender_mail,password,receiver_mail)

while(True):
    alert(sender_mail,password,receiver_mail, set_price)
    time.sleep(time_sec*60)#Delay by 10 mins