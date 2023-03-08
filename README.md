# Python Lolesports-API

Python implementation of the unoffical Lolesports API of Riot Games. Documentation of the API can be found here: https://vickz84259.github.io/lolesports-api-docs/.

Also includes a small example.

## Installation


```git clone https://github.com/gustavo-luz/lolapiv1```

Activate venv: ```source bin/activate```



To deactivate ```deactivate```


Install dependencies


```python
`pip3 install requests`

`pip install python-dateutil --upgrade`
`pip install urllib --upgrade`

```


execute every 10 seconds

```python
find_live_matches.py searches for ongoing matches
```
```python
find_next_matches.py searches for future matches
```

```python
main_live_game_stats.py receives the match id and keep displaying stats of the game every 10 seconds consuming the lolespors api
```


TODO's

try to reduce the time that updates as much as possible, go testing
the way it is now, it never fails


put a graph with life of players


format to make everything easy to read

future: gold chart, icons,frontend


Examples:

BIG vs MOUZ
2021-03-02T19:00:00Z
2021-03-02 16:00:00-03:00
105562556576287733
{'name': 'Prime League', 'slug': 'primeleague'}

BIG vs MOUZ
105562556576287733
2021-03-02T19:00:00Z
{'id': '105266091639104326', 'slug': 'primeleague', 'name': 'Prime League', 'image': 'http://static.lolesports.com/leagues/PrimeLeagueResized.png', 'priority': 1000}

"esportsGameId":"105562556576287732","esportsMatchId":"105562556576287731

game id: 105562556576287734

https://feed.lolesports.com/livestats/v1/window/105562556576287734?startingTime=2021-03-02T19:00:00Z

https://feed.lolesports.com/livestats/v1/window/105562692794240177?startingTime=2021-03-02T21:00:00Z

https://feed.lolesports.com/livestats/v1/window/105562656844501232?startingTime=2021-03-03T16:30:00Z

IHG vs RGO
2021-03-03T16:30:00Z
2021-03-03 13:30:00-03:00
105562656844501232
{'name': 'Ultraliga', 'slug': 'ultraliga'}
