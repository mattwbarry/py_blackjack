# py_blackjack

I created this repo as a sample project. In a job interview, I was asked to pick a card game and write out any methods required to run the game. I picked Blackjack as it is a simple enough game that I could easily write it in an interview setting on a white board, and it's a game that just about everyone knows how to play.

To give a basic overview, the game is made up of two classes - a `Deck` class and a `Player` class. The `Deck` class controls the deck. This class holds the players in `Deck.players`, deals out cards, asks players if they want a hit, and checks for winners. The `Player` class holds each players face down and face up cards, allows players to view these cards, and can get the total points a player holds.

I found one interesting aspect of creating this game was dealing with aces. In Blackjack, a player can choose to use an ace for 1 point or 11 points. To manage this, I built the `Player.add_points()` such that it returns a list of all possible point values that a player holds. Given this, we can much more easily handle determining a winner by using statements such as `if 21 in Player.add_points(): player wins`, `if min(Player.add_points()) > 21: player loses`, and then we can run a loop over the points list to get the highest value under 21.

As this is just a code sample, the game runs but it is not really meant for actual use. For example, I have not yet implemented a betting system and users will have to trust each other not to read the console output on other users turns or else they will be able to see others players face down cards.
