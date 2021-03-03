from lolesports_api import Lolesports_API
from time import sleep

# só funciona pra jogos no momento
#get live
api = Lolesports_API()

print("funcionando2")
live_matches = api.get_live()
for live_match in live_matches['schedule']['events']:
    if live_match['state'] == 'finished':
       id = '105562692794240160'
        #gameid = id + '2'
        #print(gameid)
       if live_match['match']['id'] == id:
                # tem 
                    print(f"{live_match['match']['teams'][0]['code']} vs {live_match['match']['teams'][1]['code']}")
                #match id
                    print("funcionando2")
                    print(f"{live_match['match']['id']}")
                    print(f"{live_match['startTime']}")
                    print(f"{live_match['league']}")
                    #print(f"{live_match['id']}")
                    #get_live_game(api.get_event_details(live_match['id']))

     
        #precisa do start time?
        #gameid = match id +2 se tiver começado ou +1 se n tiver
current_game = api.get_window('105562692794240159')
print(current_game)
#print(current_game)
#print(current_game)
#print(type(current_game))
#list_of_dict_values = list(current_game.values())
#print(list_of_dict_values)
#print(type(list_of_dict_values))



'''
split_point = [557]
split_list = [list_of_dict_values[i: j]for i, j in zip([0] + 
split_point,split_point+[None])]
'''
#print(list_of_dict_values[4])

"""                    
        #for game in games['event']['match']['games']:
        jogos = api.get_window([id])
        for jogo in jogos['event']['match']['games']:
            if jogos['gameState'] == 'in_game':

                # tem 
                    #print(f"{live_match['match']['teams'][0]['code']} vs {live_match['match']['teams'][1]['code']}")
                #match id
                    print("time azul")
                    print(f"{jogo['gameState']}")
                    print(f"{jogo['blueTeam']['totalGold']}")
                    print(f"{jogo['blueTeam']['totalKills']}")
                    print(f"{jogo['blueTeam']['towers']}")
                    print(f"{jogo['blueTeam']['dragons']}")
                    print(f"{jogo['blueTeam']['barons']}")
                    print(f"{jogo['blueTeam']['inhibitors']}")
                    print("time vermelho")
                    print(f"{jogo['redTeam']['totalGold']}")
                    print(f"{jogo['redTeam']['totalKills']}")
                    print(f"{jogo['redTeam']['towers']}")
                    print(f"{jogo['redTeam']['dragons']}")
                    print(f"{jogo['redTeam']['barons']}")
                    print(f"{jogo['redTeam']['inhibitors']}")
"""