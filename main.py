from bs4 import BeautifulSoup
from random import randint
import random
import requests
import string
import time

user_agent = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
letters = string.ascii_lowercase
delay = float(input("delay per each request sent?\t=> "))

while True:
    iden = ( ''.join(random.choice(letters)for i in range(randint(3, 11))))
    url = f"http://prnt.sc/{iden}"
    time.sleep(delay)
    reqs = requests.get(url, headers=user_agent) 
    soup = BeautifulSoup(reqs.text, 'html.parser') 
    for title in soup.find_all('title'): 
        if title.get_text() == "Lightshot — screenshot tool for Mac & Win":
           print("invalid link")
        else:
            if title.get_text() == "Screenshot by Lightshot":
                print(f"found valid link {url} saved to working.txt")
                f = open("found.txt", "a")
                f.write(f"working url\t==>  {url}\n")
