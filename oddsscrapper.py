import requests
from termcolor import colored
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import pandas as pd
import json


import time
from time import sleep

while True: #UNCOM
    #try:
        
        url = "https://www.rivalry.com/pt/match/286241"
        urlhannah = "https://www.bet365.com/#/IP/EV204480595581196172C151"
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
        #print(numbers)
        #print(len(mydivs))
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
        

      
        """
        #Informações para fingir ser um navegador
        header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
        }
        #juntamos tudo com a requests
        r = requests.get(urlhannah, headers=header)
        print(type(r))
        print(r)
        #conteudo = json.loads(r.content)
        #E finalmente usamos a função read_html do pandas
        #dfs = pd.read_html(r.text)
        
        #hannah 
        print("Odds Hannah")
        req2 = urllib.request.Request(urlhannah, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'})
        html2 = urllib.request.urlopen(req2).read()
        print(html2.title)
        #print(html.title)
        bs2 = BeautifulSoup(html2,'lxml')

        # <span class="srb-ParticipantCenteredStackedMarketRow_Odds">1.50</span>
        mydivs2 = bs2.find_all("div", {"class": "srb-ParticipantCenteredStackedMarketRow_Odds"})
        print(mydivs2)
        print(type(mydivs2))
        numbers2 = [d.text for d in mydivs2]
        print(type(numbers2))
        print(numbers)

        print(soup.find_all)
        #print(type(mydivs))
        #numbers = [d.text for d in mydivs]
        # so os numeros das odds na rivalry
        #print(numbers[0],numbers[1])

        #team-name text-sm text-navy-light
        #time1 = bs.find_all("div", {"class": "team-name outcome-one"})
        #time1 = [d.text for d in time1]
        #print(time1)

        #time2 = bs.find_all("div", {"class": "team-name outcome-two"})
        #time2 = [d.text for d in time2]
        #print(time2)

        #print("Odds Rivalry")
        #print(time1, numbers[0], "vs",numbers[1] , time2 )

        
        """



        sleep(5) #UNCOM
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