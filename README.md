# Elo Python Ranking
Orginally developed as way to rank chess players, many leagues and statsicans have applied the ranking system to rank sport teams. 

```python
eloLeague = Elo(k = 20)
eloLeague.addPlayer("Daniel", rating = 1600)
eloLeague.addPlayer("Mike")
eloLeague.expectResult(eloLeague.ratingDict['Daniel'],eloLeague.ratingDict['Mike'])
```
