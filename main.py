from bs4 import BeautifulSoup
from random import randint, choice
import urllib3
import requests
import random
import string
import time

delay = float(input("input delay per each request sent => "))

while True:
    http = urllib3.PoolManager()
    chars = string.ascii_lowercase + string.digits
    iden = ''.join(choice(chars) for i in range(randint(3, 13)))
    time.sleep(delay)
    url = f"https://prnt.sc/{iden}"
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, "html.parser")
    images = soup.findAll('img')

    for image in images:
        if image["src"] == "//st.prntscr.com/2021/02/09/0221/img/0_173a7b_211be8ff.png":
            print("deleted image found")
            break
        for title in soup.find_all('title'): 
            if title.get_text() == "Lightshot — screenshot tool for Mac & Win":
                print("redirect found")
                break
        else:
            print(f"found valid link => {url}")
            f = open("found.txt", "a")
            f.write(f"{url}\n") 
            break
