import webbrowser as wb
import requests as req
from datetime import date, timedelta
from pyclip import copy
from time import sleep

#Gets the date of today if it's Monday or next Monday if it's after Monday
def mondayCheck(today, monday):
    daysDiff = monday - today
    if daysDiff <= -1: 
        daysDiff += 7
    return date.today() + timedelta(daysDiff)

#Loads URL and returns response code
def getUrl():
    response = req.get(url)
    return response.status_code

#Assigns date to variable formatted to match B&R url
monday = 0
today = date.today().weekday()
brDate = mondayCheck(today, monday).strftime('%B-%d-%Y') 
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
            if today == monday:
                print(f'{respCode} Not up yet')
                sleep(1)
            else:
                print(f'{respCode} New B&R coming!')
                wb.open_new_tab(url)
                copy(url)
                break
        case 404:
            print(f'{respCode} No new B&R')
            break
        case _:
            print(respCode)
            break
