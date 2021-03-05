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
estado = conteudo['frames'][0]['gameState']
#print(estado)

# ------------------------------------ TIME AZUL --------------
#print("blue team")
goldtime1 = conteudo['frames'][0]['blueTeam']['totalGold']
#print(goldtime1)
killstime1 = conteudo['frames'][0]['blueTeam']['totalKills']
#print(killstime1)
torrestime1 = conteudo['frames'][0]['blueTeam']['towers']
#print(torrestime1)
dragstime1 = conteudo['frames'][0]['blueTeam']['dragons']
#print(dragstime1)
baronstime1 = conteudo['frames'][0]['blueTeam']['barons']
#print(baronstime1)

# ------------------------------------ TIME VERMELHO --------------
#print("red team ")
goldtime2 = conteudo['frames'][0]['redTeam']['totalGold']
print(goldtime2)
killstime2 = conteudo['frames'][0]['redTeam']['totalKills']
#print(killstime2)
torrestime2 = conteudo['frames'][0]['redTeam']['towers']
#print(torrestime2)
dragstime2 = conteudo['frames'][0]['redTeam']['dragons']
#print(dragstime2)
baronstime2 = conteudo['frames'][0]['redTeam']['barons']
#print(baronstime2)

# ------------------------------------ +STATS --------------
diffgold1 = goldtime1 - goldtime2
"""
if diffgold1 < 0:
    diffgold1 = "+",diffgold1
else:
    diffgold1 = '-',diffgold1
"""
print(diffgold1)
diffgold2 = goldtime2 - goldtime1
print(diffgold2)


# ------------------------------------ TABELA --------------
print("estado do jogo\t",estado)
print("-------------------------")
print("%s:\t%i" % ("gold",goldtime1), diffgold1 )



"""
print("red team")
print(conteudo['frames'][0]['blueTeam'])
"""

#todo: mostrar conteudo , descobrir o type, isolar partes importantes
