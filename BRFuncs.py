from datetime import date, timedelta
from platform import system

def mondayCheck(daysFwd):
    if daysFwd % 7 == 0:
        daysDiff = 0 - date.today().weekday()
        daysDiff += daysFwd
    return date.today() + timedelta(daysDiff)

def dateFormat():
    return '%B-%#d-%Y' if system() == 'Windows' else '%B-%-d-%Y'

def makeUrl(i):
    daysFwd = i * 7
    brDate = mondayCheck(daysFwd).strftime(dateFormat()).lower()
    return f'https://magic.wizards.com/en/news/announcements/{brDate}-banned-and-restricted-announcement'
