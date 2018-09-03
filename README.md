# Elo Python Ranking
The elo formula is a method of ranking chess players by calculating relative skill. It has found successful applications in team sports. A python package has been developed to calulate expected probability of victory based on prior skill rankings and update the rankings following a result. 

```python
from elosports.elo import Elo
eloLeague = Elo(k = 20)
eloLeague.addPlayer("Daniel", rating = 1600)
eloLeague.addPlayer("Harry")
eloLeague.expectResult(eloLeague.ratingDict['Daniel'],eloLeague.ratingDict['Harry'])
```

The difference in ratings (relative score) determines the probability of victory in a potential match-up.  After a result concludes, the difference determines how many points the victor gains and defeated loses.  A few points transfer from the loser to the winner when the higher rated player wins. Many points transfer when the lower-rated player wins.

The long-term average for teams is 1500 and values generally range from 1200 to 1800.

## k-value

```python
eloLeague = Elo(k = 20)
```
The k-factor determines how the rating reacts to new results. If the value is set too high the ratings will jump around too much and set too low it will take a long time to recognize greatness.

## g-value
```python
eloLeague = Elo(k= 20, g = 1)
```
The g-value or margin of value multiplier introduces a way of preventing autocorrelation.

## Home-field Advantage 
```python
eloLeague = Elo(k = 20, homefield = 100)
```
Home-field advantage is pre-determined. In the NBA and NFL, FiveThirtyEight gives home-court advantages of around 100 Elo points. In the case of two evenly-matched teams, Elo favors the home team.

## Expected Score
The formula for determining the expected probabilistic score can found: 
https://en.wikipedia.org/wiki/Elo_rating_system
```python
eloLeague.expectResult(eloLeague.ratingDict['Daniel'],eloLeague.ratingDict['Harry'])
```
## Update Rankings
```python
eloLeague.gameOver(winner = "Daniel, loser = "Harry")
```
## Tutorial
A tutorial with NFL (American football) simulated Elo rankings can be found in the tutorial section.
