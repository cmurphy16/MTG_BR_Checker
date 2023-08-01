import webbrowser as wb
import requests as req
from datetime import date, timedelta
from pyclip import copy

#Gets the date of a Monday when daysFwd is a multiple of 7
def mondayCheck(daysFwd):
    daysDiff = 0 - date.today().weekday()
    daysDiff += daysFwd
    return date.today() + timedelta(daysDiff)

#Checks the two upcoming Mondays for a B&R
for i in range(1,3):
    daysFwd = i * 7
    brDate = mondayCheck(daysFwd).strftime('%B-%d-%Y') 
    url = f'https://magic.wizards.com/en/news/announcements/{brDate.lower()}-banned-and-restricted-announcement?aoeui'
    print(url)
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
