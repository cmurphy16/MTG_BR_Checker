import webbrowser as wb
import requests as req
from platform import system
from datetime import date
from pyclip import copy
from time import sleep

def dateFormat():
    return '%B-%#d-%Y' if system() == 'Windows' else '%B-%-d-%Y'

url = f'https://magic.wizards.com/en/news/announcements/{date.today().strftime(dateFormat()).lower()}-banned-and-restricted-announcement'
print(url)

while True:
    respCode = req.get(url).status_code
    match respCode:
        case 200:
            print(f'{respCode} It\'s up!')
            wb.open_new_tab(url)
            copy(url)
            break
        case 403 | 404:
            print(f'{respCode} Not up yet')
            sleep(1)
        case _:
            print(respCode)
            break
