import unittest
from lolesports_api import Lolesports_API

class Test_Lolesports_API(unittest.TestCase):
    def test_get_leagues(self):
        api = Lolesports_API()
        response = api.get_leagues()
        self.assertTrue(response)
    
    def test_get_tournaments_for_league(self):
        api = Lolesports_API()
        response = api.get_tournaments_for_league()
        self.assertTrue(response)
    
    def test_get_standings(self):
        api = Lolesports_API()
        response = api.get_standings()
        self.assertTrue(response)

    def test_get_schedule(self):
        api = Lolesports_API()
        response = api.get_schedule()
        self.assertTrue(response)

    def test_get_live(self):
        api = Lolesports_API()
        response = api.get_live()
        self.assertTrue(response)

    def test_get_completed_events(self):
        api = Lolesports_API()
        response = api.get_completed_events()
        self.assertTrue(response)

    def test_get_event_details(self):
        api = Lolesports_API()
        response = api.get_event_details(1)
        self.assertTrue(response)

    def test_get_games(self):
        api = Lolesports_API()
        response = api.get_games()
        self.assertTrue(response)

    def test_get_teams(self):
        api = Lolesports_API()
        response = api.get_teams()
        self.assertTrue(response)

    def test_get_window(self):
        api = Lolesports_API()
        response = api.get_window(103462460606814155)
        self.assertTrue(response)

    def test_get_details(self):
        api = Lolesports_API()
        response = api.get_details(100205573001435494)
        self.assertTrue(response)