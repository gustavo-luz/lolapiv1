
"""
import requests
from termcolor import colored
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import pandas as pd
import json
import re


import time
from time import sleep
#try with scrapy!!
page = requests.get("https://www.bet365.com/#/IP/EV204480595581490662C151")

print(page.status_code)
#soup = BeautifulSoup(page.content, 'html.parser')
soup = BeautifulSoup(page.content, 'html.parser')

print(type(soup))
#soup.get_text()
#print(soup.prettify())
#<span class="srb-ParticipantCenteredStackedMarketRow_Odds">1.53</span>
#<div class="gl-Market gl-Market_General gl-Market_General-columnheader gl-Market_General-pwidth33-333 "><div class="gl-MarketColumnHeader ">GODSENT</div><div class="srb-ParticipantCenteredStackedMarketRow gl-Participant_General gl-Market_General-cn1 "><span class="srb-ParticipantCenteredStackedMarketRow_Odds">1.83</span></div></div>
#titulo
# <div class="gl-MarketColumnHeader ">GODSENT</div>
#<div class="srb-ParticipantCenteredStackedMarketRow gl-Participant_General gl-Market_General-cn1 "><span class="srb-ParticipantCenteredStackedMarketRow_Odds">2.00</span></div>
# <span class="srb-ParticipantCenteredStackedMarketRow_Odds">8.50</span>
#<span class="srb-ParticipantCenteredStackedMarketRow_Odds">3.75</span>
spans = soup.find_all('span',{'class_':'srb-ParticipantCenteredStackedMarketRow_Odds'})
print(spans)
lines = [span.get_text() for span in spans]
print(lines)

print(soup.find_all('span'))


fighterName = soup.find('span', class_ = 'srb-ParticipantCenteredStackedMarketRow_Odds')
print(fighterName)
"""


"""
odd1 = soup.find_all("span",class_="srb-ParticipantCenteredStackedMarketRow_Odds")

for tag in soup.find_all(re.compile("^odd")):
    print(tag)
#odd12 = soup.body.findAll(text="Odds")
#print(odd12)
soup(text='odd')
soup(text=re.compile('odds'))
print(odd1)
print(type(odd1))
print(len(odd1))
numbers = [d.text for d in odd1]
print(numbers)


#print(soup.find_all("a", class_="element"))
#print(css_soup.select("gl-MarketColumnHeader"))

"""


from bs4 import BeautifulSoup
import urllib.request
#from html2json import collect

source = urllib.request.urlopen('https://www.bet365.com/#/AC/B151/C20725661/D19/E11368665/F19/')
soup = BeautifulSoup(source, 'lxml')
#html = urllib.request.urlopen(source).read()
#print(type(html))
#print(soup.get_text())
print(type(soup))
soupstr = str(soup)
print(type(soupstr))
print(len(soupstr))

body = soup.find('body')
print(body)
#print(soupstr[30:len(soupstr)-1])


f= open("content.txt","w+")
for i in range(10):
     f.write(soupstr)

f.close() 

#print(soupstr)
#odds = soupstr.find("gl-MarketColumnHeader")
#print(odds)
#print(soupstr[74473:74482])
#soup.get_text()
#print(soup.prettify())
#gl-MarketColumnHeader

"""
spans = soup.find_all('div',{'class_':'gl-MarketColumnHeader'})
#spans = soup.find_all('span',{'class_':'sip-MergedHandicapParticipant_Odds"'})
print(spans)

numbers = [d.text for d in spans]
print(numbers)


for url in soup.select('srb-ParticipantCenteredStackedMarketRow_Odds'):
    print(url['href'])
"""
