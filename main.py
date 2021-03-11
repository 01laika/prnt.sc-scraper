from bs4 import BeautifulSoup
from random import randint, choice
import urllib3
import requests
import random
import string
import json
import time
from rich.console import Console
console = Console()

agent = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

def start():
    webhook = console.input("[purple]input webhook to send images to => ")

    try:
        r = requests.get(webhook)
        if r.json()["message"]:
            console.print("[red]invalid webhook!")
            time.sleep(1)
            start()
    except KeyError:
        pass

    try:
        delay = float(console.input("[purple]input delay per each request sent => "))
    except ValueError:
        console.print("[red]invalid option\n")
        time.sleep(1)
        start()
    else:
        
        while True:
            http = urllib3.PoolManager()
            chars = string.ascii_lowercase + string.digits
            iden = ''.join(choice(chars) for i in range(randint(3, 7)))
            time.sleep(delay)
            url = f"https://prnt.sc/{iden}"
            response = http.request('GET', url, headers=agent)
            soup = BeautifulSoup(response.data, "html.parser")
            images = soup.findAll('img')

            for image in images:
                if image["src"] == "//st.prntscr.com/2021/02/09/0221/img/0_173a7b_211be8ff.png":
                    console.print("[red]deleted image found")
                    break
                for title in soup.find_all('title'): 
                    if title.get_text() == "Lightshot — screenshot tool for Mac & Win":
                        console.print("[red]redirect found")
                        break
                else:
                    for image in images[0::3]:
                        main = (image['src'])
                    headers = {"content-type": "application/json"}
                    
                    data = {
                    "embeds": [{
                    "title": url,
                    "url": url,
                    "footer": {
                        "text": "made by laika#1331",
                        "icon_url": "https://cdn.discordapp.com/avatars/798534483652902932/d89209969185055c9098c4d415b3c449.png?size=128"
                    },
                    "author": {
                        "url": "https://github.com/01laika/prnt.sc-scraper",
                        "name": "Prnt.sc Scraper",
                        "icon_url": "https://files10.com/wp-content/uploads/2017/11/Lightshot-Logo-Icon-48x48.png"
                    },
                    "color": "8388736",
                    "image": {
                    "url": main,
                            }
                        }]
                    }       
                    console.print("[green]sent to webhook")
                    requests.post(webhook, headers=headers, json=data)
                    break
start()
