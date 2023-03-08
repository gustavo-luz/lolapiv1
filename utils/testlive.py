import json
import datetime
import requests
from lolesports_api import get_latest_date
import time
from time import sleep
from termcolor import colored
#odds
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
#tempos e arquivo de log
import csv
import pandas


# pip install python-urllib2 --upgrade

# rivalry odd
#urlodd = "https://www.rivalry.com/pt/match/294698" #UNCOM


#cblol105658534675811058
id = "105658534675811058"

#lec
#id = "105551618308363551"

while True:

    
    try: #UNCOM
        
        
        now = datetime.datetime.now(datetime.timezone.utc)
        #print(now)
        #subtraindo os segundos e microsegundos
        if now.second > 50:
            now = now = now - datetime.timedelta(seconds=now.second,microseconds=now.microsecond) + datetime.timedelta(seconds=40)
        elif now.second > 40:
            now = now = now - datetime.timedelta(seconds=now.second,microseconds=now.microsecond) + datetime.timedelta(seconds=30)
        elif now.second > 30:
            now = now = now - datetime.timedelta(seconds=now.second,microseconds=now.microsecond) + datetime.timedelta(seconds=20)
        elif now.second > 20:
            now = now = now - datetime.timedelta(seconds=now.second,microseconds=now.microsecond) + datetime.timedelta(seconds=10)
        elif now.second > 10:
            now = now = now - datetime.timedelta(seconds=now.second,microseconds=now.microsecond) + datetime.timedelta(seconds=0)
        else:
            now = now - datetime.timedelta(seconds=now.second,microseconds=now.microsecond - datetime.timedelta(seconds=10))

        
        sleep(10) #UNCOM
        
        #print(now)
        
        now_string = now.isoformat()
        now_string = str(now_string).replace('+00:00', 'Z')
        #print(now_string)
        

        mais = "?startingTime="
        #starttime = "2021-03-06T13:54:50Z"
        starttime2 = now_string
        #starttime2 = get_latest_date()
        #print(starttime2)
        #print(type(starttime2))
        complemento = id+mais+starttime2 #MUDAR PRA 2
        # print(complemento)

        base = "https://feed.lolesports.com/livestats/v1/window/"

        url = base+complemento
        print(url)

        r = requests.get(url)
        # ver os headers
        # print(r.headers)

        conteudo = json.loads(r.content)
        # print(type(conteudo))
        # print(conteudo)
        # reddit_data['data']['children']
        estado = conteudo['frames'][0]['gameState']
        # print(estado)

        # ------------------------------------ TIME AZUL --------------
        #print("blue team")
        goldtime1 = conteudo['frames'][0]['blueTeam']['totalGold']
        # print("goldtime2",goldtime2)
        killstime1 = conteudo['frames'][0]['blueTeam']['totalKills']
        # print(killstime1)
        torrestime1 = conteudo['frames'][0]['blueTeam']['towers']
        # print(torrestime1)
        dragstime1 = conteudo['frames'][0]['blueTeam']['dragons']
        # print(dragstime1)
        baronstime1 = conteudo['frames'][0]['blueTeam']['barons']
        # print(baronstime1)
        inibstime1 = conteudo['frames'][0]['blueTeam']['inhibitors']
        # print(inibstime1)

        #geraltime1 = conteudo['frames'][0]['blueTeam']
        # print(geraltime1)


        # ------------------------------------ TIME VERMELHO --------------
        #print("red team ")
        goldtime2 = conteudo['frames'][0]['redTeam']['totalGold']
        # print("goldtime2",goldtime2)
        killstime2 = conteudo['frames'][0]['redTeam']['totalKills']
        # print(killstime2)
        torrestime2 = conteudo['frames'][0]['redTeam']['towers']
        # print(torrestime2)
        dragstime2 = conteudo['frames'][0]['redTeam']['dragons']
        # print(dragstime2)
        baronstime2 = conteudo['frames'][0]['redTeam']['barons']
        # print(baronstime2)
        inibstime2 = conteudo['frames'][0]['redTeam']['inhibitors']
        # print(inibstime2)


        # ------------------------------------ +STATS --------------
        diffgold1 = goldtime1 - goldtime2

        if diffgold1 < 0:
            sinal1 = ""
        else:
            sinal1 = "+"

        diffgold1 = sinal1 + str(diffgold1)
        # print(diffgold1)


        diffgold2 = goldtime2 - goldtime1

        if diffgold2 < 0:
            sinal2 = ""
        else:
            sinal2 = "+"

        diffgold2 = sinal2 + str(diffgold2)
        # print(diffgold2)


        # ------------------------------------ TABELA BÁSICA --------------
        print("estado do jogo\t", estado)
        print("-----------------------------------------")
        #print("%s:\t%s" % ("gold", str(goldtime1) + " (" + diffgold1 + ")") )
        time1 = conteudo['gameMetadata']['blueTeamMetadata']['participantMetadata'][0]['summonerName']
        time1 = time1[0:3]
        time2 = conteudo['gameMetadata']['redTeamMetadata']['participantMetadata'][0]['summonerName']
        time2 = time2[0:3]        
        print(time1,"vs",time2)


        """
        # odds rivalry 
        req = urllib.request.Request(urlodd, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read()
        bs = BeautifulSoup(html,'lxml')
        mydivs = bs.find_all("div", {"class": "odds-flex-container"})
        numbers = [d.text for d in mydivs]
        oddtime1 = bs.find_all("div", {"class": "team-name outcome-one"})
        oddtime1 = [d.text for d in oddtime1]
        oddtime2 = bs.find_all("div", {"class": "team-name outcome-two"})
        oddtime2 = [d.text for d in oddtime2]
        print("Odds:", oddtime1, numbers[0], "vs",numbers[1] , oddtime2 )
        """
        



        print("%s:\t%s\t%s%s%s%s" % ("gold", str(goldtime1), "X ", str(goldtime2), " total:", str(goldtime1+goldtime2) ))
        print("%s:%s%s%s" % ("diff", " (" + diffgold1 + ")"," X ", "(" + diffgold2 + ")"))
        #print("%s:\t%s\t%s%s" % ("gold", str(goldtime1) + " (" + diffgold1 + ")","X ", str(goldtime2) + " (" + diffgold2 + ")"))                                        
        #print("%s:\t%s" % ("gold",diffgold2) )
        #print(f'{gold:str(goldtime1)} {kills: str(killstime1) }')
        print("%s:%s%s%s" % ("kills", "   " + str(killstime1), "   X   ", str(killstime2)))
        print("%s:%s%s%s" % ("torres", "  " + str(torrestime1), "   X   ", str(torrestime2)))
        #print("%s:%s%s%s" % ("dragões", "  " + str(dragstime1), "   X   ", str(dragstime2)))
        print("%s:%s" % ("drakes " + time1, "  " + str(dragstime1)))
        print( "          X")
        print("%s:%s" % ("drakes " + time2, "  " + str(dragstime2)))
        print("%s:%s%s%s" % ("baron", "   " + str(baronstime1), "   X   ", str(baronstime2)))
        print("%s:%s%s%s" % ("inibs", "   " + str(inibstime1), "   X   ", str(inibstime2)))

        # ------------------------ stats específicos ---------
        print("-----------------------------------------")
        #print("       ", time1)
        # top
        champtoptime1 = conteudo['gameMetadata']['blueTeamMetadata']['participantMetadata'][0]['championId']
        goldtoptime1 = conteudo['frames'][0]['blueTeam']['participants'][0]['totalGold']
        killstoptime1 = conteudo['frames'][0]['blueTeam']['participants'][0]['kills']
        mortestoptime1 = conteudo['frames'][0]['blueTeam']['participants'][0]['deaths']
        assiststoptime1 = conteudo['frames'][0]['blueTeam']['participants'][0]['assists']
        farmtoptime1 = conteudo['frames'][0]['blueTeam']['participants'][0]['creepScore']
        vidaatualtoptime1 = conteudo['frames'][0]['blueTeam']['participants'][0]['currentHealth']
        vidamaxtoptime1 = conteudo['frames'][0]['blueTeam']['participants'][0]['maxHealth']
        pctvidatoptime1 = round(vidaatualtoptime1/vidamaxtoptime1 * 100)
        #print(champtoptime1,":",killstoptime1,"/",mortestoptime1,"/",assiststoptime1)
        if pctvidatoptime1 == 0:
            pctvidatoptime1=(colored(str(pctvidatoptime1) + "%", 'grey'))
        elif pctvidatoptime1 < 20:
            pctvidatoptime1=(colored(str(pctvidatoptime1) + "%", 'red'))
        elif pctvidatoptime1 < 50:
            pctvidatoptime1=(colored(str(pctvidatoptime1) + "%", 'yellow'))
        elif pctvidatoptime1 < 70:
            pctvidatoptime1=(colored(str(pctvidatoptime1) + "%", 'magenta')) 
        else:
            pctvidatoptime1=(colored(str(pctvidatoptime1) + "%", 'green'))

        #print(pctvidatoptime1)
        # mid time 1
        champmidtime1 = conteudo['gameMetadata']['blueTeamMetadata']['participantMetadata'][1]['championId']
        goldmidtime1 = conteudo['frames'][0]['blueTeam']['participants'][1]['totalGold']
        killsmidtime1 = conteudo['frames'][0]['blueTeam']['participants'][1]['kills']
        mortesmidtime1 = conteudo['frames'][0]['blueTeam']['participants'][1]['deaths']
        assistsmidtime1 = conteudo['frames'][0]['blueTeam']['participants'][1]['assists']
        farmmidtime1 = conteudo['frames'][0]['blueTeam']['participants'][1]['creepScore']
        vidaatualmidtime1 = conteudo['frames'][0]['blueTeam']['participants'][1]['currentHealth']
        vidamaxmidtime1 = conteudo['frames'][0]['blueTeam']['participants'][1]['maxHealth']
        pctvidamidtime1 = round(vidaatualmidtime1/vidamaxmidtime1 * 100) 
        #print(type(pctvidamidtime1))
        #print(pctvidamidtime1)
        #print(champmidtime1,":",killsmidtime1,"/",mortesmidtime1,"/",assistsmidtime1)

        if pctvidamidtime1 == 0:
            pctvidamidtime1=(colored(str(pctvidamidtime1) + "%", 'grey'))
        elif pctvidamidtime1 < 20:
            pctvidamidtime1=(colored(str(pctvidamidtime1) + "%", 'red'))
        elif pctvidamidtime1 < 50:
            pctvidamidtime1=(colored(str(pctvidamidtime1) + "%", 'yellow'))
        elif pctvidamidtime1 < 70:
            pctvidamidtime1=(colored(str(pctvidamidtime1) + "%", 'magenta')) 
        else:
            pctvidamidtime1=(colored(str(pctvidamidtime1) + "%", 'green'))
             
        #print(pctvidamidtime1)                 
        #print(vidaatualmidtime1,vidamaxmidtime1,pctvidamidtime1,"%")
        # jg time 1
        champjgtime1 = conteudo['gameMetadata']['blueTeamMetadata']['participantMetadata'][2]['championId']
        goldjgtime1 = conteudo['frames'][0]['blueTeam']['participants'][2]['totalGold']
        killsjgtime1 = conteudo['frames'][0]['blueTeam']['participants'][2]['kills']
        mortesjgtime1 = conteudo['frames'][0]['blueTeam']['participants'][2]['deaths']
        assistsjgtime1 = conteudo['frames'][0]['blueTeam']['participants'][2]['assists']
        farmjgtime1 = conteudo['frames'][0]['blueTeam']['participants'][2]['creepScore']
        vidaatualjgtime1 = conteudo['frames'][0]['blueTeam']['participants'][2]['currentHealth']
        vidamaxjgtime1 = conteudo['frames'][0]['blueTeam']['participants'][2]['maxHealth']
        pctvidajgtime1 = round(vidaatualjgtime1/vidamaxjgtime1 * 100) 
        #print(champjgtime1,":",killsjgtime1,"/",mortesjgtime1,"/",assistsjgtime1)

        if pctvidajgtime1 == 0:
            pctvidajgtime1=(colored(str(pctvidajgtime1) + "%", 'grey'))
        elif pctvidajgtime1 < 20:
            pctvidajgtime1=(colored(str(pctvidajgtime1) + "%", 'red'))
        elif pctvidajgtime1 < 50:
            pctvidajgtime1=(colored(str(pctvidajgtime1) + "%", 'yellow'))
        elif pctvidajgtime1 < 70:
            pctvidajgtime1=(colored(str(pctvidajgtime1) + "%", 'magenta')) 
        else:
            pctvidajgtime1=(colored(str(pctvidajgtime1) + "%", 'green'))
             
        #print(pctvidajgtime1)    
        # adc time 1
        champadtime1 = conteudo['gameMetadata']['blueTeamMetadata']['participantMetadata'][3]['championId']
        goldadtime1 = conteudo['frames'][0]['blueTeam']['participants'][3]['totalGold']
        killsadtime1 = conteudo['frames'][0]['blueTeam']['participants'][3]['kills']
        mortesadtime1 = conteudo['frames'][0]['blueTeam']['participants'][3]['deaths']
        assistsadtime1 = conteudo['frames'][0]['blueTeam']['participants'][3]['assists']
        farmadtime1 = conteudo['frames'][0]['blueTeam']['participants'][3]['creepScore']
        vidaatualadtime1 = conteudo['frames'][0]['blueTeam']['participants'][3]['currentHealth']
        vidamaxadtime1 = conteudo['frames'][0]['blueTeam']['participants'][3]['maxHealth']
        pctvidaadtime1 = round(vidaatualadtime1/vidamaxadtime1 * 100) 
        #print(champadtime1,":",killsadtime1,"/",mortesadtime1,"/",assistsadtime1)

        if pctvidaadtime1 == 0:
            pctvidaadtime1=(colored(str(pctvidaadtime1) + "%", 'grey'))
        elif pctvidaadtime1 < 20:
            pctvidaadtime1=(colored(str(pctvidaadtime1) + "%", 'red'))
        elif pctvidaadtime1 < 50:
            pctvidaadtime1=(colored(str(pctvidaadtime1) + "%", 'yellow'))
        elif pctvidaadtime1 < 70:
            pctvidaadtime1=(colored(str(pctvidaadtime1) + "%", 'magenta')) 
        else:
            pctvidaadtime1=(colored(str(pctvidaadtime1) + "%", 'green'))
             
        #print(pctvidaadtime1)    
        # sup time 1
        champsuptime1 = conteudo['gameMetadata']['blueTeamMetadata']['participantMetadata'][4]['championId']
        goldsuptime1 = conteudo['frames'][0]['blueTeam']['participants'][4]['totalGold']
        killssuptime1 = conteudo['frames'][0]['blueTeam']['participants'][4]['kills']
        mortessuptime1 = conteudo['frames'][0]['blueTeam']['participants'][4]['deaths']
        assistssuptime1 = conteudo['frames'][0]['blueTeam']['participants'][4]['assists']
        farmsuptime1 = conteudo['frames'][0]['blueTeam']['participants'][4]['creepScore']
        vidaatualsuptime1 = conteudo['frames'][0]['blueTeam']['participants'][4]['currentHealth']
        vidamaxsuptime1 = conteudo['frames'][0]['blueTeam']['participants'][4]['maxHealth']
        pctvidasuptime1 = round(vidaatualsuptime1/vidamaxsuptime1 * 100) 
        #print(champsuptime1,":",killssuptime1,"/",mortessuptime1,"/",assistssuptime1)

        if pctvidasuptime1 == 0:
            pctvidasuptime1=(colored(str(pctvidasuptime1) + "%", 'grey'))
        elif pctvidasuptime1 < 20:
            pctvidasuptime1=(colored(str(pctvidasuptime1) + "%", 'red'))
        elif pctvidasuptime1 < 50:
            pctvidasuptime1=(colored(str(pctvidasuptime1) + "%", 'yellow'))
        elif pctvidasuptime1 < 70:
            pctvidasuptime1=(colored(str(pctvidasuptime1) + "%", 'magenta')) 
        else:
            pctvidasuptime1=(colored(str(pctvidasuptime1) + "%", 'green'))
             
        #print(pctvidasuptime1)   


        # --------------------------------- TIME 2 ---------------------


        #print("-----------------------------------------")
        #print("       ", time2)
        # top
        champtoptime2 = conteudo['gameMetadata']['redTeamMetadata']['participantMetadata'][0]['championId']
        goldtoptime2 = conteudo['frames'][0]['redTeam']['participants'][0]['totalGold']
        killstoptime2 = conteudo['frames'][0]['redTeam']['participants'][0]['kills']
        mortestoptime2 = conteudo['frames'][0]['redTeam']['participants'][0]['deaths']
        assiststoptime2 = conteudo['frames'][0]['redTeam']['participants'][0]['assists']
        farmtoptime2 = conteudo['frames'][0]['redTeam']['participants'][0]['creepScore']
        vidaatualtoptime2 = conteudo['frames'][0]['redTeam']['participants'][0]['currentHealth']
        vidamaxtoptime2 = conteudo['frames'][0]['redTeam']['participants'][0]['maxHealth']
        pctvidatoptime2 = round(vidaatualtoptime2/vidamaxtoptime2 * 100)
        #print(champtoptime2,":",killstoptime2,"/",mortestoptime2,"/",assiststoptime2)
        if pctvidatoptime2 == 0:
            pctvidatoptime2=(colored(str(pctvidatoptime2) + "%", 'grey'))
        elif pctvidatoptime2 < 20:
            pctvidatoptime2=(colored(str(pctvidatoptime2) + "%", 'red'))
        elif pctvidatoptime2 < 50:
            pctvidatoptime2=(colored(str(pctvidatoptime2) + "%", 'yellow'))
        elif pctvidatoptime2 < 70:
            pctvidatoptime2=(colored(str(pctvidatoptime2) + "%", 'magenta')) 
        else:
            pctvidatoptime2=(colored(str(pctvidatoptime2) + "%", 'green'))

        #print(pctvidatoptime2)
        # mid time 2
        champmidtime2 = conteudo['gameMetadata']['redTeamMetadata']['participantMetadata'][1]['championId']
        goldmidtime2 = conteudo['frames'][0]['redTeam']['participants'][1]['totalGold']
        killsmidtime2 = conteudo['frames'][0]['redTeam']['participants'][1]['kills']
        mortesmidtime2 = conteudo['frames'][0]['redTeam']['participants'][1]['deaths']
        assistsmidtime2 = conteudo['frames'][0]['redTeam']['participants'][1]['assists']
        farmmidtime2 = conteudo['frames'][0]['redTeam']['participants'][1]['creepScore']
        vidaatualmidtime2 = conteudo['frames'][0]['redTeam']['participants'][1]['currentHealth']
        vidamaxmidtime2 = conteudo['frames'][0]['redTeam']['participants'][1]['maxHealth']
        pctvidamidtime2 = round(vidaatualmidtime2/vidamaxmidtime2 * 100) 
        #print(type(pctvidamidtime2))
        #print(pctvidamidtime2)
        #print(champmidtime2,":",killsmidtime2,"/",mortesmidtime2,"/",assistsmidtime2)

        if pctvidamidtime2 == 0:
            pctvidamidtime2=(colored(str(pctvidamidtime2) + "%", 'grey'))
        elif pctvidamidtime2 < 20:
            pctvidamidtime2=(colored(str(pctvidamidtime2) + "%", 'red'))
        elif pctvidamidtime2 < 50:
            pctvidamidtime2=(colored(str(pctvidamidtime2) + "%", 'yellow'))
        elif pctvidamidtime2 < 70:
            pctvidamidtime2=(colored(str(pctvidamidtime2) + "%", 'magenta')) 
        else:
            pctvidamidtime2=(colored(str(pctvidamidtime2) + "%", 'green'))
             
        #print(pctvidamidtime2)                 
        #print(vidaatualmidtime2,vidamaxmidtime2,pctvidamidtime2,"%")
        # jg time 2
        champjgtime2 = conteudo['gameMetadata']['redTeamMetadata']['participantMetadata'][2]['championId']
        goldjgtime2 = conteudo['frames'][0]['redTeam']['participants'][2]['totalGold']
        killsjgtime2 = conteudo['frames'][0]['redTeam']['participants'][2]['kills']
        mortesjgtime2 = conteudo['frames'][0]['redTeam']['participants'][2]['deaths']
        assistsjgtime2 = conteudo['frames'][0]['redTeam']['participants'][2]['assists']
        farmjgtime2 = conteudo['frames'][0]['redTeam']['participants'][2]['creepScore']
        vidaatualjgtime2 = conteudo['frames'][0]['redTeam']['participants'][2]['currentHealth']
        vidamaxjgtime2 = conteudo['frames'][0]['redTeam']['participants'][2]['maxHealth']
        pctvidajgtime2 = round(vidaatualjgtime2/vidamaxjgtime2 * 100) 
        #print(champjgtime2,":",killsjgtime2,"/",mortesjgtime2,"/",assistsjgtime2)

        if pctvidajgtime2 == 0:
            pctvidajgtime2=(colored(str(pctvidajgtime2) + "%", 'grey'))
        elif pctvidajgtime2 < 20:
            pctvidajgtime2=(colored(str(pctvidajgtime2) + "%", 'red'))
        elif pctvidajgtime2 < 50:
            pctvidajgtime2=(colored(str(pctvidajgtime2) + "%", 'yellow'))
        elif pctvidajgtime2 < 70:
            pctvidajgtime2=(colored(str(pctvidajgtime2) + "%", 'magenta')) 
        else:
            pctvidajgtime2=(colored(str(pctvidajgtime2) + "%", 'green'))
             
        #print(pctvidajgtime2)    
        # adc time 2
        champadtime2 = conteudo['gameMetadata']['redTeamMetadata']['participantMetadata'][3]['championId']
        goldadtime2 = conteudo['frames'][0]['redTeam']['participants'][3]['totalGold']
        killsadtime2 = conteudo['frames'][0]['redTeam']['participants'][3]['kills']
        mortesadtime2 = conteudo['frames'][0]['redTeam']['participants'][3]['deaths']
        assistsadtime2 = conteudo['frames'][0]['redTeam']['participants'][3]['assists']
        farmadtime2 = conteudo['frames'][0]['redTeam']['participants'][3]['creepScore']
        vidaatualadtime2 = conteudo['frames'][0]['redTeam']['participants'][3]['currentHealth']
        vidamaxadtime2 = conteudo['frames'][0]['redTeam']['participants'][3]['maxHealth']
        pctvidaadtime2 = round(vidaatualadtime2/vidamaxadtime2 * 100) 
        #print(champadtime2,":",killsadtime2,"/",mortesadtime2,"/",assistsadtime2)

        if pctvidaadtime2 == 0:
            pctvidaadtime2=(colored(str(pctvidaadtime2) + "%", 'grey'))
        elif pctvidaadtime2 < 20:
            pctvidaadtime2=(colored(str(pctvidaadtime2) + "%", 'red'))
        elif pctvidaadtime2 < 50:
            pctvidaadtime2=(colored(str(pctvidaadtime2) + "%", 'yellow'))
        elif pctvidaadtime2 < 70:
            pctvidaadtime2=(colored(str(pctvidaadtime2) + "%", 'magenta')) 
        else:
            pctvidaadtime2=(colored(str(pctvidaadtime2) + "%", 'green'))
             
        #print(pctvidaadtime2)    
        # sup time 2
        champsuptime2 = conteudo['gameMetadata']['redTeamMetadata']['participantMetadata'][4]['championId']
        goldsuptime2 = conteudo['frames'][0]['redTeam']['participants'][4]['totalGold']
        killssuptime2 = conteudo['frames'][0]['redTeam']['participants'][4]['kills']
        mortessuptime2 = conteudo['frames'][0]['redTeam']['participants'][4]['deaths']
        assistssuptime2 = conteudo['frames'][0]['redTeam']['participants'][4]['assists']
        farmsuptime2 = conteudo['frames'][0]['redTeam']['participants'][4]['creepScore']
        vidaatualsuptime2 = conteudo['frames'][0]['redTeam']['participants'][4]['currentHealth']
        vidamaxsuptime2 = conteudo['frames'][0]['redTeam']['participants'][4]['maxHealth']
        pctvidasuptime2 = round(vidaatualsuptime2/vidamaxsuptime2 * 100) 
        #print(champsuptime2,":",killssuptime2,"/",mortessuptime2,"/",assistssuptime2)

        if pctvidasuptime2 == 0:
            pctvidasuptime2=(colored(str(pctvidasuptime2) + "%", 'grey'))
        elif pctvidasuptime2 < 20:
            pctvidasuptime2=(colored(str(pctvidasuptime2) + "%", 'red'))
        elif pctvidasuptime2 < 50:
            pctvidasuptime2=(colored(str(pctvidasuptime2) + "%", 'yellow'))
        elif pctvidasuptime2 < 70:
            pctvidasuptime2=(colored(str(pctvidasuptime2) + "%", 'magenta')) 
        else:
            pctvidasuptime2=(colored(str(pctvidasuptime2) + "%", 'green'))
             
        #print(pctvidasuptime2) 
  
        #teste nova tabela
        print("         ", time1,"    "," VS  ", time2)
        print(champtoptime1,":",killstoptime1,"/",mortestoptime1,"/",assiststoptime1,"       ",champtoptime2,":",killstoptime2,"/",mortestoptime2,"/",assiststoptime2)
        print("            ", pctvidatoptime1,"     ", pctvidatoptime2)
        print(champmidtime1,":",killsmidtime1,"/",mortesmidtime1,"/",assistsmidtime1,"       ",champmidtime2,":",killsmidtime2,"/",mortesmidtime2,"/",assistsmidtime2)
        print("            ", pctvidamidtime1,"     ", pctvidamidtime2)
        print(champjgtime1,":",killsjgtime1,"/",mortesjgtime1,"/",assistsjgtime1,"       ",champjgtime2,":",killsjgtime2,"/",mortesjgtime2,"/",assistsjgtime2)
        print("            ", pctvidajgtime1,"     ", pctvidajgtime2)
        print(champadtime1,":",killsadtime1,"/",mortesadtime1,"/",assistsadtime1,"       ",champadtime2,":",killsadtime2,"/",mortesadtime2,"/",assistsadtime2)
        print("            ", pctvidaadtime1,"     ", pctvidaadtime2)
        print(champsuptime1,":",killssuptime1,"/",mortessuptime1,"/",assistssuptime1,"       ",champsuptime2,":",killssuptime2,"/",mortessuptime2,"/",assistssuptime2)
        print("            ", pctvidasuptime1,"     ", pctvidasuptime2)


        #print("farmjg",farmjgtime1," ",farmjgtime2)
        #print(type(farmjgtime2))
        df = pandas.read_csv('D://windows//Documents//BET//new_api//lolapiv1//log.csv')
        #print(df)
        #valor = df['time'][0]
        #print(valor)

        #print(df['time'][0])
        cs = farmjgtime1

        if cs < 4:
            df['time'][0] = 0
        elif cs == 4:
            df['time'][0] = 105
        elif cs > 4:
            df['time'][0] = df['time'][0] + 10

        #se for menor que 4, escreve 0 no tempo
        #print(df['time'][0])
        #print(df['time'][0])
        #print(df['time'][0] // 60)
        #print(df['time'][0] % 60)
        print("Tempo de jogo:",df['time'][0] // 60, ":",df['time'][0] % 60)
        #tempo de jogo é a transformação de segundos pra minutos
        

        df.to_csv('D://windows//Documents//BET//new_api//lolapiv1//log.csv')
        print(valor)


        #print(champtoptime2,champmidtime2,champjgtime2)
        #print(champadtime2,champsuptime2)
        #toptime2 = conteudo['frames'][0]['redTeam']['totalGold']
        # print("goldtime2",goldtime2)

        #sleep(30) #for testing
        
        #print("red team")
        #print(conteudo['frames'][0]['blueTeam'])
        

    
    except: #UNCOM
        pass
     

#sleep(10)
    # todo: mostrar conteudo , descobrir o type, isolar partes importantes

