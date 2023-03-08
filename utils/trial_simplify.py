from lolesports_api import Lolesports_API
from time import sleep

api = Lolesports_API()

def handle_livematches():
    while True:
        print("funcionando2")
        id = '105562556576287732'
        #precisa do start time?
        
        #for game in games['event']['match']['games']:
        #live_matches = api.get_window([id])
        live_matches = api.get_window([id])
        for live_match in live_matches['frames']:
            if live_matches['gameState'] == 'in_game':

                # tem 
                    #print(f"{live_match['match']['teams'][0]['code']} vs {live_match['match']['teams'][1]['code']}")
                #match id
                    print("time azul")
                    print(f"{live_match['gameState']}")
                    print(f"{live_match['blueTeam']['totalGold']}")
                    print(f"{live_match['blueTeam']['totalKills']}")
                    print(f"{live_match['blueTeam']['towers']}")
                    print(f"{live_match['blueTeam']['dragons']}")
                    print(f"{live_match['blueTeam']['barons']}")
                    print(f"{live_match['blueTeam']['inhibitors']}")
                    print("time vermelho")
                    print(f"{live_match['redTeam']['totalGold']}")
                    print(f"{live_match['redTeam']['totalKills']}")
                    print(f"{live_match['redTeam']['towers']}")
                    print(f"{live_match['redTeam']['dragons']}")
                    print(f"{live_match['redTeam']['barons']}")
                    print(f"{live_match['redTeam']['inhibitors']}")
                    #print(f"{live_match['id']}")
                    #get_live_game(api.get_event_details(live_match['id']))
                    sleep(10)

if __name__ == '__main__':
    handle_livematches()
