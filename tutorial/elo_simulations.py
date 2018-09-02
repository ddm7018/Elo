import pandas as pd
import datetime 
from elosports.elo import Elo


df 			= pd.read_csv("nfl_elo.csv")
from2000 	= df[ (df['season']>1999)] 
allTeams 	= set(from2000.team1.tolist())
eloLeague 	= Elo(k = 20)

for team in allTeams:
	eloLeague.addPlayer(team)

currSeason = 2000
for game in from2000.iterrows():
	if game[1].season > currSeason:
		for key in eloLeague.ratingDict.keys():
			eloLeague.ratingDict[key] = eloLeague.ratingDict[key] - ((eloLeague.ratingDict[key] - 1500) * (1/3.))
		currSeason += 1

	if game[1].score1 > game[1].score2:
		eloLeague.gameOver(game[1].team1, game[1].team2,True)
	else:
		eloLeague.gameOver(game[1].team2, game[1].team1,0)

for team in eloLeague.ratingDict.keys():
	print team, eloLeague.ratingDict[team]