import webbrowser as wb
import requests as req
import BRFuncs as br
from datetime import date
from pyclip import copy
from time import sleep

brDate = date.today().strftime(br.dateFormat()).lower()
url = f'https://magic.wizards.com/en/news/announcements/{brDate}-banned-and-restricted-announcement'
print(url)

#Checks if there is a B&R and waits for it to release if there is one
while True:
    respCode = req.get(url).status_code
    match respCode:
        case 200:
            print(f'{respCode} It\'s up!')
            wb.open_new_tab(url)
            copy(url)
            break
        case 403:
            print(f'{respCode} Not up yet')
            sleep(1)
        case 404:
            print(f'{respCode} No new B&R')
            break
        case _:
            print(respCode)
            break
