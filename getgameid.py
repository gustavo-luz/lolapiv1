from lolesports_api import Lolesports_API
from time import sleep

# coloca a match id e pega  agame id
#get live
api = Lolesports_API()
def handle_livematches():
    #while True:
        print("funcionando2")
        id = '105562822076218136'
        live_matches = api.get_event_details(id)
        for live_match in live_matches['event']['match']['games']:
            #"completed" "unstarted" "inProgress"
            #if live_match['state'] == 'inProgress':
                    print(f"{live_match['id']}")
                    #sleep(1)
                    gameid = live_match['id']
                    #current_game = api.get_api(gameid)
                    #print(current_game)
        for live_match in live_matches['event']['match']['teams']:
            print(f"{live_match['name']}")

handle_livematches()
"""
if __name__ == '__main__':
    handle_livematches()

"""