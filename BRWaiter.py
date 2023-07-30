import webbrowser as wb
import requests as req
from datetime import date
from pyclip import copy
from time import sleep

#Loads URL and returns response code
def getUrl():
    response = req.get(url)
    return response.status_code

#Assigns date to variable formatted to match B&R url
brDate = date.today().strftime('%B-%d-%Y') 
url = f'https://magic.wizards.com/en/news/announcements/{brDate.lower()}-banned-and-restricted-announcement?aoeui'
print(url)


while True:
    respCode = getUrl()
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
