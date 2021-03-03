from lolesports_api import Lolesports_API
from time import sleep

# só funciona pra jogos no momento
#get live
api = Lolesports_API()
def handle_livematches():
    while True:
        print("funcionando2")
        live_matches = api.get_live()
        for live_match in live_matches['schedule']['events']:
            if live_match['state'] == 'inProgress':
                #id = '105814193355085137'
                #if live_match['match']['id'] == id:
                # tem 
                    print(f"{live_match['match']['teams'][0]['code']} vs {live_match['match']['teams'][1]['code']}")
                #match id
                    print("funcionando2")
                    print(f"{live_match['match']['id']}")
                    print(f"{live_match['startTime']}")
                    print(f"{live_match['league']}")
                    #print(f"{live_match['id']}")
                    #get_live_game(api.get_event_details(live_match['id']))
                    sleep(3)



if __name__ == '__main__':
    handle_livematches()