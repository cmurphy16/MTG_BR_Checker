import webbrowser as wb
import requests as req
from platform import system
from datetime import date
from pyclip import copy
from time import sleep

def dateFormat():
    return '%B-%#d-%Y' if system() == 'Windows' else '%B-%-d-%Y'

def isUp(urls):
    for url in urls:
        print(url)
        respCode = req.get(url).status_code
        match respCode:
            case 200:
                print(f'{respCode} It\'s up!')
                wb.open_new_tab(url)
                copy(url)
                return True
            case 403 | 404:
                print(f'{respCode} Not up yet')
                sleep(0.25)
            case _:
                print(f'{respCode} Unexpected response code')
                sleep(1)
                return

brDate = date.today().strftime(dateFormat()).lower()
urls = [f'https://magic.wizards.com/en/news/announcements/banned-and-restricted-{brDate}',
        f'https://magic.wizards.com/en/news/announcements/{brDate}-banned-and-restricted',
        f'https://magic.wizards.com/en/news/announcements/banned-and-restricted-announcement-{brDate}',
        f'https://magic.wizards.com/en/news/announcements/{brDate}-banned-and-restricted-announcement']

while isUp(urls) != True:
    isUp(urls)
