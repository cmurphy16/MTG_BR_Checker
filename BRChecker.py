import webbrowser as wb
import requests as req
from datetime import date, timedelta
from platform import system
from pyclip import copy

#Gets the date of a Monday
def mondayCheck(daysFwd):
    if daysFwd % 7 == 0:
        daysDiff = 0 - date.today().weekday()
        daysDiff += daysFwd
    return date.today() + timedelta(daysDiff)

#Formats the date based on OS
def dateFormat(daysFwd):
    if system() == 'Windows':
        d = mondayCheck(daysFwd).strftime('%B-%#d-%Y').lower()
    else:
        d = mondayCheck(daysFwd).strftime('%B-%-d-%Y').lower()
    return d

#Creates B&R URL with Monday date
def makeUrl(i):
    daysFwd = i * 7
    brDate = dateFormat(daysFwd)
    url = f'https://magic.wizards.com/en/news/announcements/{brDate}-banned-and-restricted-announcement?aoeui'
    print(url)
    return url

#Checks the two upcoming Mondays for a B&R
for i in range(1,3):
    url = makeUrl(i)
    respCode = req.get(url).status_code
    match respCode:
        case 403:
            print(f'{respCode} New B&R coming!')
            wb.open_new_tab(url)
            copy(url)
        case 404:
            print(f'{respCode} No new B&R')
        case _:
            print(respCode)
