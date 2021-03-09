import requests
from termcolor import colored
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request

import time
from time import sleep

while True:
    #try:
        
        url = "https://www.rivalry.com/pt/match/294698"
        #print(url)


        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read()

        #print(html.title)
        bs = BeautifulSoup(html,'lxml')


        #<div class="odds-flex-container"><!----> <span class="odds">1.46</span></div>
        # odd time 1 <div class="team-name text-sm text-navy-light">LOUD Academy</div>
        #print(bs.find('div',class_='team-name text-sm').text)
        #print(bs.find('div',class_='odds-flex-container').text)

        mydivs = bs.find_all("div", {"class": "odds-flex-container"})
        #print(mydivs)
        #print(type(mydivs))
        numbers = [d.text for d in mydivs]
        # so os numeros das odds na rivalry
        #print(numbers[0],numbers[1])

        #team-name text-sm text-navy-light
        time1 = bs.find_all("div", {"class": "team-name outcome-one"})
        time1 = [d.text for d in time1]
        #print(time1)

        time2 = bs.find_all("div", {"class": "team-name outcome-two"})
        time2 = [d.text for d in time2]
        #print(time2)

        print("Odds Rivalry")
        print(time1, numbers[0], "vs",numbers[1] , time2 )
        sleep(5)
    #except: #UNCOM
        #pass







"""
print([
    float(td.find(text=True).split(" ", 1)[0])
    for td in bs.find_all('td', {'class':'odds-flex-container'})
])
"""



#concise for export
"""
import requests
from termcolor import colored
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request


while True:

url = "https://www.rivalry.com/pt/match/294698"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()
bs = BeautifulSoup(html,'lxml')
mydivs = bs.find_all("div", {"class": "odds-flex-container"})
numbers = [d.text for d in mydivs]
time1 = bs.find_all("div", {"class": "team-name outcome-one"})
time1 = [d.text for d in time1]
time2 = bs.find_all("div", {"class": "team-name outcome-two"})
time2 = [d.text for d in time2]
print("Odds Rivalry")
print(time1, numbers[0], "vs",numbers[1] , time2 )
"""