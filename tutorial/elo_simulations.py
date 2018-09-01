import pandas as pd
from elosports.elo import Elo
import datetime 

df = pd.read_csv("nfl_elo.csv")


from2000 = df[ (df['date']>'200-06-01')] 

allTeams = set(from2000.team1.tolist())


eloLeague = Elo(k = 20)

for team in allTeams:
	eloLeague.addPlayer(team)


for game in from2000.iterrows():
	if game[1].score1 > game[1].score2:
		eloLeague.gameOver(game[1].team1, game[1].team2,0)
	else:
		eloLeague.gameOver(game[1].team2, game[1].team1,0)

for team in eloLeague.ratingDict.keys():
	print team, eloLeague.ratingDict[team]