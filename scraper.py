
import requests
import smtplib
from bs4 import BeautifulSoup
import math

url = 'https://www.amazon.in/realme-Security-Enabled-Tracking-Intruder/dp/B08LZH4FYQ/ref=sr_1_1?crid=2W0PUBN1NVB7R&dchild=1&keywords=realme+camera+360+1080p+wifi&qid=1610940641&sprefix=Realme+Camera+360%2Caps%2C284&sr=8-1'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

def check_price():

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = math.trunc(float(price[2:].replace(',', '')))
    print(title)

    if(price <+ 2450):
        print('Best Price Available, Time to buy')
        # Call send_email() Function with title param
        # send_email(title)
    else:
        print('Looks like this isn\'t the right time to buy')
