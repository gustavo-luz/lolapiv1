from lolesports_api import Lolesports_API
from time import sleep
import pytz, dateutil.parser

# conseguir as partidas do dia de acordo com a liga e start time
#get schedule
api = Lolesports_API()
def handle_livematches():
    while True:
        print("funcionando2")
        crono = api.get_schedule()
        # lpl, cblol_academy
        # ultraliga, primeleague
        liga = 'cblol_academy'
        for cronos in crono['schedule']['events']:
            if cronos['state'] == 'unstarted':
                if cronos['league']['slug'] == liga:
                # tem 
                    print(f"{cronos['match']['teams'][0]['code']} vs {cronos['match']['teams'][1]['code']}")
                #match id
                    print(f"{cronos['startTime']}")
                    utctime = dateutil.parser.parse(cronos['startTime'])
                    localtime = utctime.astimezone(pytz.timezone("America/Sao_Paulo"))
                    print(localtime)
                    #print(f"{cronos['startTime']}")
                    print(f"{cronos['match']['id']}")
                    print(f"{cronos['league']}")
                    #print(f"{live_match['id']}")
                    #get_live_game(api.get_event_details(live_match['id']))
                    sleep(1)

if __name__ == '__main__':
    handle_livematches()