import json, datetime
import requests
from lolesports_api import get_latest_date
#pip install python-urllib2 --upgrade
id = "105562656844501233"
mais = "?startingTime="
starttime = "2021-03-03T16:40:00Z"
starttime2=get_latest_date()
print(starttime2)
complemento= id+mais+starttime2
print(complemento)

base="https://feed.lolesports.com/livestats/v1/window/"

url=base+complemento
print(url)

r = requests.get(url)
#ver os headers
#print(r.headers)

conteudo = json.loads(r.content)
print(type(conteudo))
#print(conteudo)
#reddit_data['data']['children']
print(conteudo['frames'][0]['gameState'])

print("blue team")
print(conteudo['frames'][0]['blueTeam']['totalGold'])
print(conteudo['frames'][0]['blueTeam']['totalKills'])
print(conteudo['frames'][0]['blueTeam']['towers'])
print(conteudo['frames'][0]['blueTeam']['dragons'])
print(conteudo['frames'][0]['blueTeam']['barons'])


"""
print("red team")
print(conteudo['frames'][0]['blueTeam'])
"""

#todo: mostrar conteudo , descobrir o type, isolar partes importantes
