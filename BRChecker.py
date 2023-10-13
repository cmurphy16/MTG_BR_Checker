import webbrowser as wb
import requests as req
import BRFuncs as br
from pyclip import copy

#Checks the two upcoming Mondays for a B&R
for i in range(1,3):
    url = br.makeUrl(i)
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
