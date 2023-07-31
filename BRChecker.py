import webbrowser as wb
import requests as req
from datetime import date, timedelta
from pyclip import copy

#Gets the date of today if it's Monday or next Monday if it's after Monday
def mondayCheck(today, monday, daysFwd):
    daysDiff = monday - today
    if daysDiff <= 0: 
        daysDiff += daysFwd
    return date.today() + timedelta(daysDiff)

#Loads URL and returns response code
def getUrl():
    response = req.get(url)
    return response.status_code

#Checks the two upcoming Mondays for a B&R
i = 1
monday = 0
today = date.today().weekday()
while i <= 2:
    daysFwd = i * 7
    brDate = mondayCheck(today, monday, daysFwd).strftime('%B-%d-%Y') 
    url = f'https://magic.wizards.com/en/news/announcements/{brDate.lower()}-banned-and-restricted-announcement?aoeui'
    print(url)
    respCode = getUrl()
    match respCode:
        case 403:
            print(f'{respCode} New B&R coming!')
            wb.open_new_tab(url)
            copy(url)
            i += 1
        case 404:
            print(f'{respCode} No new B&R')
            i += 1
        case _:
            print(respCode)
            i += 1
