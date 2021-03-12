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
soup = BeautifulSoup(page.content, 'html.parser')

#soup.get_text()
#print(soup.prettify())
#<span class="srb-ParticipantCenteredStackedMarketRow_Odds">1.53</span>
#<div class="gl-Market gl-Market_General gl-Market_General-columnheader gl-Market_General-pwidth33-333 "><div class="gl-MarketColumnHeader ">GODSENT</div><div class="srb-ParticipantCenteredStackedMarketRow gl-Participant_General gl-Market_General-cn1 "><span class="srb-ParticipantCenteredStackedMarketRow_Odds">1.83</span></div></div>
#titulo
# <div class="gl-MarketColumnHeader ">GODSENT</div>
#<div class="srb-ParticipantCenteredStackedMarketRow gl-Participant_General gl-Market_General-cn1 "><span class="srb-ParticipantCenteredStackedMarketRow_Odds">2.00</span></div>
# <span class="srb-ParticipantCenteredStackedMarketRow_Odds">8.50</span>
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


