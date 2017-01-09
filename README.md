# Elo Python Ranking
Orginally developed as way to rank chess players, many leagues and statsicans have applied the ranking system to rank sport teams. 

```python
eloLeague = Elo(k = 20)
eloLeague.addPlayer("Daniel", rating = 1600)
eloLeague.addPlayer("Mike")
eloLeague.expectResult(eloLeague.ratingDict['Daniel'],eloLeague.ratingDict['Mike'])
```

Teams always gain points after winning games and team always lose points after losing. The point differential between the two teams after the game is zero sum. If heavy favorite loses and drops 30 points, the underdog gains 30.

The long-term average for teams is 1500 and typically range from 1200 to 1800

##k-value

```python
eloLeague = Elo(k = 20)
```
The k-factor determins how quickly the rating reacts to new games results. Set too high the ratings will jump around too muc,and conversely if set to low it will take a long time to recognize greatness

##g-value
```python
eloLeague = Elo(k= 20, g = 1)
```
The g-value or margin of value multiplier is introduced to provent autocorrelation

##home-field advantage 
```python
eloLeague = Elo(k = 20, homefield = 100)
```
Home-field advantage is pre-determined. In the NBA, 538 gives home-court advantages to around 100 elo points. Two evently matched team, the home team would have 100 more elo point temporaily. 

##expected score
The formula for determing the expected score can be found 
https://en.wikipedia.org/wiki/Elo_rating_system
```python
eloLeague.expectResult(eloLeague.ratingDict['Daniel'],eloLeague.ratingDict['Mike'])
```

#Future Changes
will continue to clean and run simulations
